"""Differential-diagnosis benchmark (spec §7.3, reframed 2026-10-15): triage cases drawn from the cited PV
literature, scored against the graph's `differential` query.

eval/public/differential.yaml:

    - id: pid-negative-end-humid
      observations:                              # what a technician reports
        - text: gradual power loss across several strings over two humid years
        - text: darkened cells in night-time EL, concentrated at the negative end of strings
          id: meas:el-negative-end-darkening       # optional: pin to a graph record once it exists
      expected: fm:potential-induced-degradation
      acceptable: []                             # other failure modes that also count as correct
      source: {cite: "src:iea-pvps-t13-01-2014#sec=4.3", h: "3f2a9c0b1d4e"}   # quote h (all-digit hashes)

Failure-mode ids follow the compiler's worklist convention: fm:<pv-root-cause slug> for the seeded causes.
An observation without an `id` is resolved with Graph.resolve (Symptom/Measurement, best match; every resolution
is recorded with its exact/fuzzy match and score). Unresolved observations and unknown pinned ids are counted,
each miss carries a reason (unresolved | no_candidates | ranked_out), and `top3_resolved` scores only cases whose
observations all resolved, so a weak resolver is never mistaken for a weak graph. Alphabetical tie-breaking is
made visible through `tied` and `top3_pessimistic` (the worst rank within a tie group).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FM = re.compile(r"^fm:[a-z0-9]+(-[a-z0-9]+)*$")
OBS_ID = re.compile(r"^(symptom|meas):[a-z0-9]+(-[a-z0-9]+)*$")
CITE = re.compile(r"^src:[a-z0-9]+(-[a-z0-9]+)*#\S+$")
HASH = re.compile(r"^[0-9a-f]{12}$")
_CASE_KEYS = {"id", "observations", "expected", "acceptable", "source", "notes"}


class CaseError(ValueError):
    pass


@dataclass(frozen=True)
class Observation:
    text: str
    id: str | None = None


@dataclass(frozen=True)
class Case:
    id: str
    observations: tuple[Observation, ...]
    expected: str
    acceptable: tuple[str, ...]
    source_cite: str
    source_h: str


def load_cases(path: Path) -> list[Case]:
    try:
        data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise CaseError(f"{path}: invalid YAML: {exc}") from exc
    except UnicodeDecodeError as exc:
        raise CaseError(f"{path}: not UTF-8: {exc}") from exc
    if not isinstance(data, list) or not data:
        raise CaseError(f"{path}: expected a non-empty YAML list of cases")
    cases, seen = [], set()
    for i, raw in enumerate(data):
        where = f"{Path(path).name}[{i}]"
        if not isinstance(raw, dict) or set(raw) - _CASE_KEYS:
            raise CaseError(f"{where}: must be a mapping with keys from {sorted(_CASE_KEYS)}")
        cid = raw.get("id")
        if not isinstance(cid, str) or not ID.match(cid) or cid in seen:
            raise CaseError(f"{where}: id must be a unique lowercase slug")
        seen.add(cid)
        obs_raw = raw.get("observations")
        if not isinstance(obs_raw, list) or not obs_raw:
            raise CaseError(f"{cid}: observations must be a non-empty list")
        observations = []
        for o in obs_raw:
            if not isinstance(o, dict) or not isinstance(o.get("text"), str) or not o["text"].strip() \
                    or set(o) - {"text", "id"}:
                raise CaseError(f"{cid}: each observation needs 'text' (and optionally 'id')")
            if "id" in o and not (isinstance(o["id"], str) and OBS_ID.match(o["id"])):
                raise CaseError(f"{cid}: observation id must be symptom:<slug> or meas:<slug>")
            observations.append(Observation(o["text"].strip(), o.get("id")))
        expected, acceptable = raw.get("expected"), raw.get("acceptable") or []
        if not isinstance(expected, str) or not FM.match(expected):
            raise CaseError(f"{cid}: expected must be fm:<slug>")
        if not isinstance(acceptable, list) or not all(isinstance(a, str) and FM.match(a) for a in acceptable):
            raise CaseError(f"{cid}: acceptable must be a list of fm:<slug>")
        source = raw.get("source")
        if not isinstance(source, dict) or set(source) != {"cite", "h"}:
            raise CaseError(f"{cid}: source needs cite (src:<id>#<loc>) and h (12 hex)")
        if not isinstance(source["cite"], str) or not isinstance(source["h"], str):
            raise CaseError(f"{cid}: quote source cite and h as strings (an all-digit h loads as a number)")
        if not CITE.match(source["cite"]) or not HASH.match(source["h"]):
            raise CaseError(f"{cid}: source needs cite (src:<id>#<loc>) and h (12 hex)")
        cases.append(Case(cid, tuple(observations), expected, tuple(acceptable), source["cite"], source["h"]))
    return cases


@dataclass(frozen=True)
class CaseResult:
    id: str
    rank: int | None  # 1-based rank of the expected (or an acceptable) failure mode, else None
    candidates: tuple[str, ...]
    unresolved: tuple[str, ...]  # observation texts that matched no Symptom/Measurement
    unknown_ids: tuple[str, ...] = ()  # pinned ids that are not active Symptom/Measurement records
    resolved: tuple[dict, ...] = ()  # {"text", "id", "match": pinned|exact|fuzzy, "score"} per observation used
    tied: int = 0  # candidates sharing the hit's score (1 = no tie); 0 when there is no hit
    pessimistic_rank: int | None = None  # worst rank within the hit's tie group
    reason: str = "hit"  # hit | unresolved | no_candidates | ranked_out
    expected_known: bool = True  # expected id exists in the graph as a FailureMode


@dataclass
class BenchmarkReport:
    results: list[CaseResult] = field(default_factory=list)
    kb_version: str = ""

    def _share(self, results: list[CaseResult], k: int, pessimistic: bool = False) -> float:
        if not results:
            return 0.0
        ranks = [r.pessimistic_rank if pessimistic else r.rank for r in results]
        return round(sum(1 for rank in ranks if rank is not None and rank <= k) / len(results), 4)

    def top(self, k: int) -> float:
        return self._share(self.results, k)

    def summary(self) -> dict:
        resolved_cases = [r for r in self.results if not r.unresolved and not r.unknown_ids and r.expected_known]
        return {"cases": len(self.results), "top1": self.top(1), "top3": self.top(3),
                "top3_pessimistic": self._share(self.results, 3, pessimistic=True),
                "top3_resolved": self._share(resolved_cases, 3), "kb_version": self.kb_version,
                "unresolved_observations": sum(len(r.unresolved) + len(r.unknown_ids) for r in self.results),
                "cases_with_unresolved": sum(1 for r in self.results if r.unresolved or r.unknown_ids),
                "cases_fully_unresolved": sum(1 for r in self.results if r.reason == "unresolved"),
                "fuzzy_resolutions": sum(1 for r in self.results for x in r.resolved if x["match"] == "fuzzy"),
                "unknown_expected": [r.id for r in self.results if not r.expected_known],
                "misses": [r.id for r in self.results if r.rank is None or r.rank > 3],
                "miss_reasons": {r.id: r.reason for r in self.results if r.reason != "hit"}}


def run_benchmark(graph, cases: list[Case], min_review: str = "drafted", exact_only: bool = False) -> BenchmarkReport:
    """Score every case; candidates are ranked in full (no top-k cut), so ranks and tie groups are exact."""
    from solar_kb.query import REVIEW_RANK

    if min_review not in REVIEW_RANK:
        raise ValueError(f"min_review must be one of {sorted(REVIEW_RANK)}")
    report = BenchmarkReport(kb_version=graph.kb_version)
    for case in cases:
        ids, unresolved, resolved = [], [], []
        for obs in case.observations:
            if obs.id:
                ids.append(obs.id)
                resolved.append({"text": obs.text, "id": obs.id, "match": "pinned", "score": 1.0})
                continue
            matches = graph.resolve(obs.text, types=["Symptom", "Measurement"], limit=1)
            if matches and (matches[0]["match"] == "exact" or not exact_only):
                ids.append(matches[0]["id"])
                resolved.append({"text": obs.text, "id": matches[0]["id"], "match": matches[0]["match"],
                                 "score": matches[0]["score"]})
            else:
                unresolved.append(obs.text)
        result = graph.differential(ids, min_review=min_review, k=10_000) if ids else \
            {"candidates": [], "unknown_observations": []}
        unknown = tuple(result.get("unknown_observations", []))
        scored = [(c["id"], c["score"]) for c in result["candidates"]]
        correct = {case.expected, *case.acceptable}
        rank = next((i for i, (cid, _) in enumerate(scored, start=1) if cid in correct), None)
        tied, pessimistic = 0, None
        if rank is not None:
            hit_score = scored[rank - 1][1]
            group = [i for i, (_, sc) in enumerate(scored, start=1) if sc == hit_score]
            tied, pessimistic = len(group), max(group)
        if rank is not None and rank <= 3:
            reason = "hit"
        elif not ids or len(unknown) == len(ids):
            reason = "unresolved"
        elif not scored:
            reason = "no_candidates"
        else:
            reason = "ranked_out"
        known = all((graph.get_entity(f) or {}).get("type") == "FailureMode" for f in correct)
        report.results.append(CaseResult(case.id, rank, tuple(cid for cid, _ in scored), tuple(unresolved), unknown,
                                         tuple(resolved), tied, pessimistic, reason, known))
    return report
