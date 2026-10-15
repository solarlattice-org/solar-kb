from solar_kb.records import load_corpus
from solar_kb.validate import validate_corpus
from tests.helpers import FIXTURES, SCHEMA, copy_fixture, rules_hit, write_record


def test_fixture_corpus_is_clean():
    corpus = load_corpus(FIXTURES / "mini", FIXTURES / "overlay")
    assert validate_corpus(corpus, SCHEMA) == []


def test_reports_load_schema_and_rule_violations_together(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    (root / "records" / "symptoms" / "broken.md").write_text("nope")
    write_record(root, "failure-modes", "typo", "id: fm:typo\ntype: FailureMode\nname: T\nstatuss: active")
    write_record(root, "failure-modes", "dangling", "id: fm:dangling\ntype: FailureMode\nname: D\n"
                 "claims:\n  - claim_id: c1\n    rel: leads_to\n    target: fm:nowhere\n"
                 '    cite: [{src: "src:iea-t13-failures", loc: "sec=1", h: "a1b2c3d4e5f6"}]\n    review: drafted')
    found = rules_hit(validate_corpus(load_corpus(root), SCHEMA))
    assert {"parse", "schema", "targets"} <= found


def test_garbage_record_yields_violations_not_exceptions(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "garbage",
                 "id: fm:garbage\ntype: FailureMode\nname: [1, 2]\nclaims: 5\naliases: 3")
    violations = validate_corpus(load_corpus(root), SCHEMA)
    assert violations and all(v.record_id == "fm:garbage" for v in violations)
