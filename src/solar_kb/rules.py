"""Semantic validator rules (spec §4.5). Each rule takes a Corpus, returns Violations.

Rules must never raise on malformed records: schema errors are reported separately,
so every field access here is defensive.
"""
from __future__ import annotations

import math
import re
from collections.abc import Callable, Iterator

from solar_kb.codes import code_key, parse_code
from solar_kb.iri import expand
from solar_kb.records import OVERLAY_ONLY_TYPES, TYPE_DIRS, TYPE_PREFIX, Corpus, Record
from solar_kb.violation import Violation

ANY = "*"  # any record type
SAME = "="  # (as a target) the same type as the source
ALL_TYPES: frozenset[str] = frozenset(TYPE_PREFIX)
# The one table of relation signatures (spec A §4.2, Plan 4d, spec B §4.3): relation -> rows of (allowed source
# types, allowed target types). A claim is allowed when its (source type, target type) pair is in some row, so
# pair-specific relations stay exact: instance_of is Product -> Component, Parameter -> Parameter or GridProfile ->
# Standard, never Product -> Standard.
RELATION_TABLE: dict[str, tuple[tuple[tuple[str, ...] | str, tuple[str, ...] | str], ...]] = {
    # spec A slice A; caused_by widened in 0.5.0 (misconfiguration, firmware bugs, unsupported topologies)
    "caused_by": ((("FailureMode",), ("Stressor", "FailureMode", "Parameter", "GridProfile", "FirmwareRelease",
                                      "Architecture")),),
    "affects": ((("FailureMode", "FaultCode"), ("Component",)),),
    "presents_as": ((("FailureMode",), ("Symptom",)),),
    "observed_as": ((("Symptom",), ("Measurement",)),),
    "produces": ((("DetectionMethod",), ("Measurement",)),),
    "detected_by": ((("FailureMode", "FaultCode"), ("DetectionMethod",)),),
    "mitigated_by": ((("FailureMode", "FaultCode"), ("Mitigation",)),),
    "leads_to": ((("FailureMode",), ("FailureMode",)),),
    "distinguished_from": ((("FailureMode",), ("FailureMode",)),),
    # Plan 4d (schema 0.4.0): a FaultCode's meaning is carried by these claims, never by prose.
    "reports": ((("FaultCode",), ("Symptom",)),),
    "indicates": ((("FaultCode",), ("FailureMode",)),),
    "has_event_class": ((("FaultCode",), ("EventConcept",)),),
    "has_production_effect": ((("FaultCode",), ("EventConcept",)),),
    "has_recovery": ((("FaultCode",), ("EventConcept",)),),
    "defined_in": ((("FaultCode",), ("Source",)),),
    # spec B §4.3 (schema 0.5.0)
    "subclass_of": ((ANY, SAME),),
    "part_of": ((ANY, ANY),),
    "instance_of": ((("Product",), ("Component",)), (("Parameter",), ("Parameter",)),
                    (("GridProfile",), ("Standard",))),
    "manufactured_by": ((("Product", "FirmwareRelease", "Tool"), ("Organization",)),),
    "issued_by": ((("Standard", "Program"), ("Organization",)),),
    "adopted_in": ((("Standard",), ("Region",)),),
    "supersedes": ((("Product", "FirmwareRelease", "Standard"), SAME),),
    "applies_to": ((("FaultCode", "Parameter", "GridProfile", "Register", "Procedure", "Requirement", "Program",
                     "FirmwareRelease"), ("Product", "Region", "Architecture")),),
    "implements": ((("Product", "FirmwareRelease"), ("Function",)),),
    "lacks": ((("Product",), ("Function", "Protocol")),),
    "requires": ((("Requirement", "Function", "Procedure", "Product"),
                  ("Function", "Product", "Tool", "Role", "Protocol", "Requirement")),),
    "configures": ((("Parameter", "GridProfile"), ("Function",)),),
    "sets_value_of": ((("GridProfile", "Requirement"), ("Parameter",)),),
    "compatible_with": ((("Product", "FirmwareRelease"), ("Product", "FirmwareRelease", "Architecture")),),
    "incompatible_with": ((("Product", "FirmwareRelease"), ("Product", "FirmwareRelease", "Architecture")),),
    "certified_to": ((("Product", "FirmwareRelease"), ("Standard", "Requirement")),),
    "fixes": ((("FirmwareRelease",), ("FailureMode", "FaultCode", "Function")),),
    "introduces": ((("FirmwareRelease",), ("FailureMode", "FaultCode", "Function")),),
    "uses_protocol": ((("Product", "Tool"), ("Protocol",)),),
    "exposes": ((("Product",), ("Register",)),),
    "maps_to": ((("Register",), ("Parameter", "Measurement", "FaultCode")),),
    "indicates_state": ((("FaultCode",), ("OperatingState",)),),
    "performed_by": ((("Mitigation", "DetectionMethod"), ("Procedure",)),),
    "uses_tool": ((("Procedure", "DetectionMethod"), ("Tool",)),),
    "has_hazard": ((("Procedure", "Product", "Component", "FailureMode"), ("Hazard",)),),
    "controlled_by": ((("Hazard",), ("Mitigation", "Tool", "Procedure")),),
    "defines": ((("Standard", "Requirement"), ("Metric", "Concept", "CalculationMethod")),),
    "explains": ((("Concept",), ANY),),
    "related_to": ((("Concept",), ANY),),
}


def _expand_pairs(rows) -> frozenset[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set()
    for sources, targets in rows:
        for s in (ALL_TYPES if sources == ANY else sources):
            for t in ((s,) if targets == SAME else ALL_TYPES if targets == ANY else targets):
                pairs.add((s, t))
    return frozenset(pairs)


# relation -> every allowed (source type, target type) pair
RELATION_PAIRS: dict[str, frozenset[tuple[str, str]]] = {rel: _expand_pairs(rows) for rel, rows in RELATION_TABLE.items()}
# relation -> (allowed source types, allowed target types): the coarse view schema <= 0.4.0 callers read
RELATION_SIGNATURES: dict[str, tuple[frozenset[str], frozenset[str]]] = {
    rel: (frozenset(s for s, _ in pairs), frozenset(t for _, t in pairs)) for rel, pairs in RELATION_PAIRS.items()
}
# Relations a claim may negate (`negated: true`, spec B §4.4): an explicit negative where `lacks` does not fit.
# Not implements (use lacks), incompatible_with (use compatible_with), lacks (a double negative), nor the
# structural, vocabulary and fallback relations.
NEGATABLE = frozenset({"compatible_with", "applies_to", "requires", "certified_to", "adopted_in", "uses_protocol",
                       "caused_by", "indicates", "affects", "fixes"})
NEGATION_HINTS = {"implements": "; use lacks", "incompatible_with": "; use compatible_with",
                  "lacks": "; use implements"}
# Claim.scope slots holding record ids -> the type they must have
SCOPE_ID_TYPES = {"products": "Product", "regions": "Region", "architecture": "Architecture", "standard": "Standard"}
# Identity slots holding one record id -> the type it must have (schema 0.5.0)
REFERENCE_SLOTS = {"product": "Product", "jurisdiction": "Region", "access_level": "Role"}
# Identity slots an active record of each new type must carry (proposed stubs carry only id, type, name, status)
REQUIRED_IDENTITY: dict[str, tuple[str, ...]] = {
    "Organization": ("org_kind",), "Role": ("role_kind",), "Product": ("make", "product_level"),
    "FirmwareRelease": ("product", "version"), "Tool": ("tool_kind",), "Function": ("function_kind",),
    "Protocol": ("protocol_kind",), "Register": ("make", "address"), "Procedure": ("procedure_kind",),
    "Standard": ("standard_kind",), "Requirement": ("clause",), "Program": ("program_kind",),
    "Concept": ("concept_kind",), "GridProfile": ("make", "profile_code"),
}
PART_LEVELS = frozenset({"model", "variant"})  # Product levels that are part_of another Product (decision 4)
QUOTE_STANDARD_KIND = "standard"  # Source.source_kind of a code, standard or utility rule (spec B decision 2)
UNCAPPED_QUOTE_TYPES = frozenset({"Requirement"})  # where a quote_source quote may exceed MAX_QUOTE_WORDS
# axis relation -> the EventAxis its target must be on
AXIS_RELATIONS: dict[str, str] = {
    "has_event_class": "event_class", "has_production_effect": "production_effect", "has_recovery": "recovery",
}
PUBLIC_CITABLE_TIERS = frozenset({"open", "reference"})
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
CLAIM_REF_RE = re.compile(r"^([a-z]+:[a-z0-9-]+)#(c[0-9]+)$")
WIKILINK_RE = re.compile(r"\[\[([^\]|]*)(?:\|[^\]]*)?\]\]")
MAX_QUOTE_WORDS = 25

Rule = Callable[[Corpus], list[Violation]]


def _v(rule: str, record: Record, message: str, claim: dict | None = None) -> Violation:
    claim_id = claim.get("claim_id") if claim else None
    return Violation(
        rule, str(record.path), message, record_id=record.id,
        claim_id=claim_id if isinstance(claim_id, str) else None,
    )


def _citations(claim: dict) -> Iterator[dict]:
    cite = claim.get("cite")
    if isinstance(cite, list):
        yield from (c for c in cite if isinstance(c, dict))


def _scope_ids(claim: dict) -> list[object]:
    """Every record id in a claim's scope (products, regions, architecture, standard)."""
    scope = claim.get("scope")
    if not isinstance(scope, dict):
        return []
    out: list[object] = []
    for key in SCOPE_ID_TYPES:
        value = scope.get(key)
        out += value if isinstance(value, list) else [value] if value is not None else []
    return out


def _type_of(corpus: Corpus, rid: object) -> str | None:
    record = corpus.records.get(rid) if isinstance(rid, str) else None
    return record.type if record else None


def rule_ids(corpus: Corpus) -> list[Violation]:
    """4.5.7: ids are <prefix>:<slug>, prefix matches type, file and directory match."""
    out = []
    for record in corpus.records.values():
        rid, rtype = record.id, record.type
        expected_type, expected_prefix = TYPE_DIRS[record.type_dir]
        if rtype != expected_type:
            out.append(_v("ids", record, f"type {rtype!r} does not belong in records/{record.type_dir}/"))
        prefix, _, slug = rid.partition(":")
        if prefix != expected_prefix:
            out.append(_v("ids", record, f"id prefix must be '{expected_prefix}:'"))
        if not SLUG_RE.match(slug):
            out.append(_v("ids", record, "id slug must be lowercase words joined by '-'"))
        if record.path.stem != slug:
            out.append(_v("ids", record, f"file name must be '{slug}.md'"))
    return out


def rule_claim_shape(corpus: Corpus) -> list[Violation]:
    """Each claim is exactly one of a relation (rel+target) or a quantity (attr+value)."""
    out = []
    for record in corpus.records.values():
        seen: set[str] = set()
        for claim in record.claims():
            cid = claim.get("claim_id")
            if isinstance(cid, str):
                if cid in seen:
                    out.append(_v("claim-shape", record, f"duplicate claim_id {cid}", claim))
                seen.add(cid)
            has_rel, has_attr = "rel" in claim, "attr" in claim
            if has_rel == has_attr:
                out.append(_v("claim-shape", record, "claim needs exactly one of 'rel' or 'attr'", claim))
            if has_rel and "target" not in claim:
                out.append(_v("claim-shape", record, "relation claim needs 'target'", claim))
            if has_attr and "value" not in claim:
                out.append(_v("claim-shape", record, "quantity claim needs 'value'", claim))
            if has_rel and not has_attr and "value" in claim:
                out.append(_v("claim-shape", record, "a relation claim cannot carry a 'value'", claim))
            if has_attr and not has_rel and "target" in claim:
                out.append(_v("claim-shape", record, "a quantity claim cannot carry a 'target'", claim))
            start, end = claim.get("valid_from"), claim.get("valid_to")
            if isinstance(start, str) and isinstance(end, str) and start > end:
                out.append(_v("claim-shape", record, "valid_from is after valid_to", claim))
            if "by" in claim and claim.get("rel") != "distinguished_from":
                out.append(_v("claim-shape", record, "'by' is only valid on distinguished_from", claim))
            if "keep" in claim and claim.get("review") != "drafted":
                out.append(_v("claim-shape", record, "'keep: drafted' requires review: drafted", claim))
            if claim.get("conflicts_with") and claim.get("review") != "disputed":
                out.append(_v("claim-shape", record, "a claim with conflicts_with must be review: disputed",
                              claim))
            quote = claim.get("quote")
            if isinstance(quote, str) and len(quote.split()) > MAX_QUOTE_WORDS \
                    and not _uncapped_quote(corpus, record, claim):
                out.append(_v("claim-shape", record, f"quote exceeds {MAX_QUOTE_WORDS} words (only a quote_source quote "
                                                     "of a code or standard on a Requirement record may)", claim))
    return out


def _cites_only_standards(corpus: Corpus, claim: dict) -> bool:
    """Every citation of the claim is on a Source with source_kind standard (a code, standard or utility rule)."""
    cites = list(_citations(claim))
    return bool(cites) and all(
        (s := corpus.records.get(c.get("src")) if isinstance(c.get("src"), str) else None) is not None
        and s.type == "Source" and s.data.get("source_kind") == QUOTE_STANDARD_KIND for c in cites)


def _uncapped_quote(corpus: Corpus, record: Record, claim: dict) -> bool:
    """Spec B decision 2: a Requirement's claim may quote its clause in full, attributed by quote_source, when the
    cited source is a code or standard. Everywhere else the 25-word cap stays."""
    return record.type in UNCAPPED_QUOTE_TYPES and isinstance(claim.get("quote_source"), str) \
        and _cites_only_standards(corpus, claim)


def rule_sources_exist(corpus: Corpus) -> list[Violation]:
    """4.5.2: every citation's src is a Source record in the corpus."""
    out = []
    for record in corpus.records.values():
        for claim in record.claims():
            for cite in _citations(claim):
                src = cite.get("src")
                if _type_of(corpus, src) != "Source":
                    out.append(_v("sources-exist", record, f"unknown source {src!r}", claim))
    return out


def rule_public_citations(corpus: Corpus) -> list[Violation]:
    """4.5.3 (strict form): public records cite only public Sources of tier open/reference."""
    out = []
    for record in corpus.by_layer("public"):
        for claim in record.claims():
            for cite in _citations(claim):
                source = corpus.records.get(cite.get("src")) if isinstance(cite.get("src"), str) else None
                if source is None or source.type != "Source":
                    continue  # reported by rule_sources_exist
                tier = source.data.get("tier")
                if source.layer != "public" or not isinstance(tier, str) \
                        or tier not in PUBLIC_CITABLE_TIERS:
                    out.append(_v("public-citations", record,
                                  f"public claim cites non-public source {source.id}", claim))
    return out


def rule_quantities(corpus: Corpus) -> list[Violation]:
    """4.5.4: every number has a unit (schema enforces) and non-empty conditions."""
    out = []
    for record in corpus.records.values():
        for claim in record.claims():
            if "value" not in claim:
                continue
            value = claim.get("value")
            if isinstance(value, dict) and not any(k in value for k in ("min", "max", "nominal")):
                out.append(_v("quantities", record, "value needs min, max or nominal", claim))
            if isinstance(value, dict) and any(isinstance(value.get(k), float) and not math.isfinite(value[k])
                                               for k in ("min", "max", "nominal")):
                out.append(_v("quantities", record, "value must be a finite number (no nan/inf)", claim))
            if isinstance(value, dict) and isinstance(value.get("min"), (int, float)) \
                    and isinstance(value.get("max"), (int, float)) and value["min"] > value["max"]:
                out.append(_v("quantities", record, "value min is greater than max", claim))
            conditions = claim.get("conditions")
            if not isinstance(conditions, str) or not conditions.strip():
                out.append(_v("quantities", record, "quantity claim needs 'conditions'", claim))
    return out


def rule_targets(corpus: Corpus) -> list[Violation]:
    """4.5.5: relation targets exist, and the (source type, target type) pair is one RELATION_PAIRS allows."""
    out = []
    for record in corpus.records.values():
        for claim in record.claims():
            rel = claim.get("rel")
            if not isinstance(rel, str) or rel not in RELATION_PAIRS:
                continue  # schema reports unknown relations
            sources, _ = RELATION_SIGNATURES[rel]
            source_ok = record.type in sources
            if not source_ok:
                out.append(_v("targets", record, f"{record.type} cannot have relation {rel}", claim))
            target = claim.get("target")
            target_type = _type_of(corpus, target)
            if target_type is None:
                out.append(_v("targets", record, f"target {target!r} does not exist", claim))
            elif source_ok and (record.type, target_type) not in RELATION_PAIRS[rel]:
                allowed = sorted(t for s, t in RELATION_PAIRS[rel] if s == record.type)
                out.append(_v("targets", record, f"{rel} cannot point to a {target_type} from a {record.type} "
                                                 f"(allowed: {', '.join(allowed)})", claim))
            if target == record.id:
                out.append(_v("targets", record, "claim points to its own record", claim))
    return out


def rule_distinguished_by(corpus: Corpus) -> list[Violation]:
    """4.5.6: distinguished_from needs by: <existing DetectionMethod>."""
    out = []
    for record in corpus.records.values():
        for claim in record.claims():
            if claim.get("rel") != "distinguished_from":
                continue
            by = claim.get("by")
            if by is None:
                out.append(_v("distinguished-by", record, "distinguished_from needs 'by'", claim))
            elif _type_of(corpus, by) != "DetectionMethod":
                out.append(_v("distinguished-by", record, f"'by' {by!r} is not a DetectionMethod", claim))
    return out


def rule_claim_refs(corpus: Corpus) -> list[Violation]:
    """conflicts_with / superseded_by point at claims that exist."""
    out = []
    for record in corpus.records.values():
        for claim in record.claims():
            conflicts = claim.get("conflicts_with")
            refs = list(conflicts) if isinstance(conflicts, list) else []
            if claim.get("superseded_by"):
                refs.append(claim["superseded_by"])
            for ref in refs:
                m = CLAIM_REF_RE.match(ref) if isinstance(ref, str) else None
                if not m:
                    continue  # schema pattern reports malformed refs
                target = corpus.records.get(m.group(1))
                claim_ids = {c["claim_id"] for c in target.claims() if isinstance(c.get("claim_id"), str)} \
                    if target is not None else set()
                if m.group(2) not in claim_ids:
                    out.append(_v("claim-refs", record, f"claim reference {ref} does not exist", claim))
    return out


def rule_layers(corpus: Corpus) -> list[Violation]:
    """4.5.8: overlay-only types stay in the overlay; public never points into the overlay."""
    out = []
    for record in corpus.by_layer("public"):
        if record.type in OVERLAY_ONLY_TYPES:
            out.append(_v("layers", record, f"{record.type} records are private (overlay only)"))
        if record.type == "Source" and record.data.get("tier") == "private":
            out.append(_v("layers", record, "private-tier Source in the public repo"))
        refs: list[object] = [record.data.get(slot) for slot in REFERENCE_SLOTS]
        for claim in record.claims():
            refs += [claim.get("target"), claim.get("by")]
            refs += _scope_ids(claim)
            conflicts = claim.get("conflicts_with")
            for ref in [*(conflicts if isinstance(conflicts, list) else []), claim.get("superseded_by")]:
                m = CLAIM_REF_RE.match(ref) if isinstance(ref, str) else None
                if m:
                    refs.append(m.group(1))
        for ref in refs:
            target = corpus.records.get(ref) if isinstance(ref, str) else None
            if target is not None and target.layer != "public":
                out.append(_v("layers", record, f"public record links to private record {ref}"))
    return out


def rule_case_links(corpus: Corpus) -> list[Violation]:
    """Case.observed are Symptoms/Measurements; Case.diagnosis is a FailureMode."""
    out = []
    for record in corpus.records.values():
        if record.type != "Case":
            continue
        observed = record.data.get("observed")
        for obs in observed if isinstance(observed, list) else []:
            if _type_of(corpus, obs) not in ("Symptom", "Measurement"):
                out.append(_v("case-links", record, f"observed {obs!r} is not a Symptom/Measurement"))
        diagnosis = record.data.get("diagnosis")
        if diagnosis is not None and _type_of(corpus, diagnosis) != "FailureMode":
            out.append(_v("case-links", record, f"diagnosis {diagnosis!r} is not a FailureMode"))
    return out


def rule_body_links(corpus: Corpus) -> list[Violation]:
    """Body wikilinks are Obsidian path links [[<type-dir>/<slug>|label]] to existing records
    (vault root = records/), so the Obsidian graph view and the typed graph agree."""
    out = []
    for record in corpus.records.values():
        for target in WIKILINK_RE.findall(record.body):
            path = re.split(r"[#^]", target, maxsplit=1)[0]  # Obsidian heading/block links: [[a/b#Heading]]
            type_dir, _, slug = path.strip().partition("/")
            prefix = TYPE_DIRS.get(type_dir, (None, None))[1]
            linked = corpus.records.get(f"{prefix}:{slug}") if prefix else None
            if linked is None:
                out.append(_v("body-links", record, f"wikilink [[{target}]] does not resolve; "
                                                    "use [[<type-dir>/<slug>|label]]"))
            elif record.layer == "public" and linked.layer != "public":
                out.append(_v("layers", record, f"public record links to private record {linked.id}"))
    return out


ID_FIELDS = ("claim_id", "target", "by", "superseded_by")
CITE_FIELDS = ("src", "loc", "h")
LOC_NUMBERS = re.compile(r"^(?:p|tbl|fig)=(\d+)(?:\.r(\d+))?$")
LOC_TIME = re.compile(r"^t=(\d+):(\d\d)-(\d+):(\d\d)$")


def _bad_text(value: object) -> bool:
    return isinstance(value, str) and (value != value.strip() or "\n" in value)


def rule_field_format(corpus: Corpus) -> list[Violation]:
    """Identifier-like strings have no newlines or padding (schema patterns let a trailing newline through:
    `$` matches before it); names are not blank."""
    out = []
    for record in corpus.records.values():
        if _bad_text(record.id):
            out.append(_v("field-format", record, "id has whitespace or a newline"))
        name = record.data.get("name")
        if isinstance(name, str) and not name.strip():
            out.append(_v("field-format", record, "name is blank"))
        if any(_bad_text(record.data.get(slot)) for slot in REFERENCE_SLOTS):
            out.append(_v("field-format", record, "a record-id slot has whitespace or a newline"))
        for claim in record.claims():
            refs = [claim.get(k) for k in ID_FIELDS] + _scope_ids(claim)
            conflicts = claim.get("conflicts_with")
            refs += conflicts if isinstance(conflicts, list) else []
            value = claim.get("value")
            if isinstance(value, dict):
                refs.append(value.get("unit"))
            refs += [cite.get(k) for cite in _citations(claim) for k in CITE_FIELDS]
            if any(_bad_text(r) for r in refs):
                out.append(_v("field-format", record, "an identifier field has whitespace or a newline", claim))
    return out


def _locator_problem(loc: str) -> str | None:
    m = LOC_NUMBERS.match(loc)
    if m and (int(m.group(1)) < 1 or (m.group(2) is not None and int(m.group(2)) < 1)):
        return "page/table/figure/row numbers start at 1"
    m = LOC_TIME.match(loc)
    if m and int(m.group(1)) * 60 + int(m.group(2)) >= int(m.group(3)) * 60 + int(m.group(4)):
        return "video segment must end after it starts"
    if loc.startswith("sec=") and (".." in loc or loc.endswith(".")):
        return "section path has an empty segment"
    return None


def rule_locators(corpus: Corpus) -> list[Violation]:
    """Locators that match the grammar but cannot point at anything (p=0, t=10:00-00:05, sec=4..3)."""
    out = []
    for record in corpus.records.values():
        for claim in record.claims():
            for cite in _citations(claim):
                loc = cite.get("loc")
                problem = _locator_problem(loc) if isinstance(loc, str) else None
                if problem:
                    out.append(_v("locators", record, f"locator {loc!r}: {problem}", claim))
    return out


def rule_mapping_prefixes(corpus: Corpus, prefixes: dict[str, str]) -> list[Violation]:
    """close/exact mappings must expand to an IRI: absolute http(s), or a prefix the schema declares. The JSON-LD
    export writes them as IRIs, so an undeclared prefix would otherwise crash the build."""
    out = []
    for record in corpus.records.values():
        for key in ("close_mappings", "exact_mappings"):
            values = record.data.get(key)
            for value in values if isinstance(values, list) else []:
                if not isinstance(value, str):
                    continue
                try:
                    expand(value, prefixes)
                except ValueError:
                    out.append(_v("mapping-prefixes", record, f"{key} entry {value!r} uses an undeclared prefix; "
                                                              "use an absolute IRI or add the prefix to the schema"))
    return out


FAULT_CODE_REQUIRED = ("make", "make_name", "model_family", "family_name", "code", "code_key", "name", "category")
# The defining row, table or heading unit. A numbered section counts when the finder took it as the code's own
# heading unit (SMA eManual "6.2.1 Event 101", Enphase "5.1.2 DC Resistance Low - Power Off"); pages never do.
DEFINED_IN_LOC_RE = re.compile(r"^(tbl=\d+(\.r\d+)?|sec=h\d+|sec=\d+(\.\d+)*)$")
BASIS_RE = re.compile(r"^basis=(rated_power|current_power|absolute)\b")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
MAX_DISPLAY_MESSAGE_WORDS = 8
MAX_VENDOR_SEVERITY_WORDS = 3
MAX_CODE_NOTE_WORDS = 25
MAX_ALIAS_WORDS = MAX_DISPLAY_MESSAGE_WORDS  # display_message is the longest alias the plan allows
MAX_NAME_WORDS = 8  # "{make_name} {family_short} {code}"
CODE_FREE_TEXT = ("note", "conditions", "review_note")  # every other claim field is an id, a number or a citation
DERATE = "ec:derate"
OUTPUT_LIMIT = "output_limit"
OUTPUT_LIMIT_UNITS = frozenset({"unit:PERCENT", "unit:KiloW", "unit:W"})


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def firmware_suffix(data: dict) -> str:
    """Schema 0.5.0: the id suffix of a firmware-scoped FaultCode, so one printed code can exist once per firmware
    generation (fc:sma-stp-core1-us-3501-fw-3-12-20-r). Records without firmware scope keep their 0.4.0 ids."""
    fmin, fmax = data.get("firmware_min"), data.get("firmware_max")
    if isinstance(fmin, str) and _slug(fmin):
        return f"-fw-{_slug(fmin)}"
    if isinstance(fmax, str) and _slug(fmax):
        return f"-fw-upto-{_slug(fmax)}"
    return ""


def _version_numbers(version: object) -> tuple[int, ...] | None:
    numbers = re.findall(r"\d+", version) if isinstance(version, str) else []
    return tuple(int(n) for n in numbers) if numbers else None


def firmware_order_problem(fmin: object, fmax: object) -> str | None:
    """firmware_min must not come after firmware_max, compared by their dotted numbers (3.12.20.R -> 3, 12, 20) when
    both have numbers; vendor schemes without digits are not compared."""
    lo, hi = _version_numbers(fmin), _version_numbers(fmax)
    if lo is not None and hi is not None and lo > hi:
        return f"firmware_min {fmin!r} is after firmware_max {fmax!r}"
    return None


def _words(value: object) -> int:
    return len(value.split()) if isinstance(value, str) else 0


def _range_problem(data: dict) -> str | None:
    """code_from/code_to: present exactly when `code` is a printed range (parse_code sees a number_end, so a hyphenated
    single code such as CRIT-4 or OV-G-V is not one), integers, from < to, and equal to the printed bounds. A range
    without bounds would never be found by containment (`resolve_code`, the make page, codes.json)."""
    lo, hi, code = data.get("code_from"), data.get("code_to"), data.get("code")
    parsed = parse_code(code) if isinstance(code, str) else None
    is_range = parsed is not None and parsed.number_end is not None
    if (lo is None) != (hi is None):
        return "code_from and code_to come together (a printed range) or not at all"
    if lo is None:
        if is_range:
            return f"a printed range needs code_from and code_to ({parsed.number}, {parsed.number_end})"
        return None
    if not isinstance(lo, int) or not isinstance(hi, int) or isinstance(lo, bool) or isinstance(hi, bool):
        return "code_from and code_to are integers"
    if not is_range:
        return "code_from/code_to are only for a printed range such as 6002-6412"
    if lo >= hi:
        return "code_from must be less than code_to"
    if (lo, hi) != (parsed.number, parsed.number_end):
        return f"code_from/code_to must be the printed range bounds ({parsed.number}, {parsed.number_end})"
    return None


def rule_fault_code(corpus: Corpus) -> list[Violation]:
    """Plan 4d: a FaultCode's identity is recomputable from its slots, its only vendor text is the short display
    message and severity word (name and aliases are deterministic and capped), its body is empty, and its claims cite
    the manual row, carry no quote and no free text beyond a 25-word note, conditions or review_note."""
    out = []
    for record in corpus.records.values():
        if record.type != "FaultCode":
            continue
        data = record.data
        missing = [k for k in FAULT_CODE_REQUIRED if not isinstance(data.get(k), str) or not data[k].strip()]
        if missing:
            out.append(_v("fault-code", record, f"missing required slot(s): {', '.join(missing)}"))
        make, family, key, code = data.get("make"), data.get("model_family"), data.get("code_key"), data.get("code")
        if all(isinstance(x, str) for x in (make, family, key)):
            expected = f"fc:{make}-{family}-{key}{firmware_suffix(data)}"
            if record.id != expected:
                out.append(_v("fault-code", record, f"id must be {expected} (fc:<make>-<model_family>-<code_key>, "
                                                    "plus -fw-<firmware_min> or -fw-upto-<firmware_max> when firmware-scoped)"))
        problem = firmware_order_problem(data.get("firmware_min"), data.get("firmware_max"))
        if problem:
            out.append(_v("fault-code", record, problem))
        if isinstance(code, str) and isinstance(key, str) and code_key(code) != key:
            out.append(_v("fault-code", record, f"code_key must be {code_key(code)!r} for code {code!r}"))
        # The public vendor text is exactly the code, display_message and vendor_severity: name and aliases are
        # deterministic, so a sentence placed in either is a leak the word caps catch.
        name, make_name = data.get("name"), data.get("make_name")
        if isinstance(name, str) and isinstance(make_name, str) and isinstance(code, str) and name.strip() \
                and not (name.startswith(make_name + " ") and name.endswith(" " + code)):
            out.append(_v("fault-code", record, f"name is '{make_name} <family short name> {code}' (deterministic)"))
        if _words(name) > MAX_NAME_WORDS:
            out.append(_v("fault-code", record, f"name exceeds {MAX_NAME_WORDS} words"))
        aliases = data.get("aliases")
        for alias in aliases if isinstance(aliases, list) else []:
            if _words(alias) > MAX_ALIAS_WORDS:
                out.append(_v("fault-code", record, f"alias {alias[:40]!r}... exceeds {MAX_ALIAS_WORDS} words; aliases are "
                                                    "the code, code_key, make_name + code and display_message"))
        problem = _range_problem(data)
        if problem:
            out.append(_v("fault-code", record, problem))
        if _words(data.get("display_message")) > MAX_DISPLAY_MESSAGE_WORDS:
            out.append(_v("fault-code", record, f"display_message exceeds {MAX_DISPLAY_MESSAGE_WORDS} words"))
        if _words(data.get("vendor_severity")) > MAX_VENDOR_SEVERITY_WORDS:
            out.append(_v("fault-code", record, f"vendor_severity exceeds {MAX_VENDOR_SEVERITY_WORDS} words"))
        if HTML_COMMENT_RE.sub("", record.body).strip():
            out.append(_v("fault-code", record, "a FaultCode has no body; only an HTML comment is allowed"))
        axes: dict[str, int] = {}
        defined_in, derate, quantities = 0, False, []
        defining_sources: set[object] = set()
        for claim in record.claims():
            rel = claim.get("rel")
            if "quote" in claim:
                out.append(_v("fault-code", record, "quote is forbidden on a FaultCode claim", claim))
            for field_name in CODE_FREE_TEXT:
                if _words(claim.get(field_name)) > MAX_CODE_NOTE_WORDS:
                    out.append(_v("fault-code", record, f"{field_name} exceeds {MAX_CODE_NOTE_WORDS} words", claim))
            if rel == "defined_in":
                defined_in += 1
                target = claim.get("target")
                if target in defining_sources:
                    out.append(_v("fault-code", record, f"one defined_in claim per source: {target} appears twice (several "
                                                        "rows of one manual are several citations on one claim)", claim))
                defining_sources.add(target)
                for cite in _citations(claim):
                    loc = cite.get("loc")
                    if isinstance(loc, str) and not DEFINED_IN_LOC_RE.match(loc):
                        out.append(_v("fault-code", record, f"defined_in cites the defining row (tbl=N.rM), table (tbl=N) "
                                                            f"or heading unit (sec=hK or a numbered sec=N.M), not {loc!r}", claim))
                    if cite.get("src") != target:
                        out.append(_v("fault-code", record, f"defined_in cites the row of its own target {target}, not "
                                                            f"{cite.get('src')!r}", claim))
            if rel in AXIS_RELATIONS and claim.get("review") != "disputed":
                axes[rel] = axes.get(rel, 0) + 1
            if rel == "has_production_effect" and claim.get("target") == DERATE:
                derate = True
            if "attr" in claim:
                if claim.get("attr") != OUTPUT_LIMIT:
                    out.append(_v("fault-code", record, f"the only quantity on a FaultCode is {OUTPUT_LIMIT}", claim))
                    continue
                quantities.append(claim)
                conditions = claim.get("conditions")
                if not isinstance(conditions, str) or not BASIS_RE.match(conditions):
                    out.append(_v("fault-code", record, "output_limit conditions must start with basis=rated_power, "
                                                        "basis=current_power or basis=absolute", claim))
                value = claim.get("value")
                if isinstance(value, dict):  # rule_quantities reports the shape otherwise
                    if value.get("unit") not in OUTPUT_LIMIT_UNITS:
                        out.append(_v("fault-code", record, f"output_limit unit is one of {', '.join(sorted(OUTPUT_LIMIT_UNITS))}, "
                                                            f"not {value.get('unit')!r}", claim))
                    if "min" in value or not any(k in value for k in ("nominal", "max")):
                        out.append(_v("fault-code", record, "output_limit is a single reduced output: nominal or max, "
                                                            "never min", claim))
        if defined_in == 0:
            out.append(_v("fault-code", record, "needs at least one defined_in claim citing the manual row"))
        for rel, n in axes.items():
            if n > 1:
                out.append(_v("fault-code", record, f"at most one non-disputed {rel} claim per record; a second value "
                                                    "on the same axis is a disputed pair (conflicts_with)"))
        if not derate:
            for claim in quantities:
                out.append(_v("fault-code", record, f"{OUTPUT_LIMIT} needs a has_production_effect -> {DERATE} claim",
                              claim))
    return out


def rule_event_axes(corpus: Corpus) -> list[Violation]:
    """Plan 4d: has_event_class / has_production_effect / has_recovery point at an EventConcept on that axis, and an
    EventConcept carries no claims (it is vocabulary, not knowledge)."""
    out = []
    for record in corpus.records.values():
        if record.type == "EventConcept" and record.data.get("claims"):
            out.append(_v("event-axes", record, "an EventConcept carries no claims"))
        for claim in record.claims():
            rel = claim.get("rel")
            axis = AXIS_RELATIONS.get(rel) if isinstance(rel, str) else None
            target = corpus.records.get(claim.get("target")) if isinstance(claim.get("target"), str) else None
            if axis is None or target is None or target.type != "EventConcept":
                continue  # rule_targets reports a missing or mistyped target
            if target.data.get("axis") != axis:
                out.append(_v("event-axes", record, f"{rel} must point at an EventConcept on the {axis} axis; "
                                                    f"{target.id} is on {target.data.get('axis')!r}", claim))
    return out


# --- Schema 0.5.0 (spec B §4.4, §6 item 6, decision 2) ------------------------------------------------------------

def rule_scope(corpus: Corpus) -> list[Violation]:
    """Claim.scope: every id exists (a proposed stub counts) and has the type its slot names; firmware and dates are
    ordered; an empty scope is omitted."""
    out = []
    for record in corpus.records.values():
        for claim in record.claims():
            scope = claim.get("scope")
            if scope is None:
                continue
            if not isinstance(scope, dict) or not scope:
                out.append(_v("scope", record, "scope is empty; omit it", claim))
                continue
            for key, expected in SCOPE_ID_TYPES.items():
                value = scope.get(key)
                for rid in value if isinstance(value, list) else [value] if value is not None else []:
                    rtype = _type_of(corpus, rid)
                    if rtype is None:
                        out.append(_v("scope", record, f"scope.{key} {rid!r} does not exist", claim))
                    elif rtype != expected:
                        out.append(_v("scope", record, f"scope.{key} {rid!r} is a {rtype}, not a {expected}", claim))
            problem = firmware_order_problem(scope.get("firmware_min"), scope.get("firmware_max"))
            if problem:
                out.append(_v("scope", record, f"scope: {problem}", claim))
            start, end = scope.get("valid_from"), scope.get("valid_to")
            if start is not None and end is not None and str(start) > str(end):
                out.append(_v("scope", record, "scope.valid_from is after scope.valid_to", claim))
    return out


def _claim_key(claim: dict) -> str:
    """Relation, target and scope of a claim, as a hashable key (garbage shapes included)."""
    scope = claim.get("scope")
    scope_key = sorted((str(k), sorted(map(str, v)) if isinstance(v, list) else str(v)) for k, v in scope.items()) \
        if isinstance(scope, dict) else ""
    return repr((claim.get("rel"), claim.get("target"), scope_key))


def rule_negated(corpus: Corpus) -> list[Violation]:
    """negated: true only on a relation claim whose relation is NEGATABLE, and never against a non-disputed positive
    claim of the same relation, target and scope in the same record (that is a contradiction, not a condition).
    That the cited passage states the negative is checked by the compiler's support gate, which reads the evidence."""
    out = []
    for record in corpus.records.values():
        asserted: dict[str, set[bool]] = {}
        for claim in record.claims():
            if "negated" not in claim:
                if "rel" in claim and claim.get("review") != "disputed":
                    asserted.setdefault(_claim_key(claim), set()).add(False)
                continue
            rel = claim.get("rel")
            if claim.get("negated") is not True:
                out.append(_v("negated", record, "write negated only as true; omit it otherwise", claim))
                continue
            if "rel" not in claim:
                out.append(_v("negated", record, "negated applies to relation claims only", claim))
            elif not isinstance(rel, str) or rel not in NEGATABLE:
                hint = NEGATION_HINTS.get(rel, "") if isinstance(rel, str) else ""
                out.append(_v("negated", record, f"{rel} cannot be negated{hint} "
                                                 f"(negatable: {', '.join(sorted(NEGATABLE))})", claim))
            elif claim.get("review") != "disputed":
                asserted.setdefault(_claim_key(claim), set()).add(True)
        for claim in record.claims():
            key = _claim_key(claim)
            if claim.get("negated") is True and claim.get("review") != "disputed" and asserted.get(key) == {True, False}:
                out.append(_v("negated", record, f"{claim.get('rel')} {claim.get('target')} is both asserted and negated "
                                                 "under the same scope; scope one of them or mark the pair disputed", claim))
    return out


def rule_quote_source(corpus: Corpus) -> list[Violation]:
    """Spec B decision 2: quote_source attributes a verbatim code or standard quote, so it needs a quote and every
    citation on a Source with source_kind standard. (rule_claim_shape lifts the 25-word cap for such a quote on a
    Requirement record.)"""
    out = []
    for record in corpus.records.values():
        for claim in record.claims():
            if "quote_source" not in claim:
                continue
            attribution = claim.get("quote_source")
            if not isinstance(attribution, str) or not attribution.strip():
                out.append(_v("quote-source", record, "quote_source is blank", claim))
            if not isinstance(claim.get("quote"), str):
                out.append(_v("quote-source", record, "quote_source needs a quote", claim))
            if not _cites_only_standards(corpus, claim):
                others = sorted({str(c.get("src")) for c in _citations(claim)
                                 if _type_of(corpus, c.get("src")) != "Source"
                                 or corpus.records[c["src"]].data.get("source_kind") != QUOTE_STANDARD_KIND})
                out.append(_v("quote-source", record, "quote_source is only for quotes of a code or standard: every "
                                                      f"cited source needs source_kind {QUOTE_STANDARD_KIND} "
                                                      f"({', '.join(others) or 'no citation'})", claim))
    return out


def rule_identity(corpus: Corpus) -> list[Violation]:
    """Schema 0.5.0 identity slots: an active record carries its type's REQUIRED_IDENTITY slots; product, jurisdiction
    and access_level name a Product, Region and Role; `make` on a new type names an Organization org:<make> (FaultCode is
    exempt until B2 links its makes); an active Requirement is part_of a Standard and an active model or variant Product
    has a model_number and is part_of a Product."""
    out = []
    for record in corpus.records.values():
        data, active = record.data, record.data.get("status") != "proposed"
        if active:
            missing = [s for s in REQUIRED_IDENTITY.get(record.type or "", ()) if data.get(s) in (None, "")]
            if missing:
                out.append(_v("identity", record, f"an active {record.type} needs {', '.join(missing)}"))
        for slot, expected in REFERENCE_SLOTS.items():
            value = data.get(slot)
            if value is None:
                continue
            rtype = _type_of(corpus, value)
            if rtype != expected:
                out.append(_v("identity", record, f"{slot} {value!r} is "
                                                  f"{'missing' if rtype is None else 'a ' + rtype}, not a {expected}"))
        make = data.get("make")
        if isinstance(make, str) and record.type != "FaultCode" and _type_of(corpus, f"org:{make}") != "Organization":
            out.append(_v("identity", record, f"make {make!r} needs the Organization org:{make} (a proposed stub is enough)"))
        part_of = {_type_of(corpus, c.get("target")) for c in record.claims()
                   if c.get("rel") == "part_of" and c.get("review") != "disputed"}
        if active and record.type == "Requirement" and "Standard" not in part_of:
            out.append(_v("identity", record, "an active Requirement is part_of its Standard"))
        if active and record.type == "Product" and str(data.get("product_level")) in PART_LEVELS:
            if not data.get("model_number"):
                out.append(_v("identity", record, f"an active {data['product_level']} Product needs model_number"))
            if "Product" not in part_of:
                out.append(_v("identity", record, f"an active {data['product_level']} Product is part_of its family "
                                                  "(or model) Product"))
    return out


ALL_RULES: list[Rule] = [
    rule_ids, rule_claim_shape, rule_sources_exist, rule_public_citations, rule_quantities,
    rule_targets, rule_distinguished_by, rule_claim_refs, rule_layers, rule_case_links,
    rule_body_links, rule_field_format, rule_locators, rule_fault_code, rule_event_axes,
    rule_scope, rule_negated, rule_quote_source, rule_identity,
]


# --- Lint: findings that are reported as warnings and never fail validation ------------------------------------------

LOW_INFORMATION = frozenset({"related_to"})


def lint_related_to(corpus: Corpus) -> list[Violation]:
    """related_to is the low-information fallback (spec B §4.3): every use is reported, with the typed relations the
    schema allows for that (source type, target type) pair."""
    out = []
    for record in corpus.records.values():
        for claim in record.claims():
            if not isinstance(claim.get("rel"), str) or claim["rel"] not in LOW_INFORMATION:
                continue
            target_type = _type_of(corpus, claim.get("target"))
            typed = sorted(rel for rel, pairs in RELATION_PAIRS.items()
                           if rel not in LOW_INFORMATION and (record.type, target_type) in pairs)
            hint = f"; a typed relation fits: {', '.join(typed)}" if typed else ""
            out.append(_v("lint-related-to", record, f"related_to is the low-information fallback{hint}", claim))
    return out


LINT_RULES: list[Rule] = [lint_related_to]


def lint_corpus(corpus: Corpus) -> list[Violation]:
    """Warnings: reported by `solar-kb validate`, never a failure."""
    return [w for rule in LINT_RULES for w in rule(corpus)]
