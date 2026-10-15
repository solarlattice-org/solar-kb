"""Record prose -> safe HTML with Obsidian links (site spec §3.2)."""
import pytest

from solar_kb.site.prose import render_prose

NAMES = {"stressor:negative-voltage-to-ground": "Negative voltage to ground", "fm:pid": "Potential-induced degradation"}


def test_wikilink_becomes_relative_link():
    out = render_prose("See [[stressors/negative-voltage-to-ground|negative voltage]].", "kb/fm/pid.html", NAMES)
    assert '<a href="../stressor/negative-voltage-to-ground">negative voltage</a>' in out


def test_wikilink_without_label_uses_the_record_name_and_drops_a_heading():
    out = render_prose("[[failure-modes/pid#Causes]]", "kb/fm/soiling.html", NAMES)
    assert '<a href="pid">Potential-induced degradation</a>' in out


def test_raw_html_is_escaped():
    out = render_prose('<script>alert(1)</script> <img src=x onerror=alert(1)>', "kb/fm/pid.html", NAMES)
    assert "<script>" not in out and "<img" not in out and "&lt;script&gt;" in out


def test_label_markup_is_escaped():
    out = render_prose("[[failure-modes/pid|<b>x</b>]]", "kb/fm/soiling.html", NAMES)
    assert "<b>" not in out and "&lt;b&gt;x&lt;/b&gt;</a>" in out


def test_javascript_links_are_not_rendered_as_links():
    assert 'href="javascript:' not in render_prose("[x](javascript:alert(1))", "kb/fm/pid.html", NAMES)


def test_wikilinks_in_code_are_left_alone():
    out = render_prose("`[[failure-modes/pid]]`\n\n    [[failure-modes/pid]]\n", "kb/fm/soiling.html", NAMES)
    assert "<a " not in out and out.count("[[failure-modes/pid]]") == 2


def test_unresolved_wikilink_raises():
    with pytest.raises(ValueError, match="does not resolve"):
        render_prose("[[failure-modes/nope]]", "kb/fm/pid.html", NAMES)
