"""The dead-link checker follows GitHub Pages' resolution rules (site spec §2.2)."""
from solar_kb.site.linkcheck import broken_links, resolve


def _site(root, files):
    for path, text in files.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text)
    return root


def test_resolve_mirrors_pages(tmp_path):
    site = _site(tmp_path, {"index.html": "", "kb/index.html": "", "kb/fm/pid.html": "", "kb/x.ttl": ""})
    assert resolve(site, "kb/fm/pid") == site / "kb/fm/pid.html"
    assert resolve(site, "kb/") == site / "kb/index.html"
    assert resolve(site, "kb") == site / "kb/index.html"
    assert resolve(site, "") == site / "index.html"
    assert resolve(site, "/kb/x.ttl") == site / "kb/x.ttl"
    assert resolve(site, "kb/fm/nope") is None and resolve(site, "kb/fm/") is None


def test_broken_links_reports_dead_paths_missing_anchors_and_escapes(tmp_path):
    site = _site(tmp_path, {
        "index.html": '<a href="kb/">kb</a><a href="kb/fm/pid#c1">ok</a><a href="https://example.org/x">ext</a>',
        "kb/index.html": '<a href="../">home</a><a href="fm/pid#c9">bad anchor</a><a href="fm/nope">dead</a>',
        "kb/fm/pid.html": '<p id="c1"></p><a href="/kb/">abs</a><a href="#c1">self</a><a href="../../../up">out</a>'
                          '<link rel="stylesheet" href="../../static/style.css">',
    })
    assert sorted(broken_links(site)) == [("kb/fm/pid.html", "../../../up"),
                                          ("kb/fm/pid.html", "../../static/style.css"),
                                          ("kb/index.html", "fm/nope"), ("kb/index.html", "fm/pid#c9")]
