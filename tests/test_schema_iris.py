"""Schema 0.3.0: term IRIs that cannot clash with record namespaces or with each other (site spec §2.5)."""
import rdflib

from solar_kb.export import export_all
from solar_kb.records import load_corpus
from tests.helpers import FIXTURES, SCHEMA

KB = "https://solarlattice.org/kb/"


def _owl_terms(tmp_path):
    export_all(load_corpus(FIXTURES / "mini"), SCHEMA, tmp_path)
    g = rdflib.Graph().parse(tmp_path / "solar_kb.owl.ttl", format="turtle")
    return {str(s)[len(KB):] for s in g.subjects() if str(s).startswith(KB)}


def test_owl_term_iris_follow_slot_uri(tmp_path):
    terms = _owl_terms(tmp_path)
    assert "cites_source" in terms and "src" not in terms  # kb/src/ is the Source namespace
    assert "SourceTier" in terms and "Tier" not in terms
    assert "close_mappings" not in terms and "exact_mappings" not in terms  # these are skos: terms
    assert {"FailureMode", "schema", "SourceTier#open"} <= terms


def test_no_two_term_iris_differ_only_by_case(tmp_path):
    terms = [t for t in _owl_terms(tmp_path) if "#" not in t]
    assert len({t.lower() for t in terms}) == len(terms)
