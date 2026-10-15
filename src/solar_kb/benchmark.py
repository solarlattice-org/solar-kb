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
      source: {cite: "src:iea-pvps-t13-01-2014#sec=4.3", h: 3f2a9c0b1d4e}

Failure-mode ids follow the compiler's worklist convention: fm:<pv-root-cause slug> for the seeded causes.
An observation without an `id` is resolved with Graph.resolve (Symptom/Measurement, best match); unresolved
observations are reported separately, so a weak resolver is never mistaken for a weak graph.
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
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
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
        if not isinstance(source, dict) or set(source) != {"cite", "h"} or not CITE.match(str(source["cite"])) \
                or not HASH.match(str(source["h"])):
            raise CaseError(f"{cid}: source needs cite (src:<id>#<loc>) and h (12 hex)")
        cases.append(Case(cid, tuple(observations), expected, tuple(acceptable), source["cite"], source["h"]))
    return cases


@dataclass(frozen=True)
class CaseResult:
    id: str
    rank: int | None  # 1-based rank of the expected (or an acceptable) failure mode, else None
    candidates: tuple[str, ...]
    unresolved: tuple[str, ...]  # observation texts that matched no Symptom/Measurement


@dataclass
class BenchmarkReport:
    results: list[CaseResult] = field(default_factory=list)
    kb_version: str = ""

    def top(self, k: int) -> float:
        return round(sum(1 for r in self.results if r.rank is not None and r.rank <= k) / len(self.results), 4) \
            if self.results else 0.0

    def summary(self) -> dict:
        return {"cases": len(self.results), "top1": self.top(1), "top3": self.top(3), "kb_version": self.kb_version,
                "unresolved_observations": sum(len(r.unresolved) for r in self.results),
                "misses": [r.id for r in self.results if r.rank is None or r.rank > 3]}


def run_benchmark(graph, cases: list[Case], k: int = 5, min_review: str = "drafted") -> BenchmarkReport:
    report = BenchmarkReport(kb_version=graph.kb_version)
    for case in cases:
        ids, unresolved = [], []
        for obs in case.observations:
            if obs.id:
                ids.append(obs.id)
                continue
            matches = graph.resolve(obs.text, types=["Symptom", "Measurement"], limit=1)
            if matches:
                ids.append(matches[0]["id"])
            else:
                unresolved.append(obs.text)
        result = graph.differential(ids, min_review=min_review, k=k) if ids else {"candidates": []}
        candidates = tuple(c["id"] for c in result["candidates"])
        correct = {case.expected, *case.acceptable}
        rank = next((i for i, c in enumerate(candidates, start=1) if c in correct), None)
        report.results.append(CaseResult(case.id, rank, candidates, tuple(unresolved)))
    return report
