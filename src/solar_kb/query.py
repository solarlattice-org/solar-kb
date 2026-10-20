"""Read-only queries over build/graph.sqlite (used by the CLI and, later, the MCP server)."""
from __future__ import annotations

import datetime
import difflib
import json
import sqlite3
from collections.abc import Iterable, Mapping
from pathlib import Path

from solar_kb.codes import parse_code, query_code
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
                score, match = 1.0, "exact"
            else:
                match = "fuzzy"
                score = difflib.SequenceMatcher(None, norm, row["norm"]).ratio()
                if score < FUZZY_CUTOFF:
                    continue
            if row["id"] not in best or score > best[row["id"]]["score"]:
                best[row["id"]] = {"id": row["id"], "type": row["type"], "name": row["name"],
                                   "score": round(score, 3), "match": match}
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
        rows = self._con.execute(sql + " ORDER BY record_id, rowid", params).fetchall()
        return [self._edge(r) for r in rows if REVIEW_RANK[r["review"]] >= floor]

    def resolve_code(self, text: str, make: str | None = None, family: str | None = None,
                     limit: int = 20) -> list[dict]:
        """Plan 4d: FaultCode records for a printed or spoken code ("3701", "event 3501", "Protect0090", "CRIT-7").

        The v1 `lookup_fault_code` order: the exact code_key; else a printed range containing the number under the
        same vendor prefix; else the bare number under any prefix. The first step with a hit wins (`match` names it).
        Within it, records of the given make rank first, then of the given family; neither filters, so a code of
        another make is still found, lower down."""
        key = query_code(text or "")
        if not key.key or limit < 1:
            return []
        rows = self._con.execute(
            "SELECT f.*, n.name, n.data_json FROM fault_codes f JOIN nodes n ON n.id = f.record_id ORDER BY f.record_id"
        ).fetchall()
        attempts = [("exact", lambda r: r["code_key"] == key.key)]
        if key.number is not None and key.number_end is None:
            attempts.append(("range", lambda r: r["code_from"] is not None and r["code_from"] <= key.number <= r["code_to"]
                             and parse_code(r["code_key"]).prefix == key.prefix))
            attempts.append(("number", lambda r: r["code_from"] is None and parse_code(r["code_key"]).number == key.number))
        for match, test in attempts:
            hits = [r for r in rows if test(r)]
            if hits:
                break
        else:
            return []

        def rank(r: sqlite3.Row) -> tuple:
            return (0 if make and r["make"] == make else 1, 0 if family and r["model_family"] == family else 1,
                    r["record_id"])

        out = []
        for r in sorted(hits, key=rank)[:limit]:
            data = json.loads(r["data_json"])
            out.append({"id": r["record_id"], "type": "FaultCode", "name": r["name"], "make": r["make"],
                        "make_name": data.get("make_name"), "model_family": r["model_family"],
                        "family_name": data.get("family_name"), "code": data.get("code"), "code_key": r["code_key"],
                        "display_message": data.get("display_message"), "match": match, "query_key": key.key})
        return out

    def differential(self, observations: Iterable[str], min_review: str = "drafted", k: int = 5,
                     field_evidence: Mapping[tuple[str, str], int] | None = None,
                     as_of: str | None = None) -> dict:
        """Spec §8.1: rank FailureModes by matched observations; return discriminating tests.

        Only current claims count: superseded claims, and claims whose validity window does not
        contain `as_of` (default: today, ISO date), are ignored. Each candidate lists the claims
        supporting each match; disputed claims filtered out by `min_review` are reported in
        `disputed_matches` so they are surfaced rather than silently dropped. `known_observations` are the
        Symptom/Measurement ids that were scored; everything else given (or reached) is in `unknown_observations`.

        A FaultCode observation (Plan 4d) is expanded through its `reports` claims at or above `min_review` into the
        Symptoms it reports, listed in `via_code`; `indicates` is never scored, so §8.1 scoring is unchanged. Nothing
        vanishes in the expansion: a reported Symptom that is only a proposed stub is listed in `unknown_observations`
        exactly as it would be when given directly, a disputed `reports` claim below the floor is a `disputed_matches`
        entry (`failure_mode` None, `symptom` the target), and a code that reports nothing at this floor is itself an
        unknown observation, so a pinned code the KB cannot use is told apart from a KB that lacks the failure mode.
        """
        if k < 1:
            raise ValueError("k must be >= 1")
        floor = _rank(min_review)
        as_of = as_of or datetime.date.today().isoformat()
        field_evidence = field_evidence or {}
        types = dict(self._con.execute("SELECT id, type FROM nodes WHERE status='active'").fetchall())

        def current(row: sqlite3.Row, target_active: bool = True) -> bool:
            return (row["superseded_by"] is None
                    and (row["valid_from"] is None or row["valid_from"] <= as_of)
                    and (row["valid_to"] is None or row["valid_to"] >= as_of)
                    and row["record_id"] in types and (not target_active or row["target"] in types))

        def claims(rel: str, target_active: bool = True) -> list[sqlite3.Row]:
            rows = self._con.execute(
                "SELECT * FROM claims WHERE rel=? ORDER BY record_id, rowid", (rel,)).fetchall()
            return [r for r in rows if current(r, target_active)]

        def ref(row: sqlite3.Row) -> dict:
            return {"record_id": row["record_id"], "claim_id": row["claim_id"], "review": row["review"]}

        via_code: dict[str, list[str]] = {}
        disputed_matches: list[dict] = []
        obs: list[str] = []
        reports: list[sqlite3.Row] | None = None
        for o in dict.fromkeys(observations):
            if types.get(o) != "FaultCode":
                obs.append(o)
                continue
            if reports is None:
                reports = claims("reports", target_active=False)  # a proposed Symptom surfaces as unknown, not silence
            reported = []
            for row in reports:
                if row["record_id"] != o:
                    continue
                if REVIEW_RANK[row["review"]] >= floor:
                    reported.append(row["target"])
                elif row["review"] == "disputed":
                    disputed_matches.append({"failure_mode": None, "observation": o, "symptom": row["target"],
                                             "record_id": o, "claim_id": row["claim_id"]})
            via_code[o] = list(dict.fromkeys(reported))
            obs += via_code[o] or [o]  # a code that reports nothing at this floor is itself an unknown observation
        obs = list(dict.fromkeys(obs))
        known = [o for o in obs if types.get(o) in ("Symptom", "Measurement")]
        unknown = [o for o in obs if o not in known]

        observed_as: dict[str, list[tuple[str, dict]]] = {}
        for row in claims("observed_as"):
            if REVIEW_RANK[row["review"]] >= floor:
                observed_as.setdefault(row["record_id"], []).append((row["target"], ref(row)))

        reach: dict[str, dict[str, list[dict]]] = {}
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
                "disputed_matches": disputed_matches, "known_observations": known, "unknown_observations": unknown,
                "via_code": via_code, "as_of": as_of, "kb_version": self.kb_version}

    def _name(self, record_id: str) -> str:
        return self._con.execute("SELECT name FROM nodes WHERE id=?", (record_id,)).fetchone()[0]
