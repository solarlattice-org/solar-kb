"""Which pages exist, and what each template is given (site spec §2.1, §3.4)."""
from __future__ import annotations

from dataclasses import dataclass

from solar_kb.iri import KB
from solar_kb.records import Corpus, Record
from solar_kb.site import views
from solar_kb.site.jsonld import record_document, script_json, to_json
from solar_kb.site.paths import (PUBLIC_TYPES, alias_ids, codes_json_path, href, make_index_path, record_jsonld_path,
                                 record_path, term_path, type_index_path)
from solar_kb.site.render import Renderer
from solar_kb.site.terms import Term

DOWNLOADS = (
    ("kb/solar_kb.owl.ttl", "OWL ontology (Turtle)"),
    ("kb/solar_kb.context.jsonld", "JSON-LD context"),
    ("kb/solar_kb.schema.json", "JSON Schema"),
    ("kb/solar_kb.yaml", "LinkML schema (source)"),
    ("kb/records.jsonld", "All public records (JSON-LD)"),
    (codes_json_path(), "Fault-code lookup table (JSON)"),
)
LOOKUP_SCRIPT = "static/fc-lookup.js"  # the code filter box (progressive enhancement, Plan 4d)


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


def fault_code_makes(corpus: Corpus, page: str) -> list[dict]:
    """The fc index rows: each make with its code count and its families (linked to the make page's family anchors)."""
    makes: dict[str, dict] = {}
    for record in _records_of(corpus, "FaultCode"):
        data = record.data
        make = makes.setdefault(str(data["make"]), {"make": str(data["make"]), "name": str(data["make_name"]), "count": 0,
                                                     "href": href(page, make_index_path(str(data["make"]))),
                                                     "families": {}})
        make["count"] += 1
        family = make["families"].setdefault(str(data["model_family"]), {
            "slug": str(data["model_family"]), "name": str(data["family_name"]), "count": 0,
            "href": href(page, make_index_path(str(data["make"])), str(data["model_family"]))})
        family["count"] += 1
    return [dict(m, families=sorted(m["families"].values(), key=lambda f: f["slug"])) for _, m in sorted(makes.items())]


def render_index_pages(r: Renderer, corpus: Corpus, terms: list[Term]) -> None:
    """Landing page, KB home, one index per record type (the fault-code index lists makes and families), and 404.html."""
    def rows(page: str) -> list[TypeRow]:
        return [TypeRow(t, p, _label(d), len(_records_of(corpus, t)), href(page, type_index_path(p)),
                        href(page, term_path(KB + t))) for t, p, d in PUBLIC_TYPES]

    total = len(corpus.records)
    # The landing index shows the types that have records (schema 0.5.0 has 31 public types, most still empty); the KB
    # home lists them all.
    r.page("landing.html.j2", "index.html", title="Solar Lattice", types=[t for t in rows("index.html") if t.count],
           total=total)
    downloads = [{"name": path.rsplit("/", 1)[1], "label": label, "href": href("kb/index.html", path)}
                 for path, label in DOWNLOADS]
    r.page("kb_index.html.j2", "kb/index.html", title="Knowledge base", types=rows("kb/index.html"), total=total,
           downloads=downloads)
    descriptions = {t.name: t.description for t in terms}
    for type_name, prefix, type_dir in PUBLIC_TYPES:
        page = type_index_path(prefix)
        common = dict(title=_label(type_dir), label=_label(type_dir), type=type_name,
                      term_href=href(page, term_path(KB + type_name)), description=descriptions.get(type_name, ""))
        if prefix == "fc":
            r.page("fc_index.html.j2", page, makes=fault_code_makes(corpus, page), codes_href=href(page, codes_json_path()),
                   lookup_href=href(page, LOOKUP_SCRIPT), **common)
            continue
        r.page("type_index.html.j2", page,
               records=[views.record_ref(corpus, rec.id, page) for rec in _records_of(corpus, type_name)], **common)
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
        r.page("term.html.j2", page, origin=f"term {term.name}", title=term.name, canonical=term.iri, term=term,
               parent=_term_ref(term.is_a, by_name, page) if term.is_a else None,
               range=_term_ref(term.range, by_name, page) if term.range else None,
               slots=[_term_ref(s, by_name, page) for s in term.slots], records=records)


def render_record_pages(r: Renderer, corpus: Corpus, prefixes: dict[str, str]) -> None:
    """For every record: its page (JSON-LD embedded), its .jsonld file, and a redirect stub per former id. A FaultCode
    gets the fault_code template (badges, Decoded sentence, defined-in row); every other type the generic one."""
    incoming, cited = views.incoming(corpus), views.cited_by(corpus)
    for record in sorted(corpus.records.values(), key=lambda rec: rec.id):
        page = record_path(record.id)
        doc = record_document(record, prefixes)
        r.write(record_jsonld_path(record.id), to_json(doc), origin=f"record {record.id}")
        view = views.record_view(record, corpus, prefixes, incoming, cited)
        template = "fault_code.html.j2" if record.type == "FaultCode" else "record.html.j2"
        r.page(template, page, origin=f"record {record.id}", title=view.name, canonical=view.iri, view=view, jsonld=script_json(doc))
        for old_id in alias_ids(record.id, record.data.get("aliases") or []):
            stub = record_path(old_id)
            r.page("redirect.html.j2", stub, origin=f"alias {old_id} of {record.id}", title=view.name, canonical=view.iri, target=href(stub, page),
                   old_id=old_id, new_id=record.id, name=view.name)


def render_fault_code_indexes(r: Renderer, corpus: Corpus) -> None:
    """kb/fc/<make>.html per make (one table per family, sorted by code prefix and number) and kb/fc/codes.json, the
    lookup table the filter box reads (Plan 4d). codes.json is written even with no codes: the KB home links to it."""
    by_make: dict[str, list[Record]] = {}
    for record in _records_of(corpus, "FaultCode"):
        by_make.setdefault(str(record.data["make"]), []).append(record)
    for make, records in sorted(by_make.items()):
        page = make_index_path(make)
        families: dict[str, list[Record]] = {}
        for record in records:
            families.setdefault(str(record.data["model_family"]), []).append(record)
        make_name = str(records[0].data.get("make_name") or make)
        r.page("fc_make.html.j2", page, origin=f"fault codes of {make}", title=f"{make_name} fault codes",
               make_name=make_name, fc_index_href=href(page, type_index_path("fc")), lookup_href=href(page, LOOKUP_SCRIPT),
               families=[{"slug": slug, "name": str(recs[0].data.get("family_name") or slug),
                          "rows": views.code_rows(corpus, recs, page)} for slug, recs in sorted(families.items())])
    r.write(codes_json_path(), to_json(views.codes_json(corpus)), origin="fault-code lookup table")
