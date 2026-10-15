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
                                            "name": "Potential-induced degradation", "score": 1.0}
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
