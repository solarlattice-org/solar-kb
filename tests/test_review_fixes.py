"""Regression tests for findings from the final whole-branch review."""
import pytest
from typer.testing import CliRunner

from solar_kb.cli import app
from solar_kb.graph import build_graph
from solar_kb.query import Graph
from solar_kb.records import load_corpus
from solar_kb.rules import ALL_RULES
from solar_kb.validate import validate_corpus
from solar_kb.yamlio import load_yaml
from tests.helpers import FIXTURES, SCHEMA, copy_fixture, write_record, copy_schema

CITE = '    cite: [{src: "src:iea-t13-failures", loc: "sec=1", h: "a1b2c3d4e5f6"}]\n    review: drafted\n'


def run_rules(corpus):
    out = []
    for rule in ALL_RULES:
        out += rule(corpus)
    return out


# F1: unhashable values in referenced records / cited sources must not crash validation
def test_unhashable_claim_id_in_referenced_record_does_not_crash(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "odd", "id: fm:odd\ntype: FailureMode\nname: O\nclaims:\n"
                 "  - claim_id: [c1]\n    rel: leads_to\n    target: fm:pid\n" + CITE)
    write_record(root, "failure-modes", "probe", "id: fm:probe\ntype: FailureMode\nname: P\nclaims:\n"
                 "  - claim_id: c1\n    rel: leads_to\n    target: fm:pid\n"
                 '    conflicts_with: ["fm:odd#c1"]\n    review: disputed\n'
                 '    cite: [{src: "src:iea-t13-failures", loc: "sec=1", h: "a1b2c3d4e5f6"}]\n')
    assert validate_corpus(load_corpus(root), SCHEMA)


def test_unhashable_source_tier_does_not_crash(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "sources", "odd", "id: src:odd\ntype: Source\nname: O\ntier: [open]\ntdm_ok: 'yes'")
    write_record(root, "failure-modes", "probe", "id: fm:probe\ntype: FailureMode\nname: P\nclaims:\n"
                 "  - claim_id: c1\n    rel: leads_to\n    target: fm:pid\n"
                 '    cite: [{src: "src:odd", loc: "sec=1", h: "a1b2c3d4e5f6"}]\n    review: drafted\n')
    assert validate_corpus(load_corpus(root), SCHEMA)


# F2: explicit nulls are treated as absent; any corpus that validates must build
@pytest.mark.parametrize("extra", ["aliases:", "aliases: ~", "status:", "status: ~"])
def test_null_optional_fields_validate_and_build(tmp_path, extra):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "probe", f"id: fm:probe\ntype: FailureMode\nname: P\n{extra}")
    corpus = load_corpus(root)
    assert validate_corpus(corpus, SCHEMA) == []
    build_graph(corpus, tmp_path / "g.sqlite", "t")


@pytest.mark.parametrize("claim", [
    "  - claim_id: c1\n    rel: ~\n    target: fm:pid\n" + CITE,
    "  - claim_id: c1\n    attr: typical_power_loss\n    value: ~\n    conditions: x\n" + CITE,
])
def test_null_rel_or_value_is_rejected(tmp_path, claim):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "probe", "id: fm:probe\ntype: FailureMode\nname: P\nclaims:\n" + claim)
    assert "claim-shape" in {v.rule for v in validate_corpus(load_corpus(root), SCHEMA)}


# F3: no private ids in public records via claim refs; DataExample is overlay-only
@pytest.mark.parametrize("field", ['conflicts_with: ["fm:private-fm#c1"]', 'superseded_by: "fm:private-fm#c1"'])
def test_public_claim_ref_into_overlay_is_a_layer_violation(tmp_path, field):
    root = copy_fixture(tmp_path, "mini")
    overlay = copy_fixture(tmp_path, "overlay")
    write_record(overlay, "failure-modes", "private-fm", "id: fm:private-fm\ntype: FailureMode\n"
                 "name: Private\nclaims:\n  - claim_id: c1\n    rel: leads_to\n    target: fm:pid\n"
                 '    cite: [{src: "src:omnidian-work-orders", loc: "p=1", h: "a1b2c3d4e5f6"}]\n    review: disputed\n')
    write_record(root, "failure-modes", "probe", "id: fm:probe\ntype: FailureMode\nname: P\nclaims:\n"
                 f"  - claim_id: c1\n    rel: leads_to\n    target: fm:pid\n    {field}\n"
                 '    cite: [{src: "src:iea-t13-failures", loc: "sec=1", h: "a1b2c3d4e5f6"}]\n    review: disputed\n')
    assert ("layers", "fm:probe") in {(v.rule, v.record_id) for v in run_rules(load_corpus(root, overlay))}


def test_data_example_is_overlay_only(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "data-examples", "d1", "id: dex:d1\ntype: DataExample\nname: D\n"
                 "dataset: acme-customer-scada")
    assert ("layers", "dex:d1") in {(v.rule, v.record_id) for v in run_rules(load_corpus(root))}


# F6: YAML 1.2 numerics - no octal, no base-60
def test_yaml_numbers_follow_yaml_1_2():
    data = load_yaml("a: 010\nb: 1:30\nc: 0o10\nd: 1e3\ne: -2.5\nf: 7\ng: .nan\nh: 0x1F")
    assert data["a"] == 10 and data["b"] == "1:30" and data["c"] == 8
    assert data["d"] == 1000.0 and data["e"] == -2.5 and data["f"] == 7 and data["h"] == 31


# F7: a claim that conflicts with another must be disputed
def test_conflicts_with_requires_disputed(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "probe", "id: fm:probe\ntype: FailureMode\nname: P\nclaims:\n"
                 "  - claim_id: c1\n    rel: leads_to\n    target: fm:pid\n"
                 '    conflicts_with: ["fm:pid#c1"]\n' + CITE)
    assert ("claim-shape", "fm:probe") in {(v.rule, v.record_id) for v in run_rules(load_corpus(root))}


# F8: an explicit overlay path without records/ is an error, not a silent no-op
def test_explicit_overlay_without_records_dir_is_an_error(tmp_path):
    corpus = load_corpus(FIXTURES / "mini", tmp_path / "no-such-overlay")
    assert "layout" in {v.rule for v in corpus.load_errors}


# F4: superseded / expired claims are not current knowledge for differential
def _graph_with(tmp_path, extra_claim_fields: str) -> Graph:
    root = copy_fixture(tmp_path, "mini")
    path = root / "records" / "failure-modes" / "soiling.md"
    text = path.read_text().replace(
        "    target: symptom:uniform-power-loss\n",
        "    target: symptom:uniform-power-loss\n" + extra_claim_fields, 1)
    path.write_text(text)
    corpus = load_corpus(root)
    assert validate_corpus(corpus, SCHEMA) == []
    build_graph(corpus, tmp_path / "g.sqlite", "t")
    return Graph(tmp_path / "g.sqlite")


def test_superseded_claim_is_excluded_from_differential(tmp_path):
    graph = _graph_with(tmp_path, '    superseded_by: "fm:soiling#c2"\n')
    ids = [c["id"] for c in graph.differential(["symptom:uniform-power-loss"])["candidates"]]
    assert ids == ["fm:pid"]


def test_expired_claim_is_excluded_but_visible_in_neighbors(tmp_path):
    graph = _graph_with(tmp_path, "    valid_to: 2020-01-01\n")
    ids = [c["id"] for c in graph.differential(["symptom:uniform-power-loss"])["candidates"]]
    assert ids == ["fm:pid"]
    assert graph.differential(["symptom:uniform-power-loss"], as_of="2019-06-01")["candidates"][1]["id"] \
        == "fm:soiling"
    [edge] = [e for e in graph.neighbors("fm:soiling", rel="presents_as")]
    assert edge["valid_to"] == "2020-01-01" and edge["superseded_by"] is None


# F5: differential carries provenance, totals and disputes
def test_differential_candidates_carry_supporting_claims(mini_graph):
    result = mini_graph.differential(["symptom:uniform-power-loss", "meas:el-negative-end-darkening"])
    pid = result["candidates"][0]
    support = {s["observation"]: s["claims"] for s in pid["support"]}
    assert support["symptom:uniform-power-loss"] == [
        {"record_id": "fm:pid", "claim_id": "c2", "review": "verified"}]
    assert support["meas:el-negative-end-darkening"] == [
        {"record_id": "fm:pid", "claim_id": "c3", "review": "verified"},
        {"record_id": "symptom:darkened-cells-in-el", "claim_id": "c1", "review": "verified"}]
    assert result["total_candidates"] == 2 and result["truncated"] is False


def test_differential_reports_truncation_and_disputed_matches(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    path = root / "records" / "failure-modes" / "bypass-diode-short.md"
    path.write_text(path.read_text().replace("target: symptom:string-power-step-loss",
                                             "target: symptom:uniform-power-loss")
                    .replace("review: verified", "review: disputed"))
    build_graph(load_corpus(root), tmp_path / "g.sqlite", "t")
    result = Graph(tmp_path / "g.sqlite").differential(["symptom:uniform-power-loss"], k=1)
    assert result["total_candidates"] == 2 and result["truncated"] is True
    assert result["disputed_matches"] == [{"failure_mode": "fm:bypass-diode-short",
                                           "observation": "symptom:uniform-power-loss",
                                           "record_id": "fm:bypass-diode-short", "claim_id": "c1"}]


def test_cli_overlay_typo_fails(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    copy_schema(root)
    result = CliRunner().invoke(app, ["validate", "--root", str(root), "--overlay", str(tmp_path / "typo")])
    assert result.exit_code == 1
