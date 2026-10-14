"""Read-only queries over build/graph.sqlite (used by the CLI and, later, the MCP server)."""
from __future__ import annotations

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
            "SELECT src, loc FROM citations WHERE record_id=? AND claim_id=? ORDER BY rowid",
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
                     field_evidence: Mapping[tuple[str, str], int] | None = None) -> dict:
        """Spec §8.1: rank FailureModes by matched observations; return discriminating tests."""
        if k < 1:
            raise ValueError("k must be >= 1")
        floor = _rank(min_review)
        field_evidence = field_evidence or {}
        obs = list(dict.fromkeys(observations))
        types = dict(self._con.execute("SELECT id, type FROM nodes WHERE status='active'").fetchall())
        known = [o for o in obs if types.get(o) in ("Symptom", "Measurement")]
        unknown = [o for o in obs if o not in known]

        def edges(rel: str) -> list[tuple[str, str]]:
            rows = self._con.execute(
                "SELECT record_id, target, review FROM claims WHERE rel=?", (rel,)).fetchall()
            return [(r["record_id"], r["target"]) for r in rows
                    if REVIEW_RANK[r["review"]] >= floor and r["record_id"] in types
                    and r["target"] in types]

        observed_as: dict[str, set[str]] = {}
        for symptom, measurement in edges("observed_as"):
            observed_as.setdefault(symptom, set()).add(measurement)
        reach: dict[str, set[str]] = {}
        for fm, symptom in edges("presents_as"):
            reach.setdefault(fm, set()).update({symptom, *observed_as.get(symptom, ())})

        candidates = []
        for fm, reachable in reach.items():
            matched = [o for o in known if o in reachable]
            if not matched:
                continue
            fe = sum(field_evidence.get((o, fm), 0) for o in matched)
            candidates.append({"id": fm, "name": self._name(fm), "score": len(matched),
                               "matched": matched, "unmatched": [o for o in known if o not in matched],
                               "field_evidence": fe})
        candidates.sort(key=lambda c: (-c["score"], -c["field_evidence"], c["id"]))
        top = candidates[:k]
        top_ids = {c["id"] for c in top}

        discriminators = []
        rows = self._con.execute(
            "SELECT * FROM claims WHERE rel='distinguished_from' ORDER BY record_id, claim_id")
        for row in rows:
            if REVIEW_RANK[row["review"]] < floor:
                continue
            if row["record_id"] in top_ids and row["target"] in top_ids:
                edge = self._edge(row)
                method = self.get_entity(row["by_method"]) if row["by_method"] else None
                edge["by_tool_ids"] = (method or {}).get("data", {}).get("tool_ids", [])
                discriminators.append(edge)
        return {"candidates": top, "discriminators": discriminators,
                "unknown_observations": unknown, "kb_version": self.kb_version}

    def _name(self, record_id: str) -> str:
        return self._con.execute("SELECT name FROM nodes WHERE id=?", (record_id,)).fetchone()[0]
