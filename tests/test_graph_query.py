import sqlite3

import pytest

from solar_kb.graph import build_graph, normalize
from solar_kb.query import Graph
from solar_kb.records import load_corpus
from tests.helpers import FIXTURES, copy_fixture, write_record


def test_normalize():
    assert normalize("PID-s (shunting)") == "pidsshunting"


def test_build_is_atomic_and_rebuildable(tmp_path):
    db = tmp_path / "out" / "graph.sqlite"
    corpus = load_corpus(FIXTURES / "mini")
    build_graph(corpus, db, "v1")
    build_graph(corpus, db, "v2")
    con = sqlite3.connect(db)
    assert con.execute("SELECT value FROM meta").fetchone() == ("v2",)
    assert con.execute("SELECT count(*) FROM nodes").fetchone()[0] == len(corpus.records)
    assert not (tmp_path / "out" / "graph.tmp").exists()


def test_missing_db_has_actionable_error(tmp_path):
    with pytest.raises(FileNotFoundError, match="solar-kb build"):
        Graph(tmp_path / "nope.sqlite")


def test_resolve_exact_alias_and_fuzzy(mini_graph):
    assert mini_graph.resolve("PID")[0] == {"id": "fm:pid", "type": "FailureMode",
                                            "name": "Potential-induced degradation", "score": 1.0,
                                            "match": "exact"}
    assert mini_graph.resolve("potential induced degradation")[0]["id"] == "fm:pid"
    assert mini_graph.resolve("electroluminesence imaging")[0]["id"] == "method:el-imaging"
    assert mini_graph.resolve("EL", types=["FailureMode"]) == []


@pytest.mark.parametrize("text", ["", "   ", "!!!", "zzzzzzzzzzqqqq"])
def test_resolve_junk_returns_empty(mini_graph, text):
    assert mini_graph.resolve(text) == []


def test_resolve_hides_proposed_stubs_by_default(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "snail-trails",
                 "id: fm:snail-trails\ntype: FailureMode\nname: Snail trails\nstatus: proposed")
    db = tmp_path / "g.sqlite"
    build_graph(load_corpus(root), db, "t")
    graph = Graph(db)
    assert graph.resolve("snail trails") == []
    assert graph.resolve("snail trails", include_proposed=True)[0]["id"] == "fm:snail-trails"


def test_get_entity(mini_graph):
    entity = mini_graph.get_entity("fm:pid")
    assert entity["type"] == "FailureMode" and entity["kb_version"] == "test-1"
    assert entity["data"]["claims"][0]["verified_at"] == "2026-11-02"
    assert mini_graph.get_entity("fm:nope") is None


def test_neighbors_directions_and_review_floor(mini_graph):
    out = mini_graph.neighbors("fm:pid", rel="presents_as")
    assert [e["target"] for e in out] == ["symptom:uniform-power-loss", "symptom:darkened-cells-in-el"]
    assert out[0]["cite"] == [{"src": "src:iea-t13-failures", "loc": "sec=4.3", "h": "a1b2c3d4e5f6"}]
    incoming = mini_graph.neighbors("symptom:uniform-power-loss", direction="in")
    assert {e["source"] for e in incoming} == {"fm:pid", "fm:soiling"}
    verified_in = mini_graph.neighbors("symptom:uniform-power-loss", direction="in",
                                       min_review="verified")
    assert {e["source"] for e in verified_in} == {"fm:pid"}
    assert len(mini_graph.neighbors("fm:pid", direction="both")) == 8  # 7 out + 1 in


@pytest.mark.parametrize("kwargs", [{"direction": "sideways"}, {"min_review": "approved"}])
def test_neighbors_rejects_bad_arguments(mini_graph, kwargs):
    with pytest.raises(ValueError):
        mini_graph.neighbors("fm:pid", **kwargs)


# --- Plan 4d: fault codes ------------------------------------------------------------------------------------------
def test_fault_codes_table_and_code_aliases(tmp_path):
    db = tmp_path / "g.sqlite"
    build_graph(load_corpus(FIXTURES / "mini"), db, "t")
    con = sqlite3.connect(db)
    rows = con.execute("SELECT record_id, make, model_family, code_key, code_from, code_to FROM fault_codes "
                       "ORDER BY record_id").fetchall()
    assert ("fc:sma-stp-core1-us-6002-6412", "sma", "stp-core1-us", "6002-6412", 6002, 6412) in rows
    assert ("fc:chint-sca-50-60ktl-isolationerr", "chint", "sca-50-60ktl", "isolationerr", None, None) in rows
    assert len(rows) == 6
    graph = Graph(db)
    for alias in ("IsolationErr", "CPS IsolationErr", "Insulation resistance low"):  # generic aliases still resolve
        assert graph.resolve(alias, types=["FaultCode"])[0]["id"].endswith("-isolationerr")


def test_resolve_code_exact_zero_padding_filler_and_ranking(mini_graph):
    hits = mini_graph.resolve_code("IsolationErr")
    assert [h["id"] for h in hits] == ["fc:chint-sca-36ktl-isolationerr", "fc:chint-sca-50-60ktl-isolationerr"]
    assert hits[0]["match"] == "exact" and hits[0]["code"] == "IsolationErr" and hits[0]["make_name"] == "CPS"
    assert hits[0]["display_message"] == "Insulation resistance low" and hits[0]["query_key"] == "isolationerr"
    assert mini_graph.resolve_code("isolation err", family="sca-50-60ktl")[0]["id"] == "fc:chint-sca-50-60ktl-isolationerr"
    assert mini_graph.resolve_code("event 3501")[0]["id"] == "fc:sma-stp-core1-us-3501"
    assert mini_graph.resolve_code("Error no. 003501")[0]["match"] == "exact"  # zero padding and filler words
    assert mini_graph.resolve_code("3501", make="chint")[0]["id"] == "fc:sma-stp-core1-us-3501"  # ranked, not filtered
    assert mini_graph.resolve_code("PROTECT 0090")[0]["id"] == "fc:chint-sca-50-60ktl-protect90"


def test_resolve_code_range_containment_then_bare_number(mini_graph):
    [hit] = mini_graph.resolve_code("6100")
    assert hit["id"] == "fc:sma-stp-core1-us-6002-6412" and hit["match"] == "range" and hit["code"] == "6002-6412"
    assert mini_graph.resolve_code("6002-6412")[0]["match"] == "exact"
    assert mini_graph.resolve_code("crit 6100") == []  # a range only contains numbers under its own prefix
    [hit] = mini_graph.resolve_code("90")  # no exact or range hit: the bare number finds Protect0090
    assert hit["id"] == "fc:chint-sca-50-60ktl-protect90" and hit["match"] == "number"
    assert mini_graph.resolve_code("6002") == [] or mini_graph.resolve_code("6002")[0]["match"] == "range"


@pytest.mark.parametrize("text", ["", "   ", "event", "99999"])
def test_resolve_code_junk_returns_empty(mini_graph, text):
    assert mini_graph.resolve_code(text) == []
    assert mini_graph.resolve_code("3501", limit=0) == []
