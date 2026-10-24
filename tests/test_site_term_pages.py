"""The ontology page and one page per schema term (site spec §3.4)."""
from solar_kb.iri import KB
from solar_kb.records import load_corpus
from solar_kb.site.pages import render_term_pages
from solar_kb.site.render import Renderer
from solar_kb.site.terms import load_ontology
from tests.helpers import FIXTURES, SCHEMA

ONTOLOGY = load_ontology(SCHEMA)


def _render(tmp_path):
    render_term_pages(Renderer(tmp_path, "0.3.0"), load_corpus(FIXTURES / "mini"), list(ONTOLOGY.terms),
                      ONTOLOGY.iri, ONTOLOGY.description)


def test_class_page(tmp_path):
    _render(tmp_path)
    page = (tmp_path / "kb/FailureMode.html").read_text()
    assert '<link rel="canonical" href="https://solarlattice.org/kb/FailureMode">' in page
    assert '<a href="Record">Record</a>' in page and '<a href="fm/pid">Potential-induced degradation</a>' in page
    assert '<a href="http://www.w3.org/2004/02/skos/core#closeMatch">close_mappings</a>' in page


def test_enum_values_are_anchors(tmp_path):
    _render(tmp_path)
    page = (tmp_path / "kb/SourceTier.html").read_text()
    assert 'id="open"' in page and 'id="reference"' in page and 'id="private"' in page


def test_slot_page_lives_at_its_iri_and_names_its_yaml_key(tmp_path):
    _render(tmp_path)
    page = (tmp_path / "kb/cites_source.html").read_text()
    assert "the key is <code>src</code>" in page and f"<code>{KB}cites_source</code>" in page
    assert not (tmp_path / "kb/src.html").exists() and not (tmp_path / "kb/close_mappings.html").exists()
    assert '<a href="SourceTier">SourceTier</a>' in (tmp_path / "kb/tier.html").read_text()


def test_schema_page_lists_every_term(tmp_path):
    _render(tmp_path)
    page = (tmp_path / "kb/schema.html").read_text()
    assert '<link rel="canonical" href="https://solarlattice.org/kb/schema">' in page
    assert '<a href="FailureMode">FailureMode</a>' in page and '<a href="cites_source">src</a>' in page
    # +category (2026-10-17); +FaultCode/EventConcept (0.4.0); 0.5.0: +22 classes (21 types, ClaimScope), +13 enums, +41 slots
    assert sum(1 for t in ONTOLOGY.terms if t.local) == 166
