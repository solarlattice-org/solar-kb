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


# --- final review fixes ----------------------------------------------------------------------------------------
REVIEW_CASES = f"""
- id: pinned-typo
  observations:
    - text: EL darkening
      id: meas:el-negative-end-darkning
  expected: fm:pid
  source: {SRC}
- id: fuzzy-uniform
  observations:
    - text: uniform power loss across strings
  expected: fm:soiling
  source: {SRC}
- id: expected-typo
  observations:
    - text: Step loss of string power
  expected: fm:bypass-diode-shrot
  source: {SRC}
"""


def _report(tmp_path, graph, text, **kw):
    (tmp_path / "c.yaml").write_text(text)
    return run_benchmark(graph, load_cases(tmp_path / "c.yaml"), **kw)


def test_unknown_pinned_ids_are_counted_not_dropped(tmp_path, graph):
    report = _report(tmp_path, graph, REVIEW_CASES)
    r = {x.id: x for x in report.results}["pinned-typo"]
    assert r.unknown_ids == ("meas:el-negative-end-darkning",) and r.reason == "unresolved"
    assert report.summary()["unresolved_observations"] >= 1


def test_resolutions_are_recorded_and_exact_only_excludes_fuzzy(tmp_path, graph):
    report = _report(tmp_path, graph, REVIEW_CASES)
    fuzzy = {x.id: x for x in report.results}["fuzzy-uniform"]
    assert fuzzy.resolved[0]["id"] == "symptom:uniform-power-loss" and fuzzy.resolved[0]["match"] == "fuzzy"
    assert report.summary()["fuzzy_resolutions"] == 1
    strict = _report(tmp_path, graph, REVIEW_CASES, exact_only=True)
    assert {x.id: x for x in strict.results}["fuzzy-uniform"].unresolved == ("uniform power loss across strings",)


def test_summary_separates_resolver_and_graph_misses(tmp_path, graph):
    report = _report(tmp_path, graph, CASES)
    s = report.summary()
    assert s["cases_fully_unresolved"] == 1 and s["cases_with_unresolved"] == 1
    assert s["top3_resolved"] == 1.0  # every case whose observations all resolved has its answer in the top 3
    assert s["miss_reasons"] == {"nothing-resolves": "unresolved"}


def test_unknown_expected_ids_are_reported(tmp_path, graph):
    s = _report(tmp_path, graph, REVIEW_CASES).summary()
    assert s["unknown_expected"] == ["expected-typo"]


def test_ties_are_visible_and_pessimistic_top3_is_reported(tmp_path, graph):
    report = _report(tmp_path, graph, CASES)
    r = {x.id: x for x in report.results}
    assert (r["soiling-tie-counts-as-top3"].rank, r["soiling-tie-counts-as-top3"].tied) == (2, 2)
    assert r["pid-by-text-and-id"].tied == 1 and r["soiling-tie-counts-as-top3"].pessimistic_rank == 2
    assert report.summary()["top3_pessimistic"] == 0.75


@pytest.mark.parametrize("text, message", [
    ("- id: a\n  observations: [{text: x}\n", "YAML"),
    (f"- id: a\n  observations: [{{text: x}}]\n  expected: fm:pid\n  source: {{cite: 'src:a#p=1', h: 123456789012}}",
     "quote"),
])
def test_yaml_errors_and_unquoted_hashes_are_case_errors(tmp_path, text, message):
    (tmp_path / "c.yaml").write_text(text)
    with pytest.raises(CaseError, match=message):
        load_cases(tmp_path / "c.yaml")


def test_non_utf8_case_file_is_a_case_error(tmp_path):
    (tmp_path / "c.yaml").write_bytes(b"- id: caf\xe9\n")
    with pytest.raises(CaseError):
        load_cases(tmp_path / "c.yaml")


def test_bad_min_review_fails_even_when_nothing_resolves(tmp_path, graph):
    with pytest.raises(ValueError, match="min_review"):
        _report(tmp_path, graph, f"- id: a\n  observations: [{{text: qqqq zzzz}}]\n  expected: fm:pid\n  source: {SRC}",
                min_review="bogus")


def test_cli_exit_2_on_yaml_syntax_error(tmp_path):
    db = tmp_path / "g.sqlite"
    build_graph(load_corpus(FIXTURES / "mini"), db, "bench-1")
    (tmp_path / "c.yaml").write_text("- id: a\n  observations: [{text: x}\n")
    result = CliRunner().invoke(app, ["eval", "differential", "--cases", str(tmp_path / "c.yaml"), "--db", str(db)])
    assert result.exit_code == 2 and "cases error" in result.output


def test_fault_code_observation_is_pinned_and_expanded(tmp_path, graph):
    text = (f"- id: code\n  observations: [{{text: inverter shows IsolationErr, id: fc:chint-sca-50-60ktl-isolationerr}}]\n"
            f"  expected: fm:insulation-loss\n  acceptable: [fm:leakage-current]\n  source: {SRC}")
    [r] = _report(tmp_path, graph, text).results
    assert r.rank == 1 and r.unknown_ids == () and r.resolved[0]["match"] == "pinned" and r.tied == 2
