from pathlib import Path

from solar_kb.records import Record
from solar_kb.schema_check import SchemaChecker
from tests.helpers import SCHEMA


def _record(data: dict) -> Record:
    return Record(data=data, body="", path=Path("x.md"), layer="public", type_dir="failure-modes")


def test_valid_record_has_no_violations():
    checker = SchemaChecker(SCHEMA)
    assert checker.check(_record({"id": "fm:x", "type": "FailureMode", "name": "X"})) == []


def test_unknown_type_is_reported_without_crashing():
    checker = SchemaChecker(SCHEMA)
    [v] = checker.check(_record({"id": "fm:x", "type": "Gadget", "name": "X"}))
    assert v.rule == "schema" and "Gadget" in v.message


def test_closed_world_rejects_typo_fields_and_bad_values():
    checker = SchemaChecker(SCHEMA)
    data = {"id": "fm:x", "type": "FailureMode", "name": "X", "clams": [],
            "claims": [{"claim_id": "c1", "rel": "caused_by", "target": "stressor:y",
                        "cite": [], "review": "maybe"}]}
    messages = " | ".join(v.message for v in checker.check(_record(data)))
    assert "'clams' was unexpected" in messages
    assert "should be non-empty" in messages
    assert "'maybe' is not one of" in messages


def test_locator_grammar_is_enforced():
    checker = SchemaChecker(SCHEMA)
    good = ["sec=4.3", "p=12", "tbl=3", "tbl=3.r5", "fig=7", "t=12:40-13:30"]
    for loc in good + ["page 4", "sec=", "t=12:4-13:30", "tbl=3.5"]:
        data = {"id": "fm:x", "type": "FailureMode", "name": "X",
                "claims": [{"claim_id": "c1", "rel": "caused_by", "target": "stressor:y",
                            "cite": [{"src": "src:a", "loc": loc, "h": "a1b2c3d4e5f6"}], "review": "drafted"}]}
        assert (checker.check(_record(data)) == []) == (loc in good), loc
