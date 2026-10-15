import json

import pytest
from typer.testing import CliRunner

from solar_kb.benchmark import CaseError, load_cases, run_benchmark
from solar_kb.cli import app
from solar_kb.graph import build_graph
from solar_kb.records import load_corpus
from tests.helpers import FIXTURES

H = "a1b2c3d4e5f6"
SRC = f'{{cite: "src:iea-t13-failures#sec=4.3", h: "{H}"}}'

CASES = f"""
- id: pid-by-text-and-id
  observations:
    - text: Uniform power loss across a string
    - text: EL darkening at the negative end of strings
      id: meas:el-negative-end-darkening
  expected: fm:pid
  source: {SRC}
- id: soiling-tie-counts-as-top3
  observations:
    - text: gradual string underperformance
  expected: fm:soiling
  source: {SRC}
- id: diode-step
  observations:
    - text: Step loss of string power
  expected: fm:bypass-diode-short
  acceptable: [fm:pid]
  source: {SRC}
- id: nothing-resolves
  observations:
    - text: qqqq zzzz xxxx
  expected: fm:pid
  source: {SRC}
"""


@pytest.fixture
def graph(tmp_path):
    from solar_kb.query import Graph

    db = tmp_path / "g.sqlite"
    build_graph(load_corpus(FIXTURES / "mini"), db, "bench-1")
    return Graph(db)


def test_load_cases(tmp_path):
    (tmp_path / "c.yaml").write_text(CASES)
    cases = load_cases(tmp_path / "c.yaml")
    assert [c.id for c in cases] == ["pid-by-text-and-id", "soiling-tie-counts-as-top3", "diode-step",
                                     "nothing-resolves"]
    assert cases[0].observations[1].id == "meas:el-negative-end-darkening" and cases[2].acceptable == ("fm:pid",)


def test_run_benchmark_scores_top1_top3_and_unresolved(tmp_path, graph):
    (tmp_path / "c.yaml").write_text(CASES)
    report = run_benchmark(graph, load_cases(tmp_path / "c.yaml"))
    ranks = {r.id: r.rank for r in report.results}
    assert ranks == {"pid-by-text-and-id": 1, "soiling-tie-counts-as-top3": 2, "diode-step": 1,
                     "nothing-resolves": None}
    s = report.summary()
    assert (s["top1"], s["top3"], s["unresolved_observations"]) == (0.5, 0.75, 1)
    assert s["misses"] == ["nothing-resolves"] and s["kb_version"] == "bench-1"


@pytest.mark.parametrize("text, message", [
    ("[]", "non-empty"),
    (f"- id: a\n  observations: []\n  expected: fm:pid\n  source: {SRC}", "observations"),
    (f"- id: a\n  observations: [{{text: x, id: fm:pid}}]\n  expected: fm:pid\n  source: {SRC}", "symptom:"),
    (f"- id: a\n  observations: [{{text: x}}]\n  expected: pid\n  source: {SRC}", "fm:<slug>"),
    (f"- id: a\n  observations: [{{text: x}}]\n  expected: fm:pid\n  acceptable: [soiling]\n  source: {SRC}",
     "acceptable"),
    ("- id: a\n  observations: [{text: x}]\n  expected: fm:pid\n  source: {cite: 'src:a#p=1'}", "source"),
    (f"- id: a\n  observations: [{{text: x}}]\n  expected: fm:pid\n  source: {SRC}\n  why: x", "keys"),
    (f"- id: a\n  observations: [{{text: x}}]\n  expected: fm:pid\n  source: {SRC}\n"
     f"- id: a\n  observations: [{{text: x}}]\n  expected: fm:pid\n  source: {SRC}", "unique"),
])
def test_load_cases_rejects_malformed(tmp_path, text, message):
    (tmp_path / "c.yaml").write_text(text)
    with pytest.raises(CaseError, match=message):
        load_cases(tmp_path / "c.yaml")


def test_cli_eval_differential(tmp_path):
    db = tmp_path / "g.sqlite"
    build_graph(load_corpus(FIXTURES / "mini"), db, "bench-1")
    (tmp_path / "c.yaml").write_text(CASES)
    runner = CliRunner()
    result = runner.invoke(app, ["eval", "differential", "--cases", str(tmp_path / "c.yaml"), "--db", str(db)])
    assert result.exit_code == 0 and json.loads(result.output)["top3"] == 0.75
    assert runner.invoke(app, ["eval", "differential", "--cases", str(tmp_path / "none.yaml"),
                               "--db", str(db)]).exit_code == 2
