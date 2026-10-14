"""Ontology and data exports (spec §4.7): JSON Schema, OWL, JSON-LD context, JSON-LD records."""
from __future__ import annotations

import json
import warnings
from pathlib import Path

from linkml.generators.jsonldcontextgen import ContextGenerator
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.generators.owlgen import OwlSchemaGenerator

from solar_kb.records import Corpus

EXPORT_FILES = ("solar_kb.schema.json", "solar_kb.owl.ttl", "solar_kb.context.jsonld",
                "records.jsonld")


def export_all(corpus: Corpus, schema_path: Path, out_dir: Path) -> list[Path]:
    """Write the exports for the PUBLIC layer only. Returns the written paths."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    schema = str(schema_path)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        outputs = {
            "solar_kb.schema.json": JsonSchemaGenerator(schema).serialize(),
            "solar_kb.owl.ttl": OwlSchemaGenerator(
                schema,
                skip_vacuous_min_zero_cardinality_axioms=True,
                skip_vacuous_local_range_axioms=True,
                consolidate_cardinality_axioms=True,
            ).serialize(),
            "solar_kb.context.jsonld": ContextGenerator(schema).serialize(),
        }
    context = json.loads(outputs["solar_kb.context.jsonld"])["@context"]
    context["body"] = "skos:note"
    graph = [dict(r.data, body=r.body) for _, r in sorted(corpus.records.items())
             if r.layer == "public"]
    outputs["records.jsonld"] = json.dumps({"@context": context, "@graph": graph}, indent=2,
                                           sort_keys=True)
    written = []
    for name in EXPORT_FILES:
        path = out_dir / name
        path.write_text(outputs[name], encoding="utf-8")
        written.append(path)
    return written
