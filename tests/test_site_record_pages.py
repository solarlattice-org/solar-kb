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
    meas = (tmp_path / "kb/meas/iv-curve-step.html").read_text()  # Measurement signals (2026-10-19)
    assert "<h2>Signals</h2>" in meas and "<code>model_160.DCA</code>" in meas
    assert '<a href="http://qudt.org/vocab/unit/A">A</a>' in meas and "one third" in meas
    assert "<h2>Signals</h2>" not in page
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


# --- Plan 4d: fault-code and event-concept pages --------------------------------------------------------------------
def test_fault_code_page_badges_decoded_differential_and_defined_in(tmp_path):
    out = _render(load_corpus(FIXTURES / "mini"), tmp_path)
    page = (out / "kb/fc/chint-sca-50-60ktl-isolationerr.html").read_text()
    assert ('<a href="./">Fault codes</a> › <a href="chint">CPS</a> › '
            '<a href="chint#sca-50-60ktl">CPS SCA50/60KTL-DO/US-480</a>') in page
    assert "<dt>Code</dt><dd><code>IsolationErr</code></dd>" in page
    assert "<dt>Shown as</dt><dd>Insulation resistance low</dd>" in page
    assert "<dt>Vendor severity</dt><dd>PROTECTION</dd>" in page and "<dt>Page</dt><dd>6</dd>" in page
    # the three axis badges, each a link to the concept with its claim's review badge; a silent axis says so
    assert '<a href="../ec/fault">fault</a> <span class="badge drafted">drafted · lead</span>' in page
    assert '<span class="label">Production</span>\n<span class="muted">not stated</span>' in page
    assert '<a href="../ec/manual-reset">after a manual reset</a>' in page
    # the deterministic Decoded sentence, built from the claims alone
    assert ('<p class="decoded">Reports <a href="../symptom/low-insulation-resistance">low insulation resistance</a>; '
            'may indicate <a href="../fm/insulation-loss">insulation loss</a>; look at <a href="../comp/dc-cable">DC cable</a>; '
            'confirm with <a href="../method/insulation-resistance-test">insulation resistance test</a>.</p>') in page
    # the derived differential: failure modes presenting the reported symptom and the test that tells them apart
    assert "What can be behind" in page and '<a href="../fm/leakage-current">Leakage current</a>' in page
    assert "told apart" not in page.split("<h2>Claims</h2>")[0] and "insulation loss measures low Riso dry" in page
    assert ('<a href="../fm/insulation-loss">Insulation loss</a> vs <a href="../fm/leakage-current">Leakage current</a>'
            ' <span class="badge drafted">drafted · lead</span></td><td><a href="../method/insulation-resistance-test">'
            'Insulation resistance test</a></td>') in page
    # defined in: source, publisher and edition, locator and hash, the fixed sentence
    assert "<h2>Defined in</h2>" in page and 'href="../src/chint-fault-manual"' in page
    assert "Chint Power Systems America · Rev 2.1" in page and "<code>tbl=8.r1</code>" in page and "page 6" in page
    assert "The manufacturer's own cause and corrective text is not reproduced here." in page
    assert "Same condition on other equipment" in page and "<dt>SMA</dt>" in page
    assert 'href="sma-stp-core1-us-3501"' in page and 'href="chint-sca-36ktl-isolationerr"' in page
    assert "Same code in other families" in page
    assert "<h2>Claims</h2>" in page and 'id="c7"' in page and "<h2>Data</h2>" in page  # the standard tail follows
    assert '<link rel="canonical" href="https://solarlattice.org/kb/fc/chint-sca-50-60ktl-isolationerr">' in page
    assert 'href="../FaultCode"' not in page  # the breadcrumb replaces the type line


def test_fault_code_page_derate_badge_and_a_code_with_only_defined_in(tmp_path):
    out = _render(load_corpus(FIXTURES / "mini"), tmp_path)
    fan = (out / "kb/fc/chint-sca-50-60ktl-extfanerr.html").read_text()
    assert '<a href="../ec/derate">reduced to 50 % of rated power</a>' in fan and '<a href="../ec/warning">warning</a>' in fan
    assert '<a href="../ec/service-required">needs service</a>' in fan
    assert "<h2>Decoded</h2>" not in fan and "Same condition" not in fan  # nothing reported, nothing to decode
    assert "<code>tbl=2.r3</code>" in fan and "<code>tbl=4.r1</code>" in fan  # both rows of the one defined_in claim
    rng = (out / "kb/fc/sma-stp-core1-us-6002-6412.html").read_text()
    assert "The manual lists this code without further explanation." in rng and 'class="axis-card"' not in rng
    assert "<dt>Code</dt><dd><code>6002-6412</code></dd>" in rng and "SMA Solar Technology AG · BA-en-13" in rng
    sma = (out / "kb/fc/sma-stp-core1-us-3501.html").read_text()
    assert "<dt>Vendor severity</dt>" not in sma and "<code>sec=h12</code>" in sma
    assert "<dt>CPS</dt><dd>" in sma and 'href="chint-sca-36ktl-isolationerr"' in sma and "Same code in other" not in sma


def test_event_concept_source_and_symptom_pages_list_the_codes(tmp_path):
    out = _render(load_corpus(FIXTURES / "mini"), tmp_path)
    concept = (out / "kb/ec/fault.html").read_text()
    assert "<h2>Referenced by</h2>" in concept and "<h3>CPS</h3>" in concept and "<h3>SMA</h3>" in concept
    assert ('<tr><td><a href="../fc/chint-sca-50-60ktl-isolationerr">CPS SCA50-60KTL IsolationErr</a></td>'
            "<td>CPS SCA50/60KTL-DO/US-480</td><td>Insulation resistance low</td><td><code>has_event_class</code> "
            '<a href="../fc/chint-sca-50-60ktl-isolationerr#c2">c2</a> <span class="badge drafted">drafted · lead</span></td></tr>') in concept
    assert concept.count("<h3>CPS</h3>") == 1 and "Reading rule" in concept  # the body's reading rule renders
    assert "<h3>" not in (out / "kb/ec/auto-reset.html").read_text().split("<h2>Data</h2>")[0]  # no codes: no table
    source = (out / "kb/src/chint-fault-manual.html").read_text()
    assert "<code>defined_in</code>" in source and 'href="../fc/chint-sca-50-60ktl-isolationerr#c1"' in source
    assert "Cited by" in source and "<dt>Edition or date</dt><dd>Rev 2.1</dd>" in source
    symptom = (out / "kb/symptom/low-insulation-resistance.html").read_text()
    assert "<code>reports</code>" in symptom and 'href="../fc/sma-stp-core1-us-3501#c2"' in symptom
