"""Read-only queries over build/graph.sqlite (used by the CLI and, later, the MCP server)."""
from __future__ import annotations

import datetime
import difflib
import json
import sqlite3
from collections.abc import Iterable, Mapping
from pathlib import Path

from solar_kb.graph import normalize

REVIEW_RANK = {"disputed": 0, "drafted": 1, "verified": 2}
DIRECTIONS = ("out", "in", "both")
FUZZY_CUTOFF = 0.6


def _rank(min_review: str) -> int:
    if min_review not in REVIEW_RANK:
        raise ValueError(f"min_review must be one of {sorted(REVIEW_RANK)}")
    return REVIEW_RANK[min_review]


class Graph:
    def __init__(self, db_path: Path):
        db_path = Path(db_path)
        if not db_path.is_file():
            raise FileNotFoundError(f"graph database not found: {db_path} (run `solar-kb build`)")
        self._con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        self._con.row_factory = sqlite3.Row

    def close(self) -> None:
        self._con.close()

    @property
    def kb_version(self) -> str:
        return self._con.execute("SELECT value FROM meta WHERE key='kb_version'").fetchone()[0]

    def _citations(self, record_id: str, claim_id: str) -> list[dict]:
        rows = self._con.execute(
            "SELECT src, loc, h FROM citations WHERE record_id=? AND claim_id=? ORDER BY rowid",
            (record_id, claim_id),
        )
        return [dict(r) for r in rows]

    def resolve(self, text: str, types: Iterable[str] | None = None, limit: int = 5,
                include_proposed: bool = False) -> list[dict]:
        norm = normalize(text or "")
        if not norm or limit < 1:
            return []
        wanted = set(types) if types else None
        rows = self._con.execute(
            "SELECT a.norm, n.id, n.type, n.name, n.status FROM aliases a JOIN nodes n ON n.id=a.id"
        ).fetchall()
        best: dict[str, dict] = {}
        for row in rows:
            if wanted and row["type"] not in wanted:
                continue
            if row["status"] == "proposed" and not include_proposed:
                continue
            if row["norm"] == norm:
                score = 1.0
            else:
                score = difflib.SequenceMatcher(None, norm, row["norm"]).ratio()
                if score < FUZZY_CUTOFF:
                    continue
            if row["id"] not in best or score > best[row["id"]]["score"]:
                best[row["id"]] = {"id": row["id"], "type": row["type"], "name": row["name"],
                                   "score": round(score, 3)}
        return sorted(best.values(), key=lambda m: (-m["score"], m["id"]))[:limit]

    def get_entity(self, record_id: str) -> dict | None:
        row = self._con.execute("SELECT * FROM nodes WHERE id=?", (record_id,)).fetchone()
        if row is None:
            return None
        return {"id": row["id"], "type": row["type"], "name": row["name"], "status": row["status"],
                "layer": row["layer"], "body": row["body"], "data": json.loads(row["data_json"]),
                "kb_version": self.kb_version}

    def _edge(self, row: sqlite3.Row) -> dict:
        return {"source": row["record_id"], "rel": row["rel"], "target": row["target"],
                "claim_id": row["claim_id"], "review": row["review"], "by": row["by_method"],
                "conditions": row["conditions"], "note": row["note"],
                "superseded_by": row["superseded_by"], "valid_from": row["valid_from"],
                "valid_to": row["valid_to"],
                "cite": self._citations(row["record_id"], row["claim_id"])}

    def neighbors(self, record_id: str, rel: str | None = None, direction: str = "out",
                  min_review: str = "drafted") -> list[dict]:
        if direction not in DIRECTIONS:
            raise ValueError(f"direction must be one of {DIRECTIONS}")
        floor = _rank(min_review)
        clauses = []
        if direction in ("out", "both"):
            clauses.append("record_id = :id")
        if direction in ("in", "both"):
            clauses.append("target = :id")
        sql = f"SELECT * FROM claims WHERE rel IS NOT NULL AND ({' OR '.join(clauses)})"
        params: dict = {"id": record_id}
        if rel is not None:
            sql += " AND rel = :rel"
            params["rel"] = rel
        rows = self._con.execute(sql + " ORDER BY record_id, claim_id", params).fetchall()
        return [self._edge(r) for r in rows if REVIEW_RANK[r["review"]] >= floor]

    def differential(self, observations: Iterable[str], min_review: str = "drafted", k: int = 5,
                     field_evidence: Mapping[tuple[str, str], int] | None = None,
                     as_of: str | None = None) -> dict:
        """Spec §8.1: rank FailureModes by matched observations; return discriminating tests.

        Only current claims count: superseded claims, and claims whose validity window does not
        contain `as_of` (default: today, ISO date), are ignored. Each candidate lists the claims
        supporting each match; disputed claims filtered out by `min_review` are reported in
        `disputed_matches` so they are surfaced rather than silently dropped.
        """
        if k < 1:
            raise ValueError("k must be >= 1")
        floor = _rank(min_review)
        as_of = as_of or datetime.date.today().isoformat()
        field_evidence = field_evidence or {}
        obs = list(dict.fromkeys(observations))
        types = dict(self._con.execute("SELECT id, type FROM nodes WHERE status='active'").fetchall())
        known = [o for o in obs if types.get(o) in ("Symptom", "Measurement")]
        unknown = [o for o in obs if o not in known]

        def current(row: sqlite3.Row) -> bool:
            return (row["superseded_by"] is None
                    and (row["valid_from"] is None or row["valid_from"] <= as_of)
                    and (row["valid_to"] is None or row["valid_to"] >= as_of)
                    and row["record_id"] in types and row["target"] in types)

        def claims(rel: str) -> list[sqlite3.Row]:
            rows = self._con.execute(
                "SELECT * FROM claims WHERE rel=? ORDER BY record_id, claim_id", (rel,)).fetchall()
            return [r for r in rows if current(r)]

        def ref(row: sqlite3.Row) -> dict:
            return {"record_id": row["record_id"], "claim_id": row["claim_id"], "review": row["review"]}

        observed_as: dict[str, list[tuple[str, dict]]] = {}
        for row in claims("observed_as"):
            if REVIEW_RANK[row["review"]] >= floor:
                observed_as.setdefault(row["record_id"], []).append((row["target"], ref(row)))

        reach: dict[str, dict[str, list[dict]]] = {}
        disputed_matches = []
        for row in claims("presents_as"):
            fm, symptom = row["record_id"], row["target"]
            reached = [(symptom, [ref(row)])] + [(m, [ref(row), r]) for m, r in observed_as.get(symptom, [])]
            if REVIEW_RANK[row["review"]] < floor:
                disputed_matches += [{"failure_mode": fm, "observation": o, "record_id": fm,
                                      "claim_id": row["claim_id"]}
                                     for o, _ in reached if o in known and row["review"] == "disputed"]
                continue
            for o, path in reached:
                support = reach.setdefault(fm, {}).setdefault(o, [])
                support += [r for r in path if r not in support]

        candidates = []
        for fm, support in reach.items():
            matched = [o for o in known if o in support]
            if not matched:
                continue
            fe = sum(field_evidence.get((o, fm), 0) for o in matched)
            candidates.append({"id": fm, "name": self._name(fm), "score": len(matched),
                               "matched": matched, "unmatched": [o for o in known if o not in matched],
                               "field_evidence": fe,
                               "support": [{"observation": o, "claims": support[o]} for o in matched]})
        candidates.sort(key=lambda c: (-c["score"], -c["field_evidence"], c["id"]))
        top = candidates[:k]
        top_ids = {c["id"] for c in top}

        discriminators = []
        for row in claims("distinguished_from"):
            if REVIEW_RANK[row["review"]] < floor:
                continue
            if row["record_id"] in top_ids and row["target"] in top_ids:
                edge = self._edge(row)
                method = self.get_entity(row["by_method"]) if row["by_method"] else None
                edge["by_tool_ids"] = (method or {}).get("data", {}).get("tool_ids", [])
                discriminators.append(edge)
        return {"candidates": top, "total_candidates": len(candidates),
                "truncated": len(candidates) > k, "discriminators": discriminators,
                "disputed_matches": disputed_matches, "unknown_observations": unknown,
                "as_of": as_of, "kb_version": self.kb_version}

    def _name(self, record_id: str) -> str:
        return self._con.execute("SELECT name FROM nodes WHERE id=?", (record_id,)).fetchone()[0]
