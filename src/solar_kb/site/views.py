"""View models: plain data the templates print (site spec §3.4)."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

from solar_kb.iri import KB, expand
from solar_kb.records import Corpus, Record
from solar_kb.site.paths import href, record_jsonld_path, record_path, term_path
from solar_kb.site.prose import render_prose

REVIEW_LABELS = {"verified": "verified · fact", "drafted": "drafted · lead", "disputed": "disputed"}
MANIFEST_FIELDS = (("publisher", "Publisher"), ("edition_or_date", "Edition or date"), ("tier", "Tier"),
                   ("license", "Licence"), ("tdm_ok", "Text and data mining"), ("collection", "Collection"),
                   ("origin_url", "Origin"), ("sha256", "SHA-256"))
DETAIL_FIELDS = (("verified_by", "verified by"), ("verified_at", "verified on"), ("review_note", "review note"),
                 ("keep", "keep"), ("valid_from", "valid from"), ("valid_to", "valid to"))


@dataclass(frozen=True)
class Ref:
    """A link as a template prints it. href None = plain text; proposed adds a *proposed* tag."""
    label: str
    href: str | None = None
    proposed: bool = False


def record_ref(corpus: Corpus, rid: str, page_path: str, fragment: str = "") -> Ref:
    record = corpus.records.get(rid)
    if record is None:
        return Ref(rid + (f"#{fragment}" if fragment else ""))
    label = record.data["name"] + (f" ({fragment})" if fragment else "")
    return Ref(label, href(page_path, record_path(rid), fragment), record.data.get("status") == "proposed")


def claim_ref(corpus: Corpus, ref: str, page_path: str) -> Ref:
    """fm:pid#c3 -> a link to that claim's anchor."""
    rid, _, claim_id = ref.partition("#")
    return record_ref(corpus, rid, page_path, claim_id)


@dataclass(frozen=True)
class CitationView:
    source: Ref
    loc: str
    h: str


@dataclass(frozen=True)
class ClaimView:
    claim_id: str
    review: str
    review_label: str
    target: Ref | None
    by: Ref | None
    value: str | None
    unit: str | None
    unit_iri: str | None
    conditions: str | None
    note: str | None
    quote: str | None
    citations: tuple[CitationView, ...]
    details: tuple[tuple[str, str], ...]
    refs: tuple[tuple[str, Ref], ...]


@dataclass(frozen=True)
class Incoming:
    source: Ref
    rel: str
    claim_id: str
    claim_href: str


@dataclass(frozen=True)
class RecordView:
    id: str
    iri: str
    name: str
    type: str
    type_href: str
    status: str
    aliases: tuple[str, ...]
    prose: str
    manifest: tuple[tuple[str, str, str | None], ...]  # (label, value, link or None)
    groups: tuple[tuple[str, tuple[ClaimView, ...]], ...]  # (rel or attr, claims)
    referenced_by: tuple[Incoming, ...]
    cited_by: tuple[Incoming, ...]
    mappings: tuple[tuple[str, str, str], ...]  # (label, value as written, IRI)
    jsonld_href: str
    records_jsonld_href: str


Index = dict[str, list[tuple[str, str, str]]]  # record id -> [(from record id, claim id, relation)]


def incoming(corpus: Corpus) -> Index:
    """Who points at each record, through a claim's target or its `by` (distinguished_from)."""
    out: Index = defaultdict(list)
    for rid, record in sorted(corpus.records.items()):
        for claim in record.claims():
            cid, rel = claim.get("claim_id", ""), claim.get("rel", "")
            if isinstance(claim.get("target"), str):
                out[claim["target"]].append((rid, cid, rel))
            if isinstance(claim.get("by"), str):
                out[claim["by"]].append((rid, cid, f"{rel} (by)"))
    return out


def cited_by(corpus: Corpus) -> Index:
    """Which claims cite each Source, one entry per claim."""
    out: Index = defaultdict(list)
    for rid, record in sorted(corpus.records.items()):
        for claim in record.claims():
            cites = claim.get("cite") if isinstance(claim.get("cite"), list) else []
            for src in sorted({c.get("src") for c in cites if isinstance(c, dict) and isinstance(c.get("src"), str)}):
                out[src].append((rid, claim.get("claim_id", ""), "cites"))
    return out


def _num(x: object) -> str:
    return f"{x:g}" if isinstance(x, float) else str(x)


def format_value(value: dict) -> str:
    """{min: 10, max: 30} -> '10–30'; one bound -> '≥ 10' / '≤ 30'; nominal is appended."""
    lo, hi, nominal = value.get("min"), value.get("max"), value.get("nominal")
    parts = []
    if lo is not None and hi is not None:
        parts.append(f"{_num(lo)}–{_num(hi)}")
    elif lo is not None:
        parts.append(f"≥ {_num(lo)}")
    elif hi is not None:
        parts.append(f"≤ {_num(hi)}")
    if nominal is not None:
        parts.append(f"nominal {_num(nominal)}")
    return ", ".join(parts)


def _web_link(value: str) -> str | None:
    """Only http(s) values become links, so a javascript: origin_url renders as text."""
    return value if value.startswith(("https://", "http://")) else None


def _claim_view(corpus: Corpus, claim: dict, page: str, prefixes: dict[str, str]) -> ClaimView:
    value = claim.get("value") if isinstance(claim.get("value"), dict) else None
    unit = value.get("unit") if value and isinstance(value.get("unit"), str) else None
    refs = []
    if isinstance(claim.get("superseded_by"), str):
        refs.append(("superseded by", claim_ref(corpus, claim["superseded_by"], page)))
    for ref in claim.get("conflicts_with") or []:
        refs.append(("conflicts with", claim_ref(corpus, ref, page)))
    cites = claim.get("cite") if isinstance(claim.get("cite"), list) else []
    review = claim.get("review", "")
    return ClaimView(
        claim_id=claim["claim_id"], review=review, review_label=REVIEW_LABELS.get(review, review),
        target=record_ref(corpus, claim["target"], page) if isinstance(claim.get("target"), str) else None,
        by=record_ref(corpus, claim["by"], page) if isinstance(claim.get("by"), str) else None,
        value=format_value(value) if value else None,
        unit=unit.partition(":")[2] if unit else None,
        unit_iri=expand(unit, prefixes) if unit else None,
        conditions=claim.get("conditions"), note=claim.get("note"), quote=claim.get("quote"),
        citations=tuple(CitationView(record_ref(corpus, c["src"], page), str(c.get("loc", "")), str(c.get("h", "")))
                        for c in cites if isinstance(c, dict) and isinstance(c.get("src"), str)),
        details=tuple((label, str(claim[key])) for key, label in DETAIL_FIELDS if claim.get(key) is not None),
        refs=tuple(refs),
    )


def _incoming_views(corpus: Corpus, entries: list[tuple[str, str, str]], page: str) -> tuple[Incoming, ...]:
    return tuple(Incoming(record_ref(corpus, rid, page), rel, cid, href(page, record_path(rid), cid))
                 for rid, cid, rel in entries)


def record_view(record: Record, corpus: Corpus, prefixes: dict[str, str], incoming_index: Index,
                cited_index: Index) -> RecordView:
    page = record_path(record.id)
    data = record.data
    groups: dict[str, list[ClaimView]] = {}
    for claim in record.claims():
        heading = claim.get("rel") or claim.get("attr") or "claim"
        groups.setdefault(heading, []).append(_claim_view(corpus, claim, page, prefixes))
    names = {rid: r.data["name"] for rid, r in corpus.records.items()}
    proposed = {rid for rid, r in corpus.records.items() if r.data.get("status") == "proposed"}
    manifest = tuple((label, str(data[key]), _web_link(str(data[key])) if key == "origin_url" else None)
                     for key, label in MANIFEST_FIELDS if record.type == "Source" and data.get(key) is not None)
    mappings = tuple((label, value, expand(value, prefixes))
                     for key, label in (("exact_mappings", "exact match"), ("close_mappings", "close match"))
                     for value in data.get(key) or [] if isinstance(value, str))
    return RecordView(
        id=record.id, iri=expand(record.id, prefixes), name=data["name"], type=record.type,
        type_href=href(page, term_path(KB + record.type)), status=data.get("status", "active"),
        aliases=tuple(a for a in data.get("aliases") or [] if isinstance(a, str)),
        prose=render_prose(record.body, page, names, proposed) if record.body.strip() else "",
        manifest=manifest, groups=tuple((h, tuple(c)) for h, c in groups.items()),
        referenced_by=_incoming_views(corpus, incoming_index.get(record.id, []), page),
        cited_by=_incoming_views(corpus, cited_index.get(record.id, []), page),
        mappings=mappings,
        jsonld_href=href(page, record_jsonld_path(record.id)),
        records_jsonld_href=href(page, "kb/records.jsonld"),
    )
