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


# --- Plan 4d: fault-code index, make pages and codes.json --------------------------------------------------------
import json  # noqa: E402
import re  # noqa: E402

from solar_kb.site.pages import render_fault_code_indexes  # noqa: E402


def test_fault_code_index_make_pages_and_codes_json(tmp_path):
    corpus = load_corpus(FIXTURES / "mini")
    r = Renderer(tmp_path, "0.4.0")
    render_index_pages(r, corpus, TERMS)
    render_fault_code_indexes(r, corpus)
    index = (tmp_path / "kb/fc/index.html").read_text()
    assert '<a href="chint">CPS</a></td><td>4</td>' in index and '<a href="sma">SMA</a></td><td>2</td>' in index
    assert '<a href="chint#sca-36ktl">CPS SCA36KTL-DO/US-480</a> (1) · <a href="chint#sca-50-60ktl">' in index
    assert '<form class="fc-lookup" data-fc-lookup data-codes="codes.json" hidden>' in index
    assert '<script src="../../static/fc-lookup.js" defer></script>' in index and 'href="../FaultCode"' in index
    make = (tmp_path / "kb/fc/chint.html").read_text()
    assert '<a href="./">Fault codes</a> › CPS' in make and "<h1>CPS fault codes</h1>" in make
    assert '<h2 id="sca-36ktl">CPS SCA36KTL-DO/US-480</h2>' in make and '<h2 id="sca-50-60ktl">' in make
    assert re.findall(r'<tr data-key="([a-z0-9-]+)"', make) == ["isolationerr", "extfanerr", "isolationerr", "protect90"]
    assert '<td><a href="chint-sca-50-60ktl-protect90">Protect0090</a></td><td>Bus over voltage</td>' in make
    assert '<a href="../ec/derate">reduced to 50 % of rated power</a>' in make
    assert '<a href="../symptom/low-insulation-resistance">Low insulation resistance</a>' in make and "<td>7</td>" in make
    sma = (tmp_path / "kb/fc/sma.html").read_text()
    assert '<tr data-key="6002-6412" data-from="6002" data-to="6412">' in sma
    assert re.findall(r'<tr data-key="([a-z0-9-]+)"', sma) == ["3501", "6002-6412"]
    codes = json.loads((tmp_path / "kb/fc/codes.json").read_text())
    assert codes["chint"]["sca-50-60ktl"]["isolationerr"] == {
        "id": "fc:chint-sca-50-60ktl-isolationerr", "code": "IsolationErr", "label": "Insulation resistance low",
        "from": None, "to": None}
    assert codes["sma"]["stp-core1-us"]["6002-6412"]["from"] == 6002 and codes["sma"]["stp-core1-us"]["6002-6412"]["to"] == 6412
    assert codes["_names"]["chint"] == {"name": "CPS", "families": {"sca-36ktl": "CPS SCA36KTL-DO/US-480",
                                                                   "sca-50-60ktl": "CPS SCA50/60KTL-DO/US-480"}}
    kb = (tmp_path / "kb/index.html").read_text()
    assert 'href="fc/codes.json"' in kb and "Fault-code lookup table" in kb
    landing = (tmp_path / "index.html").read_text()
    assert "Fault codes</span>" in landing and "Event concepts</span>" in landing


def test_fault_code_index_with_no_codes(tmp_path):
    r = Renderer(tmp_path, "0.4.0")
    render_index_pages(r, Corpus(), TERMS)
    render_fault_code_indexes(r, Corpus())
    assert "No fault codes yet." in (tmp_path / "kb/fc/index.html").read_text()
    assert json.loads((tmp_path / "kb/fc/codes.json").read_text()) == {"_names": {}}
    assert not (tmp_path / "kb/fc/chint.html").exists()
