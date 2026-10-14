"""Semantic validator rules (spec §4.5). Each rule takes a Corpus, returns Violations.

Rules must never raise on malformed records: schema errors are reported separately,
so every field access here is defensive.
"""
from __future__ import annotations

import re
from collections.abc import Callable, Iterator

from solar_kb.records import OVERLAY_ONLY_TYPES, TYPE_DIRS, Corpus, Record
from solar_kb.violation import Violation

# relation -> (allowed source types, allowed target types)
RELATION_SIGNATURES: dict[str, tuple[frozenset[str], frozenset[str]]] = {
    "caused_by": (frozenset({"FailureMode"}), frozenset({"Stressor", "FailureMode"})),
    "affects": (frozenset({"FailureMode"}), frozenset({"Component"})),
    "presents_as": (frozenset({"FailureMode"}), frozenset({"Symptom"})),
    "observed_as": (frozenset({"Symptom"}), frozenset({"Measurement"})),
    "produces": (frozenset({"DetectionMethod"}), frozenset({"Measurement"})),
    "detected_by": (frozenset({"FailureMode"}), frozenset({"DetectionMethod"})),
    "mitigated_by": (frozenset({"FailureMode"}), frozenset({"Mitigation"})),
    "leads_to": (frozenset({"FailureMode"}), frozenset({"FailureMode"})),
    "distinguished_from": (frozenset({"FailureMode"}), frozenset({"FailureMode"})),
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
            if "by" in claim and claim.get("rel") != "distinguished_from":
                out.append(_v("claim-shape", record, "'by' is only valid on distinguished_from", claim))
            if "keep" in claim and claim.get("review") != "drafted":
                out.append(_v("claim-shape", record, "'keep: drafted' requires review: drafted", claim))
            quote = claim.get("quote")
            if isinstance(quote, str) and len(quote.split()) > MAX_QUOTE_WORDS:
                out.append(_v("claim-shape", record, f"quote exceeds {MAX_QUOTE_WORDS} words", claim))
    return out


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
                if source.layer != "public" or source.data.get("tier") not in PUBLIC_CITABLE_TIERS:
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
            if isinstance(value, dict) and isinstance(value.get("min"), (int, float)) \
                    and isinstance(value.get("max"), (int, float)) and value["min"] > value["max"]:
                out.append(_v("quantities", record, "value min is greater than max", claim))
            conditions = claim.get("conditions")
            if not isinstance(conditions, str) or not conditions.strip():
                out.append(_v("quantities", record, "quantity claim needs 'conditions'", claim))
    return out


def rule_targets(corpus: Corpus) -> list[Violation]:
    """4.5.5: relation targets exist and have the right types for the relation."""
    out = []
    for record in corpus.records.values():
        for claim in record.claims():
            rel = claim.get("rel")
            if not isinstance(rel, str) or rel not in RELATION_SIGNATURES:
                continue  # schema reports unknown relations
            sources, targets = RELATION_SIGNATURES[rel]
            if record.type not in sources:
                out.append(_v("targets", record, f"{record.type} cannot have relation {rel}", claim))
            target = claim.get("target")
            target_type = _type_of(corpus, target)
            if target_type is None:
                out.append(_v("targets", record, f"target {target!r} does not exist", claim))
            elif target_type not in targets:
                out.append(_v("targets", record, f"{rel} cannot point to a {target_type}", claim))
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
                if target is None or m.group(2) not in {c.get("claim_id") for c in target.claims()}:
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
        refs: list[object] = []
        for claim in record.claims():
            refs += [claim.get("target"), claim.get("by")]
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
            type_dir, _, slug = target.strip().partition("/")
            prefix = TYPE_DIRS.get(type_dir, (None, None))[1]
            linked = corpus.records.get(f"{prefix}:{slug}") if prefix else None
            if linked is None:
                out.append(_v("body-links", record, f"wikilink [[{target}]] does not resolve; "
                                                    "use [[<type-dir>/<slug>|label]]"))
            elif record.layer == "public" and linked.layer != "public":
                out.append(_v("layers", record, f"public record links to private record {linked.id}"))
    return out


ALL_RULES: list[Rule] = [
    rule_ids, rule_claim_shape, rule_sources_exist, rule_public_citations, rule_quantities,
    rule_targets, rule_distinguished_by, rule_claim_refs, rule_layers, rule_case_links,
    rule_body_links,
]
