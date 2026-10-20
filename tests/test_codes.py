"""The code_key grammar (Plan 4d). The first three tests are ported from solar-brain tests/test_faults_codes.py and
must stay equal in both repos: the compiler's key is the key the public graph looks up."""
import pytest

from solar_kb.codes import CodeKey, code_key, parse_code, query_code


def test_code_key_strips_zero_padding_and_case() -> None:
    assert parse_code("Fault0090").key == "fault90"
    assert parse_code("0104").key == "104" and parse_code("0104").number == 104
    assert parse_code("CRIT-4").key == "crit4" and parse_code("CRIT-4").prefix == "crit"
    assert parse_code("0000").key == "0"


def test_code_key_range_and_non_numeric() -> None:
    k = parse_code("IntProtect0010-0260")
    assert (k.key, k.prefix, k.number, k.number_end) == ("intprotect10-260", "intprotect", 10, 260)
    assert parse_code("ExtFanErr") == parse_code("extfanerr")
    assert parse_code("ExtFanErr").number is None
    assert parse_code("PV1 (2) VoltOver").key == "pv12voltover"


def test_query_code_drops_filler_words_but_keeps_vendor_prefixes() -> None:
    assert query_code("event 3501").key == "3501"
    assert query_code("Error no. 0104").key == "104"
    assert query_code("fault 90").key == "fault90"
    assert query_code("crit 4").key == "crit4"
    assert query_code("  #3701 ").key == "3701"
    assert query_code("NoGrid").key == "nogrid"  # a filler word only counts as a whole word
    assert query_code("ID 8206").key == "8206"


@pytest.mark.parametrize("printed, key", [
    ("3701", "3701"), ("6002-6412", "6002-6412"), ("Protect0090", "protect90"), ("GridV.OutLim", "gridvoutlim"),
    ("CRIT-4", "crit4"), ("2", "2"), ("OV-G-V", "ovgv"), ("IsolationErr", "isolationerr"), ("0104", "104"),
    ("104", "104"), ("Warn 0030", "warn30"),
])
def test_code_key_examples_from_the_plan(printed, key) -> None:
    assert code_key(printed) == key


def test_code_key_is_idempotent_so_the_graph_can_reparse_stored_keys() -> None:
    for printed in ("Protect0090", "6002-6412", "CRIT-4", "IsolationErr", "IntProtect0010-0260"):
        key = code_key(printed)
        assert code_key(key) == key
        assert parse_code(key) == CodeKey(key, parse_code(printed).prefix, parse_code(printed).number,
                                          parse_code(printed).number_end)
