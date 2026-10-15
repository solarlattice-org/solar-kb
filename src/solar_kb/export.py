"""Ontology and data exports (spec §4.7): JSON Schema, OWL, JSON-LD context, JSON-LD records."""
from __future__ import annotations

import json
import warnings
from pathlib import Path

from linkml.generators.jsonldcontextgen import ContextGenerator
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.generators.owlgen import OwlSchemaGenerator

from solar_kb.iri import KB, expand, load_prefixes
from solar_kb.records import Corpus, Record

EXPORT_FILES = ("solar_kb.schema.json", "solar_kb.owl.ttl", "solar_kb.context.jsonld",
                "records.jsonld")
# Identifier-valued terms. They are written as absolute IRIs and typed @id, so the JSON-LD links nodes
# instead of carrying strings. Absolute values also sidestep the context's key clashes: `src` and `unit` are
# both a slot and a prefix, and a JSON-LD key can mean only one of them.
IRI_TERMS = ("target", "by", "superseded_by", "conflicts_with", "src", "unit", "close_mappings",
             "exact_mappings")


def jsonld_context(schema_path: Path) -> dict:
    """The JSON-LD context for records: linkml's generated context plus the @id coercions above."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        context = json.loads(ContextGenerator(str(schema_path)).serialize())["@context"]
    context["body"] = "skos:note"
    for term in IRI_TERMS:
        entry = context.get(term)
        entry = dict(entry) if isinstance(entry, dict) else {"@id": entry if isinstance(entry, str) else term}
        entry["@type"] = "@id"
        context[term] = entry
    return context


def _expand_claim(claim: dict, prefixes: dict[str, str]) -> dict:
    out = dict(claim)
    for key in ("target", "by", "superseded_by"):
        if isinstance(out.get(key), str):
            out[key] = expand(out[key], prefixes)
    if isinstance(out.get("conflicts_with"), list):
        out["conflicts_with"] = [expand(v, prefixes) for v in out["conflicts_with"]]
    value = out.get("value")
    if isinstance(value, dict) and isinstance(value.get("unit"), str):
        out["value"] = dict(value, unit=expand(value["unit"], prefixes))
    if isinstance(out.get("cite"), list):
        out["cite"] = [dict(c, src=expand(c["src"], prefixes)) if isinstance(c.get("src"), str) else c
                       for c in out["cite"]]
    return out


def record_node(record: Record, prefixes: dict[str, str]) -> dict:
    """One record as a JSON-LD node object whose identifiers are absolute IRIs."""
    data = dict(record.data)
    data["id"] = expand(record.id, prefixes)
    for key in ("close_mappings", "exact_mappings"):
        if isinstance(data.get(key), list):
            data[key] = [expand(v, prefixes) for v in data[key]]
    if isinstance(data.get("claims"), list):
        # Each claim is a node with its claim IRI (<record IRI>#<claim_id>), so superseded_by / conflicts_with land on it.
        data["claims"] = [dict(_expand_claim(c, prefixes), **{"@id": f"{data['id']}#{c['claim_id']}"})
                          if isinstance(c.get("claim_id"), str) else _expand_claim(c, prefixes)
                          for c in data["claims"]]
    if isinstance(data.get("signals"), list):
        data["signals"] = [dict(s, unit=expand(s["unit"], prefixes)) if isinstance(s.get("unit"), str) else s
                           for s in data["signals"]]
    # "@type" links each record to its OWL class (kb:FailureMode, ...); "type" alone is only a literal.
    return dict(data, body=record.body, **{"@type": KB + record.type})


def export_all(corpus: Corpus, schema_path: Path, out_dir: Path) -> list[Path]:
    """Write the exports for the PUBLIC layer only. Returns the written paths."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    schema = str(schema_path)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        outputs = {
            "solar_kb.schema.json": JsonSchemaGenerator(schema).serialize(),
            # use_native_uris=False makes slot_uri count, so OWL and the JSON-LD context mint the same IRIs.
            "solar_kb.owl.ttl": OwlSchemaGenerator(
                schema,
                use_native_uris=False,
                skip_vacuous_min_zero_cardinality_axioms=True,
                skip_vacuous_local_range_axioms=True,
                consolidate_cardinality_axioms=True,
            ).serialize(),
        }
    prefixes = load_prefixes(schema_path)
    context = jsonld_context(schema_path)
    outputs["solar_kb.context.jsonld"] = json.dumps({"@context": context}, indent=2, sort_keys=True)
    graph = [record_node(r, prefixes) for _, r in sorted(corpus.records.items()) if r.layer == "public"]
    outputs["records.jsonld"] = json.dumps({"@context": context, "@graph": graph}, indent=2,
                                           sort_keys=True)
    written = []
    for name in EXPORT_FILES:
        path = out_dir / name
        path.write_text(outputs[name], encoding="utf-8")
        written.append(path)
    return written
