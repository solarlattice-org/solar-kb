"""Record pages, Source pages, JSON-LD files, proposed stubs and alias redirects (site spec §3.4)."""
import json

from solar_kb.iri import KB, load_prefixes
from solar_kb.records import load_corpus
from solar_kb.site.jsonld import CONTEXT_URL
from solar_kb.site.pages import render_record_pages
from solar_kb.site.render import Renderer
from solar_kb.validate import validate_corpus
from tests.helpers import FIXTURES, SCHEMA, copy_fixture, write_record

PREFIXES = load_prefixes(SCHEMA)


def _render(corpus, out):
    render_record_pages(Renderer(out, "0.3.0"), corpus, PREFIXES)
    return out


def test_record_page_claims_badges_and_citations(tmp_path):
    page = (_render(load_corpus(FIXTURES / "mini"), tmp_path) / "kb/fm/pid.html").read_text()
    assert 'id="c1"' in page and 'id="c8"' in page
    assert 'class="badge verified"' in page and 'class="badge drafted"' in page
    assert '<a href="../stressor/negative-voltage-to-ground">Negative voltage to ground</a>' in page
    assert 'href="../src/nrel-pid-guide"' in page and "<code>tbl=2.r3</code>" in page and "h=a1b2c3d4e5f6" in page
    assert "10–30" in page and '<a href="http://qudt.org/vocab/unit/PERCENT">PERCENT</a>' in page
    assert "told apart by" in page and "verified by: reviewer" in page
    assert "<dt>Category</dt><dd>Modules</dd>" in page  # the category slot (2026-10-17)
    assert "<dt>Category</dt>" not in (tmp_path / "kb/method/el-imaging.html").read_text()  # absent when unset
    assert '<link rel="canonical" href="https://solarlattice.org/kb/fm/pid">' in page
    assert '<link rel="alternate" type="application/ld+json" href="pid.jsonld">' in page
    assert 'href="../FailureMode"' in page and 'href="../records.jsonld"' in page


def test_embedded_and_sidecar_jsonld_are_the_same_document(tmp_path):
    out = _render(load_corpus(FIXTURES / "mini"), tmp_path)
    doc = json.loads((out / "kb/fm/pid.jsonld").read_text())
    assert doc["id"] == KB + "fm/pid" and doc["@context"] == CONTEXT_URL
    page = (out / "kb/fm/pid.html").read_text()
    embedded = page.split('<script type="application/ld+json">', 1)[1].split("</script>", 1)[0]
    assert json.loads(embedded) == doc


def test_referenced_by_and_cited_by(tmp_path):
    out = _render(load_corpus(FIXTURES / "mini"), tmp_path)
    stressor = (out / "kb/stressor/negative-voltage-to-ground.html").read_text()
    assert "Referenced by" in stressor and 'href="../fm/pid#c1"' in stressor
    method = (out / "kb/method/el-imaging.html").read_text()
    assert "distinguished_from (by)" in method
    source = (out / "kb/src/nrel-pid-guide.html").read_text()
    assert "Cited by" in source and 'href="../fm/pid#c8"' in source and "Edition or date" not in source
    assert "<dt>Tier</dt><dd>reference</dd>" in (out / "kb/src/iea-t13-failures.html").read_text()


def test_proposed_stub_has_a_page_and_links_to_it_are_tagged(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "hotspot", "id: fm:hotspot\ntype: FailureMode\nname: Hotspot\nstatus: proposed")
    write_record(root, "failure-modes", "cell-crack",
                 "id: fm:cell-crack\ntype: FailureMode\nname: Cell crack\nclaims:\n  - claim_id: c1\n"
                 "    rel: leads_to\n    target: fm:hotspot\n"
                 '    cite: [{src: "src:iea-t13-failures", loc: "sec=4.1", h: "a1b2c3d4e5f6"}]\n    review: drafted',
                 body="Cracks can grow into a [[failure-modes/hotspot]].\n")
    corpus = load_corpus(root)
    assert validate_corpus(corpus, SCHEMA) == []
    out = _render(corpus, tmp_path / "site")
    assert "not yet reviewed" in (out / "kb/fm/hotspot.html").read_text()
    crack = (out / "kb/fm/cell-crack.html").read_text()
    assert '<a href="hotspot">Hotspot</a> <span class="badge proposed">proposed</span>' in crack
    assert crack.count('<a href="hotspot">Hotspot</a> <span class="badge proposed">proposed</span>') == 2  # claim + prose


def test_former_id_alias_gets_a_redirect_stub(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    pid = root / "records/failure-modes/pid.md"
    pid.write_text(pid.read_text().replace("aliases: [PID, PID-s]",
                                           "aliases: [PID, PID-s, 'fm:potential-induced-degradation']"))
    out = _render(load_corpus(root), tmp_path / "site")
    stub = (out / "kb/fm/potential-induced-degradation.html").read_text()
    assert '<meta http-equiv="refresh" content="0; url=pid">' in stub
    assert '<link rel="canonical" href="https://solarlattice.org/kb/fm/pid">' in stub
    assert not (out / "kb/fm/PID.html").exists()


def test_hostile_prose_and_origin_url_are_neutralised(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "sources", "evil", "id: src:evil\ntype: Source\nname: Evil <i>source</i>\ntier: open\n"
                 "tdm_ok: 'yes'\norigin_url: 'javascript:alert(1)'", body="</script><script>alert(1)</script>\n")
    page = (_render(load_corpus(root), tmp_path / "site") / "kb/src/evil.html").read_text()
    assert "<script>alert" not in page and 'href="javascript:' not in page and "<i>source</i>" not in page
    assert "<dd>javascript:alert(1)</dd>" in page


def test_record_header_shows_status(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "hotspot", "id: fm:hotspot\ntype: FailureMode\nname: Hotspot\nstatus: proposed")
    out = _render(load_corpus(root), tmp_path / "site")
    assert "<dt>Status</dt><dd>active</dd>" in (out / "kb/fm/pid.html").read_text()
    assert "<dt>Status</dt><dd>proposed</dd>" in (out / "kb/fm/hotspot.html").read_text()
