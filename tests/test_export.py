import json

import rdflib

from solar_kb.export import EXPORT_FILES, export_all
from solar_kb.records import load_corpus
from tests.helpers import FIXTURES, SCHEMA


def test_exports_are_written_and_parse(tmp_path):
    corpus = load_corpus(FIXTURES / "mini", FIXTURES / "overlay")
    written = export_all(corpus, SCHEMA, tmp_path)
    assert [p.name for p in written] == list(EXPORT_FILES)
    json.loads((tmp_path / "solar_kb.schema.json").read_text())
    rdflib.Graph().parse(tmp_path / "solar_kb.owl.ttl", format="turtle")
    records = json.loads((tmp_path / "records.jsonld").read_text())
    ids = {r["id"] for r in records["@graph"]}
    assert "https://solarlattice.org/kb/fm/pid" in ids
    assert not any(i.startswith("https://solarlattice.org/kb/case/")
                   or i == "https://solarlattice.org/kb/src/omnidian-work-orders" for i in ids)
    assert records["@context"]["body"] == "skos:note"


def test_records_jsonld_expands_to_rdf(tmp_path):
    export_all(load_corpus(FIXTURES / "mini"), SCHEMA, tmp_path)
    g = rdflib.Graph().parse(tmp_path / "records.jsonld", format="json-ld")
    pid = rdflib.URIRef("https://solarlattice.org/kb/fm/pid")
    assert (pid, None, None) in g
