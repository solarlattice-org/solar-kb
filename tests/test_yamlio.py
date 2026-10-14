import pytest

from solar_kb.yamlio import FrontMatterError, load_yaml, split_front_matter


def test_yes_no_and_dates_stay_strings():
    data = load_yaml("a: yes\nb: no\nc: 2026-11-02\nd: true\ne: 1.5\nf: off")
    assert data == {"a": "yes", "b": "no", "c": "2026-11-02", "d": True, "e": 1.5, "f": "off"}


def test_split_front_matter_returns_data_and_body():
    data, body = split_front_matter("---\nid: fm:pid\n---\n\nProse here.\n")
    assert data == {"id": "fm:pid"}
    assert body == "Prose here.\n"


def test_split_front_matter_handles_crlf_and_empty_body():
    data, body = split_front_matter("---\r\nid: fm:pid\r\n---\r\n")
    assert data == {"id": "fm:pid"}
    assert body == ""


@pytest.mark.parametrize("text, message", [
    ("id: fm:pid\n", "must start"),
    ("---\nid: fm:pid\n", "no closing"),
    ("---\nid: [unclosed\n---\n", "invalid YAML"),
    ("---\n- a\n- b\n---\n", "mapping"),
    ("---\nid: fm:pid\n---trailing\n", "own line"),
])
def test_split_front_matter_rejects_malformed(text, message):
    with pytest.raises(FrontMatterError, match=message):
        split_front_matter(text)
