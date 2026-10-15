"""Which pages exist, and what each template is given (site spec §2.1, §3.4)."""
from __future__ import annotations

from dataclasses import dataclass

from solar_kb.iri import KB
from solar_kb.records import Corpus, Record
from solar_kb.site import views
from solar_kb.site.paths import PUBLIC_TYPES, href, term_path, type_index_path
from solar_kb.site.render import Renderer
from solar_kb.site.terms import Term

DOWNLOADS = (
    ("kb/solar_kb.owl.ttl", "OWL ontology (Turtle)"),
    ("kb/solar_kb.context.jsonld", "JSON-LD context"),
    ("kb/solar_kb.schema.json", "JSON Schema"),
    ("kb/solar_kb.yaml", "LinkML schema (source)"),
    ("kb/records.jsonld", "All public records (JSON-LD)"),
)


@dataclass(frozen=True)
class TypeRow:
    type: str
    prefix: str
    label: str
    count: int
    href: str
    term_href: str


def _label(type_dir: str) -> str:
    """failure-modes -> Failure modes"""
    return type_dir.replace("-", " ").capitalize()


def _records_of(corpus: Corpus, type_name: str) -> list[Record]:
    return sorted((r for r in corpus.records.values() if r.type == type_name), key=lambda r: r.id)


def render_index_pages(r: Renderer, corpus: Corpus, terms: list[Term]) -> None:
    """Landing page, KB home, one index per record type, and 404.html."""
    def rows(page: str) -> list[TypeRow]:
        return [TypeRow(t, p, _label(d), len(_records_of(corpus, t)), href(page, type_index_path(p)),
                        href(page, term_path(KB + t))) for t, p, d in PUBLIC_TYPES]

    total = len(corpus.records)
    r.page("landing.html.j2", "index.html", title="Solar Lattice", types=rows("index.html"), total=total)
    downloads = [{"name": path.rsplit("/", 1)[1], "label": label, "href": href("kb/index.html", path)}
                 for path, label in DOWNLOADS]
    r.page("kb_index.html.j2", "kb/index.html", title="Knowledge base", types=rows("kb/index.html"), total=total,
           downloads=downloads)
    descriptions = {t.name: t.description for t in terms}
    for type_name, prefix, type_dir in PUBLIC_TYPES:
        page = type_index_path(prefix)
        r.page("type_index.html.j2", page, title=_label(type_dir), label=_label(type_dir), type=type_name,
               term_href=href(page, term_path(KB + type_name)), description=descriptions.get(type_name, ""),
               records=[views.record_ref(corpus, rec.id, page) for rec in _records_of(corpus, type_name)])
    r.page("404.html.j2", None, title="Not found")


def _term_ref(name: str, by_name: dict[str, Term], page: str) -> views.Ref:
    """A schema term as a link: its page when the IRI is ours, its external IRI otherwise (skos:), and plain text
    for a linkml built-in type such as string."""
    term = by_name.get(name)
    if term is None:
        return views.Ref(name)
    return views.Ref(name, href(page, term_path(term.iri)) if term.local else term.iri)


def render_term_pages(r: Renderer, corpus: Corpus, terms: list[Term], ontology_iri: str, description: str) -> None:
    """kb/schema.html (the ontology IRI) and one page per kb: term."""
    by_name = {t.name: t for t in terms}
    public = {t for t, _, _ in PUBLIC_TYPES}
    page = term_path(ontology_iri)
    sections = [(heading, [(_term_ref(t.name, by_name, page), t.description) for t in terms if t.kind == kind])
                for heading, kind in (("Classes", "class"), ("Slots", "slot"), ("Enums", "enum"))]
    r.page("schema.html.j2", page, title="Ontology", canonical=ontology_iri, description=description,
           sections=sections)
    for term in terms:
        if not term.local:
            continue
        page = term_path(term.iri)
        records = None
        if term.name in public:
            records = [views.record_ref(corpus, rec.id, page) for rec in _records_of(corpus, term.name)]
        r.page("term.html.j2", page, title=term.name, canonical=term.iri, term=term,
               parent=_term_ref(term.is_a, by_name, page) if term.is_a else None,
               range=_term_ref(term.range, by_name, page) if term.range else None,
               slots=[_term_ref(s, by_name, page) for s in term.slots], records=records)
