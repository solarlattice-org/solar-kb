"""Plan 1.1: citation content hash `h` and the deferred minor findings from Plan 1's final review."""
from pathlib import Path

import pytest

from solar_kb.records import Record
from solar_kb.schema_check import SchemaChecker
from tests.helpers import SCHEMA

H = "a1b2c3d4e5f6"


def _fm(cite: dict) -> Record:
    data = {"id": "fm:x", "type": "FailureMode", "name": "X",
            "claims": [{"claim_id": "c1", "rel": "caused_by", "target": "stressor:y", "cite": [cite],
                        "review": "drafted"}]}
    return Record(data=data, body="", path=Path("x.md"), layer="public", type_dir="failure-modes")


# 1. citations carry the cited unit's content hash
@pytest.mark.parametrize("cite, ok", [
    ({"src": "src:a", "loc": "sec=1", "h": H}, True),
    ({"src": "src:a", "loc": "sec=1"}, False),
    ({"src": "src:a", "loc": "sec=1", "h": "A1B2C3D4E5F6"}, False),
    ({"src": "src:a", "loc": "sec=1", "h": "a1b2c3"}, False),
])
def test_citation_requires_a_12_hex_hash(cite, ok):
    assert (SchemaChecker(SCHEMA).check(_fm(cite)) == []) == ok
