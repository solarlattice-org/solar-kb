"""Landing page, KB home, type indexes and 404 (site spec §3.4)."""
from solar_kb.records import Corpus, load_corpus
from solar_kb.site.pages import render_index_pages
from solar_kb.site.render import Renderer
from solar_kb.site.terms import load_ontology
from tests.helpers import FIXTURES, SCHEMA

TERMS = list(load_ontology(SCHEMA).terms)


def test_landing_kb_home_and_type_index(tmp_path):
    render_index_pages(Renderer(tmp_path, "0.3.0"), load_corpus(FIXTURES / "mini"), TERMS)
    landing = (tmp_path / "index.html").read_text()
    assert 'href="kb/"' in landing and 'href="static/style.css"' in landing
    assert 'class="atlas-intro"' in landing and 'class="index-list"' in landing
    assert 'class="signal-halo"' in landing and 'class="signal"' in landing
    assert "Failure modes</span><span class=\"index-arrow\"" in landing
    kb = (tmp_path / "kb/index.html").read_text()
    assert 'href="fm/"' in kb and 'href="solar_kb.owl.ttl"' in kb and "Schema version 0.3.0" in kb
    fm = (tmp_path / "kb/fm/index.html").read_text()
    assert '<a href="pid">Potential-induced degradation</a>' in fm and 'href="../FailureMode"' in fm
    assert "What went wrong." in fm


def test_empty_corpus_says_no_records_yet(tmp_path):
    render_index_pages(Renderer(tmp_path, "0.3.0"), Corpus(), TERMS)
    assert "No records have been published yet" in (tmp_path / "index.html").read_text()
    assert "No records have been published yet" in (tmp_path / "kb/index.html").read_text()
    assert "No failure modes yet." in (tmp_path / "kb/fm/index.html").read_text()


def test_404_uses_root_absolute_links(tmp_path):
    render_index_pages(Renderer(tmp_path, "0.3.0"), Corpus(), TERMS)
    page = (tmp_path / "404.html").read_text()
    assert 'href="/static/style.css"' in page and 'href="/kb/"' in page and 'href="/"' in page
