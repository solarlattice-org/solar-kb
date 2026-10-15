"""Schema terms (classes, slots, enums) and their IRIs, from linkml's SchemaView (site spec §3.4).

native=False makes a slot's IRI its slot_uri, which is what the OWL export uses (use_native_uris=False)."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

from solar_kb.iri import KB


@dataclass(frozen=True)
class Term:
    name: str
    kind: str  # "class" | "slot" | "enum"
    iri: str
    description: str = ""
    is_a: str | None = None
    abstract: bool = False
    range: str | None = None
    multivalued: bool = False
    slots: tuple[str, ...] = ()
    values: tuple[tuple[str, str], ...] = ()  # enum permissible values: (value, description)

    @property
    def local(self) -> bool:
        """True when the IRI is ours (kb:), so the site serves a page for it."""
        return self.iri.startswith(KB)

    @property
    def iri_name(self) -> str:
        return self.iri.rsplit("/", 1)[-1]


@dataclass(frozen=True)
class Ontology:
    iri: str
    version: str
    description: str
    terms: tuple[Term, ...]


def load_ontology(schema_path: Path) -> Ontology:
    sv = SchemaView(str(schema_path))
    default_range = sv.schema.default_range or "string"
    terms = []
    for name, cls in sv.all_classes(imports=False).items():
        terms.append(Term(name=name, kind="class", iri=sv.get_uri(name, expand=True, native=False),
                          description=cls.description or "", is_a=cls.is_a, abstract=bool(cls.abstract),
                          slots=tuple(sv.class_slots(name))))
    for name, slot in sv.all_slots(imports=False).items():
        terms.append(Term(name=name, kind="slot", iri=sv.get_uri(name, expand=True, native=False),
                          description=slot.description or "", range=slot.range or default_range,
                          multivalued=bool(slot.multivalued)))
    for name, enum in sv.all_enums(imports=False).items():
        terms.append(Term(name=name, kind="enum", iri=sv.get_uri(name, expand=True, native=False),
                          description=enum.description or "",
                          values=tuple((v, pv.description or "") for v, pv in enum.permissible_values.items())))
    return Ontology(iri=sv.schema.id, version=str(sv.schema.version), description=sv.schema.description or "",
                    terms=tuple(sorted(terms, key=lambda t: (t.kind, t.name))))
