"""Record files on disk -> an in-memory Corpus.

Layout: <root>/records/<type-dir>/<slug>.md. The public repo is one root; the private
overlay (solar-brain/overlay) is a second root loaded with layer="overlay".
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from solar_kb.violation import Violation
from solar_kb.yamlio import FrontMatterError, split_front_matter

# type-dir -> (record type, id prefix)
TYPE_DIRS: dict[str, tuple[str, str]] = {
    "failure-modes": ("FailureMode", "fm"),
    "stressors": ("Stressor", "stressor"),
    "symptoms": ("Symptom", "symptom"),
    "measurements": ("Measurement", "meas"),
    "detection-methods": ("DetectionMethod", "method"),
    "mitigations": ("Mitigation", "mit"),
    "components": ("Component", "comp"),
    "sources": ("Source", "src"),
    "cases": ("Case", "case"),
    "data-examples": ("DataExample", "dex"),
}
TYPE_PREFIX: dict[str, str] = {t: p for t, p in TYPE_DIRS.values()}
TYPE_DIR: dict[str, str] = {t: d for d, (t, _) in TYPE_DIRS.items()}
OVERLAY_ONLY_TYPES = frozenset({"Case"})
LAYERS = ("public", "overlay")


@dataclass
class Record:
    data: dict
    body: str
    path: Path
    layer: str
    type_dir: str

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
        for path in sorted(type_dir.glob("*.md")):
            try:
                data, body = split_front_matter(path.read_text(encoding="utf-8"))
            except (FrontMatterError, UnicodeDecodeError) as exc:
                corpus.load_errors.append(Violation("parse", str(path), str(exc)))
                continue
            record = Record(data=data, body=body, path=path, layer=layer, type_dir=type_dir.name)
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
    corpus = Corpus()
    _load_root(Path(root), "public", corpus)
    if overlay is not None:
        _load_root(Path(overlay), "overlay", corpus)
    return corpus
