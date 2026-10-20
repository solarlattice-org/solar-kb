"""View models: plain data the templates print (site spec §3.4)."""
from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass

from solar_kb.codes import parse_code
from solar_kb.iri import KB, expand
from solar_kb.records import Corpus, Record
from solar_kb.site.paths import href, make_index_path, record_jsonld_path, record_path, term_path, type_index_path
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
    category: str  # "" when the record has none
    signals: tuple[tuple[str, str, str | None, str], ...]  # (point, unit, unit IRI, pattern) for Measurements
    prose: str
    manifest: tuple[tuple[str, str, str | None], ...]  # (label, value, link or None)
    groups: tuple[tuple[str, tuple[ClaimView, ...]], ...]  # (rel or attr, claims)
    referenced_by: tuple[Incoming, ...]
    cited_by: tuple[Incoming, ...]
    mappings: tuple[tuple[str, str, str], ...]  # (label, value as written, IRI)
    jsonld_href: str
    records_jsonld_href: str
    fault_code: FaultCodeView | None = None  # FaultCode records only (Plan 4d)
    referenced_by_make: tuple[tuple[str, tuple[ConceptUse, ...]], ...] = ()  # EventConcept records: codes by make


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
        category=str(data.get("category") or ""),
        signals=tuple((str(s.get("point")), str(s.get("unit") or "").partition(":")[2],
                       expand(s["unit"], prefixes) if isinstance(s.get("unit"), str) else None, str(s.get("pattern") or ""))
                      for s in data.get("signals") or [] if isinstance(s, dict)),
        prose=render_prose(record.body, page, names, proposed) if record.body.strip() else "",
        manifest=manifest, groups=tuple((h, tuple(c)) for h, c in groups.items()),
        referenced_by=_incoming_views(corpus, incoming_index.get(record.id, []), page),
        cited_by=_incoming_views(corpus, cited_index.get(record.id, []), page),
        mappings=mappings,
        jsonld_href=href(page, record_jsonld_path(record.id)),
        records_jsonld_href=href(page, "kb/records.jsonld"),
        fault_code=fault_code_view(record, corpus, incoming_index) if record.type == "FaultCode" else None,
        referenced_by_make=_referenced_by_make(corpus, record, page, incoming_index),
    )


# --- Fault codes (Plan 4d) -------------------------------------------------------------------------------------------
# axis relation -> (card label, concept id -> badge word). A concept outside the table shows its record name.
AXIS_BADGES: tuple[tuple[str, str, dict[str, str]], ...] = (
    ("has_event_class", "Class", {"ec:fault": "fault", "ec:warning": "warning", "ec:informational": "informational"}),
    ("has_production_effect", "Production", {"ec:trip": "stops", "ec:derate": "reduced",
                                             "ec:no-production-effect": "unaffected"}),
    ("has_recovery", "Clears", {"ec:auto-reset": "by itself", "ec:auto-reset-limited": "after a limited number of retries",
                                "ec:manual-reset": "after a manual reset", "ec:service-required": "needs service"}),
)
# relation -> the words that introduce its targets in the Decoded sentence, in sentence order
DECODED_LEADS = (("reports", "reports"), ("indicates", "may indicate"), ("affects", "look at"),
                 ("detected_by", "confirm with"), ("mitigated_by", "do:"))
UNIT_SYMBOLS = {"unit:PERCENT": "%", "unit:KiloW": "kW", "unit:W": "W"}
BASIS_WORDS = {"rated_power": "of rated power", "current_power": "of current power", "absolute": ""}
_BASIS = re.compile(r"^basis=(\w+)")


@dataclass(frozen=True)
class AxisBadge:
    axis: str  # "Class" | "Production" | "Clears"
    label: str  # "fault", "stops", "reduced to 50 % of rated power", "after a manual reset", "not stated"
    concept: Ref | None  # the ec: page; None when the axis is not stated
    review: str
    review_label: str
    claim_id: str


@dataclass(frozen=True)
class DecodedPart:
    lead: str
    targets: tuple[Ref, ...]


@dataclass(frozen=True)
class DifferentialTest:
    a: Ref
    b: Ref
    by: Ref | None
    note: str | None
    review: str
    review_label: str


@dataclass(frozen=True)
class DifferentialBlock:
    symptom: Ref
    failure_modes: tuple[tuple[Ref, str, str], ...]  # (failure mode, review, review label) from presents_as claims
    tests: tuple[DifferentialTest, ...]  # distinguished_from among them, one per pair


@dataclass(frozen=True)
class DefinedIn:
    source: Ref
    details: str  # "publisher · edition"
    citations: tuple[tuple[str, str], ...]  # (loc, h)
    review: str
    review_label: str
    claim_id: str


@dataclass(frozen=True)
class FaultCodeView:
    make: str
    make_name: str
    make_href: str
    fc_index_href: str
    family: str
    family_name: str
    code: str
    display_message: str
    vendor_severity: str
    page: str
    only_defined: bool  # every claim is defined_in: "The manual lists this code without further explanation."
    badges: tuple[AxisBadge, ...]
    decoded: tuple[DecodedPart, ...]
    differential: tuple[DifferentialBlock, ...]
    defined_in: tuple[DefinedIn, ...]
    same_condition: tuple[tuple[str, tuple[Ref, ...]], ...]  # (make name, codes reporting the same symptom)
    same_code: tuple[Ref, ...]  # the same make and code_key in other families


@dataclass(frozen=True)
class ConceptUse:
    """One FaultCode carrying an EventConcept, as the concept page's by-make table prints it."""
    code: Ref
    family_name: str
    display_message: str
    rel: str
    claim_id: str
    claim_href: str
    review: str
    review_label: str


@dataclass(frozen=True)
class CodeRow:
    """One row of a make page's family table. Each axis cell holds the settled value (one at most, by the validator) or,
    when the record only has a disputed pair, every contested value tagged disputed; empty when the axis is not stated."""
    code: Ref
    code_key: str
    code_from: int | None
    code_to: int | None
    display_message: str
    event_class: tuple[AxisBadge, ...]
    production: tuple[AxisBadge, ...]
    recovery: tuple[AxisBadge, ...]
    reports: tuple[Ref, ...]
    page: str


def _review(claim: dict) -> tuple[str, str]:
    review = str(claim.get("review", ""))
    return review, REVIEW_LABELS.get(review, review)


def _targets(record: Record, rel: str) -> list[str]:
    return list(dict.fromkeys(c["target"] for c in record.claims()
                              if c.get("rel") == rel and isinstance(c.get("target"), str)))


def _find_claim(record: Record | None, claim_id: str) -> dict:
    return next((c for c in (record.claims() if record else []) if c.get("claim_id") == claim_id), {})


def _decase(name: str) -> str:
    """'Low insulation resistance' -> 'low insulation resistance' for mid-sentence use; an acronym ('DC cable',
    'IV curve tracing') keeps its case."""
    first = name.split(" ", 1)[0]
    return name[0].lower() + name[1:] if len(first) > 1 and not first.isupper() else name


def _output_limit(record: Record) -> str:
    """' to 50 % of rated power' from the record's output_limit claim, or '' when there is no number."""
    for claim in record.claims():
        value = claim.get("value") if claim.get("attr") == "output_limit" else None
        if not isinstance(value, dict):
            continue
        number = next((value[k] for k in ("nominal", "max", "min") if isinstance(value.get(k), (int, float))), None)
        if number is None:
            continue
        unit = str(value.get("unit") or "")
        symbol = UNIT_SYMBOLS.get(unit, unit.partition(":")[2])
        m = _BASIS.match(str(claim.get("conditions") or ""))
        basis = BASIS_WORDS.get(m.group(1), "") if m else ""
        return f" to {_num(number)} {symbol}" + (f" {basis}" if basis else "")
    return ""


def _badge_label(corpus: Corpus, record: Record, target: str, labels: dict[str, str]) -> str:
    label = labels.get(target)
    if label is None:
        other = corpus.records.get(target)
        label = _decase(other.data["name"]) if other else target
    return label + _output_limit(record) if target == "ec:derate" else label


def _axis_badges(corpus: Corpus, record: Record, page: str) -> tuple[AxisBadge, ...]:
    out = []
    for rel, axis, labels in AXIS_BADGES:
        claims = [c for c in record.claims() if c.get("rel") == rel and isinstance(c.get("target"), str)]
        if not claims:
            out.append(AxisBadge(axis, "not stated", None, "", "", ""))
        for claim in claims:  # a disputed pair shows both values, each with its own review badge
            review, review_label = _review(claim)
            out.append(AxisBadge(axis, _badge_label(corpus, record, claim["target"], labels),
                                 record_ref(corpus, claim["target"], page), review, review_label,
                                 str(claim.get("claim_id", ""))))
    return tuple(out)


def _decoded(corpus: Corpus, record: Record, page: str) -> tuple[DecodedPart, ...]:
    parts = []
    for rel, lead in DECODED_LEADS:
        targets = _targets(record, rel)
        if targets:
            refs = []
            for target in targets:
                ref = record_ref(corpus, target, page)
                refs.append(Ref(_decase(ref.label), ref.href, ref.proposed) if target in corpus.records else ref)
            parts.append(DecodedPart(lead, tuple(refs)))
    if parts:
        parts[0] = DecodedPart(parts[0].lead[0].upper() + parts[0].lead[1:], parts[0].targets)
    return tuple(parts)


def _differential(corpus: Corpus, record: Record, page: str, incoming_index: Index) -> tuple[DifferentialBlock, ...]:
    """What `differential` would say for the reported symptom: the failure modes that present it, and the
    distinguished_from tests among them (one per pair, the first claim found), review badges inherited."""
    blocks = []
    for symptom in _targets(record, "reports"):
        modes: dict[str, tuple[str, str]] = {}
        for rid, cid, rel in incoming_index.get(symptom, []):
            other = corpus.records.get(rid)
            if rel == "presents_as" and other is not None and other.type == "FailureMode" and rid not in modes:
                modes[rid] = _review(_find_claim(other, cid))
        tests, seen = [], set()
        for a in modes:
            for claim in corpus.records[a].claims():
                b = claim.get("target")
                if claim.get("rel") == "distinguished_from" and b in modes and frozenset((a, b)) not in seen:
                    seen.add(frozenset((a, b)))
                    review, review_label = _review(claim)
                    by = claim.get("by")
                    tests.append(DifferentialTest(record_ref(corpus, a, page), record_ref(corpus, b, page),
                                                  record_ref(corpus, by, page) if isinstance(by, str) else None,
                                                  claim.get("note") if isinstance(claim.get("note"), str) else None,
                                                  review, review_label))
        blocks.append(DifferentialBlock(record_ref(corpus, symptom, page),
                                        tuple((record_ref(corpus, f, page), *review) for f, review in modes.items()),
                                        tuple(tests)))
    return tuple(blocks)


def _defined_in(corpus: Corpus, record: Record, page: str) -> tuple[DefinedIn, ...]:
    out = []
    for claim in record.claims():
        if claim.get("rel") != "defined_in" or not isinstance(claim.get("target"), str):
            continue
        source = corpus.records.get(claim["target"])
        details = " · ".join(str(source.data[k]) for k in ("publisher", "edition_or_date")
                             if source is not None and source.data.get(k) is not None)
        review, review_label = _review(claim)
        cites = claim.get("cite") if isinstance(claim.get("cite"), list) else []
        out.append(DefinedIn(record_ref(corpus, claim["target"], page), details,
                             tuple((str(c.get("loc", "")), str(c.get("h", ""))) for c in cites if isinstance(c, dict)),
                             review, review_label, str(claim.get("claim_id", ""))))
    return tuple(out)


def _same_condition(corpus: Corpus, record: Record, page: str, incoming_index: Index) -> tuple:
    by_make: dict[str, dict[str, Ref]] = {}
    for symptom in _targets(record, "reports"):
        for rid, _cid, rel in incoming_index.get(symptom, []):
            other = corpus.records.get(rid)
            if rel == "reports" and other is not None and other.type == "FaultCode" and rid != record.id:
                make_name = str(other.data.get("make_name") or other.data.get("make") or "")
                by_make.setdefault(make_name, {})[rid] = record_ref(corpus, rid, page)
    return tuple((make, tuple(refs[r] for r in sorted(refs))) for make, refs in sorted(by_make.items()))


def _same_code(corpus: Corpus, record: Record, page: str) -> tuple[Ref, ...]:
    data = record.data
    return tuple(record_ref(corpus, rid, page) for rid, other in sorted(corpus.records.items())
                 if other.type == "FaultCode" and rid != record.id and other.data.get("make") == data.get("make")
                 and other.data.get("code_key") == data.get("code_key"))


def fault_code_view(record: Record, corpus: Corpus, incoming_index: Index) -> FaultCodeView:
    """Everything the fault_code template prints beyond the generic record view: all of it from slots and claims, none
    of it drafted (Plan 4d: no prose on a FaultCode)."""
    page = record_path(record.id)
    data = record.data
    make = str(data.get("make") or "")
    rels = {c.get("rel") for c in record.claims()} | {c.get("attr") for c in record.claims() if "attr" in c}
    return FaultCodeView(
        make=make, make_name=str(data.get("make_name") or make), make_href=href(page, make_index_path(make)),
        fc_index_href=href(page, type_index_path("fc")), family=str(data.get("model_family") or ""),
        family_name=str(data.get("family_name") or ""), code=str(data.get("code") or ""),
        display_message=str(data.get("display_message") or ""), vendor_severity=str(data.get("vendor_severity") or ""),
        page=str(data.get("page") or ""), only_defined=rels <= {"defined_in"},
        badges=_axis_badges(corpus, record, page), decoded=_decoded(corpus, record, page),
        differential=_differential(corpus, record, page, incoming_index), defined_in=_defined_in(corpus, record, page),
        same_condition=_same_condition(corpus, record, page, incoming_index), same_code=_same_code(corpus, record, page),
    )


def _referenced_by_make(corpus: Corpus, record: Record, page: str, incoming_index: Index) -> tuple:
    """An EventConcept's referencing codes grouped by make: the cross-vendor answer to which codes trip, derate or
    clear by themselves. Empty for every other type (the generic Referenced by list is used)."""
    if record.type != "EventConcept":
        return ()
    groups: dict[str, list[ConceptUse]] = {}
    for rid, cid, rel in incoming_index.get(record.id, []):
        other = corpus.records.get(rid)
        if other is None or other.type != "FaultCode":
            continue
        review, review_label = _review(_find_claim(other, cid))
        groups.setdefault(str(other.data.get("make_name") or other.data.get("make") or ""), []).append(ConceptUse(
            record_ref(corpus, rid, page), str(other.data.get("family_name") or ""),
            str(other.data.get("display_message") or ""), rel, cid, href(page, record_path(rid), cid), review, review_label))
    return tuple((make, tuple(uses)) for make, uses in sorted(groups.items()))


def code_order(code_key: str) -> tuple:
    """Make-page order: vendor prefix, then number (codes without a number last), then the key."""
    parsed = parse_code(code_key)
    return (parsed.prefix, parsed.number if parsed.number is not None else float("inf"), code_key)


def _axis_cells(corpus: Corpus, record: Record, page: str) -> dict[str, tuple[AxisBadge, ...]]:
    """Per axis relation, what a make-page cell shows: the non-disputed claim when there is one, else every disputed
    claim (so a contested class is never printed as settled)."""
    out = {}
    for rel, axis, labels in AXIS_BADGES:
        claims = [c for c in record.claims() if c.get("rel") == rel and isinstance(c.get("target"), str)]
        settled = [c for c in claims if c.get("review") != "disputed"]
        cells = []
        for claim in settled[:1] or claims:
            review, review_label = _review(claim)
            ref = record_ref(corpus, claim["target"], page)
            cells.append(AxisBadge(axis, _badge_label(corpus, record, claim["target"], labels),
                                   Ref(_badge_label(corpus, record, claim["target"], labels), ref.href, ref.proposed),
                                   review, review_label, str(claim.get("claim_id", ""))))
        out[rel] = tuple(cells)
    return out


def code_rows(corpus: Corpus, records: list[Record], page: str) -> tuple[CodeRow, ...]:
    """The rows of one family's table on a make page, sorted by `code_order`."""
    rows = []
    for record in records:
        data = record.data
        concepts = _axis_cells(corpus, record, page)
        rows.append(CodeRow(
            code=Ref(str(data.get("code") or ""), href(page, record_path(record.id))),
            code_key=str(data.get("code_key") or ""),
            code_from=data.get("code_from") if isinstance(data.get("code_from"), int) else None,
            code_to=data.get("code_to") if isinstance(data.get("code_to"), int) else None,
            display_message=str(data.get("display_message") or ""),
            event_class=concepts["has_event_class"], production=concepts["has_production_effect"],
            recovery=concepts["has_recovery"],
            reports=tuple(record_ref(corpus, s, page) for s in _targets(record, "reports")),
            page=str(data.get("page") or ""),
        ))
    return tuple(sorted(rows, key=lambda row: code_order(row.code_key)))


def codes_json(corpus: Corpus) -> dict:
    """kb/fc/codes.json: {"<make>": {"<family>": {"<code_key>": {id, code, label, from, to}}}} plus display names under
    "_names" (no make slug can start with an underscore)."""
    out: dict = {}
    names: dict = {}
    for rid, record in sorted(corpus.records.items()):
        if record.type != "FaultCode":
            continue
        data = record.data
        make, family = str(data.get("make") or ""), str(data.get("model_family") or "")
        out.setdefault(make, {}).setdefault(family, {})[str(data.get("code_key") or "")] = {
            "id": rid, "code": str(data.get("code") or ""), "label": str(data.get("display_message") or ""),
            "from": data.get("code_from"), "to": data.get("code_to")}
        names.setdefault(make, {"name": str(data.get("make_name") or make), "families": {}})["families"][family] = \
            str(data.get("family_name") or family)
    out["_names"] = names
    return out
