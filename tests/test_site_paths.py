"""IRI -> file map, relative links, collisions, alias stubs, and schema terms (site spec §2, §3.4)."""
import pytest
import rdflib

from solar_kb.export import export_all
from solar_kb.iri import KB
from solar_kb.records import load_corpus
from solar_kb.site.paths import (PUBLIC_TYPES, alias_ids, codes_json_path, collisions, href, iri_to_path,
                                 make_index_path, record_jsonld_path, record_path, term_path, type_index_path)
from solar_kb.site.terms import load_ontology
from tests.helpers import FIXTURES, SCHEMA


def test_record_type_and_term_paths():
    assert record_path("fm:pid") == "kb/fm/pid.html"
    assert record_jsonld_path("fm:pid") == "kb/fm/pid.jsonld"
    assert type_index_path("fm") == "kb/fm/index.html"
    assert term_path(KB + "FailureMode") == "kb/FailureMode.html"
    assert term_path(KB + "schema") == "kb/schema.html"
    with pytest.raises(ValueError):
        term_path(KB + "fm/pid")
    assert [p for _, p, _ in PUBLIC_TYPES] == ["fm", "stressor", "symptom", "meas", "method", "mit", "comp", "fc", "ec",
                                               "src"]


def test_iri_to_path_mirrors_pages():
    assert iri_to_path(KB + "fm/pid") == ("kb/fm/pid.html", "")
    assert iri_to_path(KB + "fm/pid#c3") == ("kb/fm/pid.html", "c3")
    assert iri_to_path(KB + "SourceTier#open") == ("kb/SourceTier.html", "open")
    assert iri_to_path(KB) == ("kb/index.html", "")
    assert iri_to_path("https://solarlattice.org/") == ("index.html", "")
    assert iri_to_path(KB + "solar_kb.owl.ttl") == ("kb/solar_kb.owl.ttl", "")


def test_href_is_relative_and_extensionless():
    assert href("kb/fm/pid.html", "kb/stressor/x.html") == "../stressor/x"
    assert href("kb/fm/pid.html", "kb/fm/index.html") == "./"
    assert href("kb/index.html", "index.html") == "../"
    assert href("index.html", "kb/index.html") == "kb/"
    assert href("kb/fm/pid.html", "kb/fm/pid.html", "c3") == "pid#c3"
    assert href("kb/fm/pid.html", "kb/solar_kb.owl.ttl") == "../solar_kb.owl.ttl"


def test_collisions():
    assert collisions(["kb/fm/pid.html", "kb/FailureMode.html", "kb/fm/index.html", "kb/index.html"]) == []
    assert collisions(["kb/Tier.html", "kb/tier.html"]) == [("kb/Tier.html", "kb/tier.html")]
    assert collisions(["kb/src.html", "kb/src/index.html"]) == [("kb/src.html", "kb/src/index.html")]
    assert collisions(["kb/Stressor.html", "kb/stressor/index.html"]) == []  # Pages URLs are case-sensitive
    assert collisions(["kb/fm/pid.html", "kb/fm/pid.html"]) == [("kb/fm/pid.html", "kb/fm/pid.html")]


def test_alias_ids_takes_former_ids_of_any_record_type():
    # a cross-type merge (2026-10-19: stressor:junction-box-corrosion into fm:junction-box-failure) keeps its old address
    assert alias_ids("fm:pid", ["PID", "PID-s", "fm:old-pid", "stressor:pid", "fm:pid", "fm:Bad", "src:x", "nope:x"]) == [
        "fm:old-pid", "stressor:pid"]


def test_term_pages_cover_exactly_the_owl_kb_iris(tmp_path):
    export_all(load_corpus(FIXTURES / "mini"), SCHEMA, tmp_path)
    g = rdflib.Graph().parse(tmp_path / "solar_kb.owl.ttl", format="turtle")
    owl = {str(s) for s in g.subjects() if str(s).startswith(KB) and "#" not in str(s)}
    ontology = load_ontology(SCHEMA)
    assert {t.iri for t in ontology.terms if t.local} | {ontology.iri} == owl


def test_term_details():
    terms = {t.name: t for t in load_ontology(SCHEMA).terms}
    assert terms["src"].iri == KB + "cites_source" and terms["src"].iri_name == "cites_source"
    assert not terms["close_mappings"].local
    assert terms["FailureMode"].is_a == "Record" and "claims" in terms["FailureMode"].slots
    assert ("open", "") in terms["SourceTier"].values and terms["tier"].range == "SourceTier"


def test_no_site_paths_collide_for_the_real_schema():
    ontology = load_ontology(SCHEMA)
    paths = [term_path(t.iri) for t in ontology.terms if t.local] + [term_path(ontology.iri), "kb/index.html"]
    paths += [record_path(r) for r in load_corpus(FIXTURES / "mini").records]
    paths += [type_index_path(p) for _, p, _ in PUBLIC_TYPES]
    paths += [make_index_path(m) for m in ("chint", "sma")] + [codes_json_path()]  # Plan 4d make pages
    assert collisions(paths) == []


def test_fault_code_paths_and_former_ids():
    assert make_index_path("chint") == "kb/fc/chint.html" and codes_json_path() == "kb/fc/codes.json"
    assert href("kb/fc/chint-sca-50-60ktl-isolationerr.html", make_index_path("chint"), "sca-50-60ktl") == "chint#sca-50-60ktl"
    assert alias_ids("fc:chint-sca-50-60ktl-isolationerr",
                     ["IsolationErr", "fc:chint-sca-50-60ktl-isolation-err", "ec:alarm", "3701"]) == [
        "ec:alarm", "fc:chint-sca-50-60ktl-isolation-err"]
