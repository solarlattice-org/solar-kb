"""JSON-LD identifiers are absolute IRIs typed @id, and mappings must expand (site spec §3.3)."""
import json

import pytest
import rdflib

from solar_kb.export import export_all
from solar_kb.iri import KB, expand, load_prefixes
from solar_kb.records import load_corpus
from solar_kb.validate import validate_corpus
from tests.helpers import FIXTURES, SCHEMA, copy_fixture, write_record

PREFIXES = load_prefixes(SCHEMA)


def _records_graph(tmp_path):
    export_all(load_corpus(FIXTURES / "mini"), SCHEMA, tmp_path)
    return rdflib.Graph().parse(tmp_path / "records.jsonld", format="json-ld")


def test_expand():
    assert expand("fm:pid", PREFIXES) == KB + "fm/pid"
    assert expand("fm:pid#c3", PREFIXES) == KB + "fm/pid#c3"
    assert expand("unit:PERCENT", PREFIXES) == "http://qudt.org/vocab/unit/PERCENT"
    assert expand("https://example.org/x", PREFIXES) == "https://example.org/x"
    with pytest.raises(ValueError, match="undeclared prefix"):
        expand("mds:Module", PREFIXES)


def test_source_records_get_their_kb_iri(tmp_path):
    subjects = {str(s) for s in _records_graph(tmp_path).subjects() if isinstance(s, rdflib.URIRef)}
    assert KB + "src/iea-t13-failures" in subjects
    assert not any(s.startswith(("src:", "unit:")) for s in subjects)


def test_targets_citations_and_units_are_iri_nodes(tmp_path):
    g = _records_graph(tmp_path)
    targets = set(g.objects(None, rdflib.URIRef(KB + "target")))
    assert rdflib.URIRef(KB + "stressor/negative-voltage-to-ground") in targets
    assert all(isinstance(t, rdflib.URIRef) for t in targets)
    assert rdflib.URIRef(KB + "src/nrel-pid-guide") in set(g.objects(None, rdflib.URIRef(KB + "cites_source")))
    assert rdflib.URIRef(KB + "method/el-imaging") in set(g.objects(None, rdflib.URIRef(KB + "by")))
    assert rdflib.URIRef("http://qudt.org/vocab/unit/PERCENT") in set(g.objects(None, rdflib.URIRef(KB + "unit")))


def test_published_context_is_the_records_context(tmp_path):
    export_all(load_corpus(FIXTURES / "mini"), SCHEMA, tmp_path)
    published = json.loads((tmp_path / "solar_kb.context.jsonld").read_text())["@context"]
    assert published == json.loads((tmp_path / "records.jsonld").read_text())["@context"]
    assert published["target"]["@type"] == "@id" and published["src"]["@id"] == "cites_source"


def test_mapping_with_undeclared_prefix_is_a_violation(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "components", "inverter", "id: comp:inverter\ntype: Component\nname: Inverter\n"
                 "close_mappings: ['mds:Inverter', 'https://example.org/onto/Inverter', 'skos:Concept']")
    hits = [v for v in validate_corpus(load_corpus(root), SCHEMA) if v.rule == "mapping-prefixes"]
    assert len(hits) == 1 and "mds:Inverter" in hits[0].message


def test_claims_are_nodes_that_claim_references_point_at(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "pid-variant", "id: fm:pid-variant\ntype: FailureMode\nname: PID variant\n"
                 "claims:\n  - claim_id: c1\n    attr: typical_power_loss\n"
                 "    value: {min: 5, max: 15, unit: 'unit:PERCENT'}\n    conditions: n-type modules\n"
                 "    conflicts_with: ['fm:pid#c8']\n    superseded_by: 'fm:pid#c8'\n"
                 '    cite: [{src: "src:nrel-pid-guide", loc: "p=3", h: "a1b2c3d4e5f6"}]\n    review: disputed')
    corpus = load_corpus(root)
    assert validate_corpus(corpus, SCHEMA) == []
    export_all(corpus, SCHEMA, tmp_path / "out")
    g = rdflib.Graph().parse(tmp_path / "out" / "records.jsonld", format="json-ld")
    c8 = rdflib.URIRef(KB + "fm/pid#c8")
    assert (rdflib.URIRef(KB + "fm/pid"), rdflib.URIRef(KB + "claims"), c8) in g
    assert str(g.value(c8, rdflib.URIRef(KB + "claim_id"))) == "c8"
    for pred in ("conflicts_with", "superseded_by"):
        assert set(g.objects(None, rdflib.URIRef(KB + pred))) == {c8}
