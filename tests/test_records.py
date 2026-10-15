from solar_kb.records import load_corpus
from tests.helpers import FIXTURES, copy_fixture, rules_hit, write_record


def test_loads_public_and_overlay_layers():
    corpus = load_corpus(FIXTURES / "mini", FIXTURES / "overlay")
    assert corpus.load_errors == []
    assert corpus.records["fm:pid"].layer == "public"
    assert corpus.records["case:wo-1001"].layer == "overlay"
    assert corpus.records["fm:pid"].body.startswith("PID shunts cells")
    assert "[[stressors/negative-voltage-to-ground|" in corpus.records["fm:pid"].body


def test_missing_records_dir_is_an_empty_corpus(tmp_path):
    corpus = load_corpus(tmp_path)
    assert corpus.records == {} and corpus.load_errors == []


def test_top_level_readme_and_dotfiles_are_ignored_but_stray_files_reported(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    (root / "records" / "README.md").write_text("# layout")
    (root / "records" / "failure-modes" / ".gitkeep").write_text("")
    assert load_corpus(root).load_errors == []
    (root / "records" / "failure-modes" / "notes.txt").write_text("not a record")
    assert [v.rule for v in load_corpus(root).load_errors] == ["layout"]


def test_unknown_directory_parse_error_missing_id_and_duplicate(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    (root / "records" / "widgets").mkdir()
    (root / "records" / "failure-modes" / "broken.md").write_text("no front matter")
    write_record(root, "failure-modes", "anon", "type: FailureMode\nname: Anon")
    write_record(root, "failure-modes", "pid-copy", "id: fm:pid\ntype: FailureMode\nname: Dup")
    corpus = load_corpus(root)
    assert rules_hit(corpus.load_errors) == {"layout", "parse", "duplicate-id"}
    assert len(corpus.load_errors) == 4


def test_non_utf8_file_is_a_parse_error(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    (root / "records" / "symptoms" / "latin1.md").write_bytes(b"---\nname: caf\xe9\n---\n")
    corpus = load_corpus(root)
    assert rules_hit(corpus.load_errors) == {"parse"}
