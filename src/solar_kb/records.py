"""Record files on disk -> an in-memory Corpus.

Layout: <root>/records/<type-dir>/<slug>.md. The public repo is one root; the private
overlay (solar-brain/overlay) is a second root loaded with layer="overlay".
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from solar_kb.violation import Violation
from solar_kb.yamlio import FrontMatterError, drop_nulls, split_front_matter

# type-dir -> (record type, id prefix)
TYPE_DIRS: dict[str, tuple[str, str]] = {
    "failure-modes": ("FailureMode", "fm"),
    "stressors": ("Stressor", "stressor"),
    "symptoms": ("Symptom", "symptom"),
    "measurements": ("Measurement", "meas"),
    "detection-methods": ("DetectionMethod", "method"),
    "mitigations": ("Mitigation", "mit"),
    "components": ("Component", "comp"),
    "fault-codes": ("FaultCode", "fc"),
    "event-concepts": ("EventConcept", "ec"),
    "sources": ("Source", "src"),
    # Schema 0.5.0 (spec B §4.1), in module order: core, equipment, events, control, communication, practice,
    # regulation, engineering.
    "organizations": ("Organization", "org"),
    "regions": ("Region", "region"),
    "roles": ("Role", "role"),
    "products": ("Product", "prod"),
    "firmware-releases": ("FirmwareRelease", "fw"),
    "tools": ("Tool", "tool"),
    "operating-states": ("OperatingState", "state"),
    "functions": ("Function", "func"),
    "parameters": ("Parameter", "param"),
    "grid-profiles": ("GridProfile", "profile"),
    "protocols": ("Protocol", "proto"),
    "registers": ("Register", "reg"),
    "procedures": ("Procedure", "proc"),
    "hazards": ("Hazard", "hazard"),
    "standards": ("Standard", "std"),
    "requirements": ("Requirement", "req"),
    "programs": ("Program", "prog"),
    "concepts": ("Concept", "concept"),
    "metrics": ("Metric", "metric"),
    "calculation-methods": ("CalculationMethod", "calc"),
    "architectures": ("Architecture", "arch"),
    "cases": ("Case", "case"),
    "data-examples": ("DataExample", "dex"),
}
TYPE_PREFIX: dict[str, str] = {t: p for t, p in TYPE_DIRS.values()}
TYPE_DIR: dict[str, str] = {t: d for d, (t, _) in TYPE_DIRS.items()}
OVERLAY_ONLY_TYPES = frozenset({"Case", "DataExample"})
LAYERS = ("public", "overlay")


@dataclass
class Record:
    data: dict
    body: str
    path: Path
    layer: str
    type_dir: str
    root: Path | None = None  # the repo/overlay root the record was loaded from

    @property
    def rel_path(self) -> str:
        """Path relative to its root (stable across machines), e.g. records/failure-modes/pid.md."""
        return str(self.path.relative_to(self.root)) if self.root is not None else str(self.path)

    @property
    def id(self) -> str | None:
        value = self.data.get("id")
        return value if isinstance(value, str) else None

    @property
    def type(self) -> str | None:
        value = self.data.get("type")
        return value if isinstance(value, str) else None

    def claims(self) -> list[dict]:
        claims = self.data.get("claims")
        if not isinstance(claims, list):
            return []
        return [c for c in claims if isinstance(c, dict)]


@dataclass
class Corpus:
    records: dict[str, Record] = field(default_factory=dict)
    load_errors: list[Violation] = field(default_factory=list)
    layers: tuple[str, ...] = ()  # which roots were loaded: ("public",) or ("public", "overlay")

    def by_layer(self, layer: str) -> list[Record]:
        return [r for r in self.records.values() if r.layer == layer]


def _load_root(root: Path, layer: str, corpus: Corpus) -> None:
    records_dir = root / "records"
    if not records_dir.is_dir():
        return
    for type_dir in sorted(p for p in records_dir.iterdir() if p.is_dir()):
        if type_dir.name not in TYPE_DIRS:
            corpus.load_errors.append(
                Violation("layout", str(type_dir), f"unknown record directory '{type_dir.name}'")
            )
            continue
        for path in sorted(type_dir.iterdir()):
            if path.name.startswith("."):
                continue  # .gitkeep, editor/OS files
            if path.is_dir():
                corpus.load_errors.append(Violation("layout", str(path), "nested directories are not loaded"))
                continue
            if path.suffix != ".md":
                corpus.load_errors.append(Violation("layout", str(path), "records must be .md files"))
                continue
            try:
                data, body = split_front_matter(path.read_text(encoding="utf-8"))
            except (FrontMatterError, UnicodeDecodeError, OSError) as exc:
                corpus.load_errors.append(Violation("parse", str(path), str(exc)))
                continue
            record = Record(data=drop_nulls(data), body=body, path=path, layer=layer, type_dir=type_dir.name,
                            root=root)
            rid = record.id
            if rid is None:
                corpus.load_errors.append(Violation("parse", str(path), "missing string 'id'"))
                continue
            if rid in corpus.records:
                other = corpus.records[rid].path
                corpus.load_errors.append(
                    Violation("duplicate-id", str(path), f"id also used by {other}", record_id=rid)
                )
                continue
            corpus.records[rid] = record


def load_corpus(root: Path, overlay: Path | None = None) -> Corpus:
    corpus = Corpus(layers=("public",) if overlay is None else ("public", "overlay"))
    _load_root(Path(root), "public", corpus)
    if overlay is not None:
        if not (Path(overlay) / "records").is_dir():
            corpus.load_errors.append(
                Violation("layout", str(overlay), "overlay has no records/ directory")
            )
        _load_root(Path(overlay), "overlay", corpus)
    return corpus
