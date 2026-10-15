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


# --- deferred minors from Plan 1's final review -------------------------------------------------------------
import json  # noqa: E402
import sqlite3  # noqa: E402

import rdflib  # noqa: E402
from typer.testing import CliRunner  # noqa: E402

from solar_kb.cli import app  # noqa: E402
from solar_kb.export import export_all  # noqa: E402
from solar_kb.graph import build_graph  # noqa: E402
from solar_kb.query import Graph  # noqa: E402
from solar_kb.records import load_corpus  # noqa: E402
from solar_kb.rules import ALL_RULES  # noqa: E402
from solar_kb.validate import validate_corpus  # noqa: E402
from tests.helpers import FIXTURES, REPO, copy_fixture, write_record  # noqa: E402

CITE = f'    cite: [{{src: "src:iea-t13-failures", loc: "sec=1", h: "{H}"}}]\n    review: drafted\n'


def hits(root, overlay=None):
    corpus = load_corpus(root, overlay)
    out = []
    for rule in ALL_RULES:
        out += rule(corpus)
    return {(v.rule, v.record_id) for v in out}


def probe(root, claim, front_extra=""):
    write_record(root, "failure-modes", "probe",
                 f"id: fm:probe\ntype: FailureMode\nname: Probe\n{front_extra}claims:\n" + claim)


@pytest.mark.parametrize("claim", [
    f'  - claim_id: c1\n    rel: leads_to\n    target: fm:pid\n    cite: [{{src: "src:iea-t13-failures", loc: "p=12\\n", h: "{H}"}}]\n    review: drafted\n',
    f'  - claim_id: c1\n    rel: leads_to\n    target: " fm:pid"\n' + CITE,
    f'  - claim_id: "c1\\n"\n    rel: leads_to\n    target: fm:pid\n' + CITE,
])
def test_newlines_and_padding_in_identifier_fields_are_rejected(tmp_path, claim):
    root = copy_fixture(tmp_path, "mini")
    probe(root, claim)
    assert ("field-format", "fm:probe") in hits(root)


def test_blank_name_is_rejected(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "symptoms", "blank", "id: symptom:blank\ntype: Symptom\nname: '  '")
    assert ("field-format", "symptom:blank") in hits(root)


@pytest.mark.parametrize("loc", ["t=10:00-00:05", "t=01:00-01:00", "p=0", "tbl=0", "tbl=2.r0", "fig=0",
                                 "sec=4..3", "sec=4."])
def test_nonsense_locators_are_rejected(tmp_path, loc):
    root = copy_fixture(tmp_path, "mini")
    probe(root, f'  - claim_id: c1\n    rel: leads_to\n    target: fm:pid\n'
                f'    cite: [{{src: "src:iea-t13-failures", loc: "{loc}", h: "{H}"}}]\n    review: drafted\n')
    assert ("locators", "fm:probe") in hits(root)


def test_sane_locators_pass(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    for i, loc in enumerate(["t=00:05-10:00", "p=1", "tbl=1.r1", "fig=1", "sec=A.1", "sec=h12", "sec=front"]):
        write_record(root, "failure-modes", f"ok-{i}",
                     f"id: fm:ok-{i}\ntype: FailureMode\nname: OK\nclaims:\n  - claim_id: c1\n    rel: leads_to\n"
                     f'    target: fm:pid\n    cite: [{{src: "src:iea-t13-failures", loc: "{loc}", h: "{H}"}}]\n'
                     "    review: drafted\n")
    assert not {r for r, rid in hits(root) if rid and rid.startswith("fm:ok-")}


@pytest.mark.parametrize("claim", [
    "  - claim_id: c1\n    rel: leads_to\n    target: fm:pid\n    value: {nominal: 3, unit: unit:PERCENT}\n"
    "    conditions: x\n" + CITE,
    "  - claim_id: c1\n    attr: typical_power_loss\n    target: fm:pid\n    value: {nominal: 3, unit: unit:PERCENT}\n"
    "    conditions: x\n" + CITE,
])
def test_mixed_claim_shapes_are_rejected(tmp_path, claim):
    root = copy_fixture(tmp_path, "mini")
    probe(root, claim)
    assert ("claim-shape", "fm:probe") in hits(root)


@pytest.mark.parametrize("value", ["{nominal: .nan, unit: unit:PERCENT}", "{min: -.inf, max: 3, unit: unit:PERCENT}"])
def test_non_finite_numbers_are_rejected(tmp_path, value):
    root = copy_fixture(tmp_path, "mini")
    probe(root, f"  - claim_id: c1\n    attr: typical_power_loss\n    value: {value}\n    conditions: x\n" + CITE)
    assert ("quantities", "fm:probe") in hits(root)


def test_validity_window_must_be_ordered(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    probe(root, "  - claim_id: c1\n    rel: leads_to\n    target: fm:pid\n    valid_from: 2026-01-01\n"
                "    valid_to: 2025-01-01\n" + CITE)
    assert ("claim-shape", "fm:probe") in hits(root)


def test_stray_files_and_nested_dirs_are_reported(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    (root / "records" / "failure-modes" / "notes.markdown").write_text("---\nid: fm:x\n---\n")
    (root / "records" / "failure-modes" / "drafts").mkdir()
    corpus = load_corpus(root)
    assert [v.rule for v in corpus.load_errors] == ["layout", "layout"]


def test_dangling_symlink_is_a_parse_error_not_a_crash(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    (root / "records" / "symptoms" / "ghost.md").symlink_to(tmp_path / "nowhere.md")
    assert [v.rule for v in load_corpus(root).load_errors] == ["parse"]


def test_graph_stores_relative_paths_and_layers(tmp_path):
    db = tmp_path / "g.sqlite"
    build_graph(load_corpus(FIXTURES / "mini", FIXTURES / "overlay"), db, "t")
    con = sqlite3.connect(db)
    paths = [r[0] for r in con.execute("SELECT path FROM nodes")]
    assert all(not p.startswith("/") for p in paths) and "records/failure-modes/pid.md" in paths
    assert dict(con.execute("SELECT key, value FROM meta"))["layers"] == "public+overlay"
    build_graph(load_corpus(FIXTURES / "mini"), db, "t")
    assert dict(sqlite3.connect(db).execute("SELECT key, value FROM meta"))["layers"] == "public"


def test_records_jsonld_types_records_with_their_owl_classes(tmp_path):
    export_all(load_corpus(FIXTURES / "mini"), SCHEMA, tmp_path)
    records = rdflib.Graph().parse(tmp_path / "records.jsonld", format="json-ld")
    owl = rdflib.Graph().parse(tmp_path / "solar_kb.owl.ttl", format="turtle")
    cls = rdflib.URIRef("https://solarlattice.org/kb/FailureMode")
    assert (rdflib.URIRef("https://solarlattice.org/kb/fm/pid"), rdflib.RDF.type, cls) in records
    assert (cls, rdflib.RDF.type, rdflib.OWL.Class) in owl


def test_resolve_labels_exact_and_fuzzy_matches(mini_graph):
    assert mini_graph.resolve("PID")[0]["match"] == "exact"
    assert mini_graph.resolve("bypass diode open")[0]["match"] == "fuzzy"


def test_claims_keep_file_order_not_text_order(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    claims = "".join(f"  - claim_id: c{i}\n    rel: leads_to\n    target: fm:pid\n" + CITE for i in (2, 10))
    probe(root, claims)
    db = tmp_path / "g.sqlite"
    build_graph(load_corpus(root), db, "t")
    assert [e["claim_id"] for e in Graph(db).neighbors("fm:probe")] == ["c2", "c10"]


def test_obsidian_heading_and_block_links_resolve(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "probe", "id: fm:probe\ntype: FailureMode\nname: P",
                 "See [[failure-modes/pid#Causes|PID causes]] and [[detection-methods/el-imaging#^b1]].")
    assert not {r for r, rid in hits(root) if rid == "fm:probe"}


def _repo(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    (root / "schema").mkdir()
    (root / "schema" / "solar_kb.yaml").write_text((REPO / "schema" / "solar_kb.yaml").read_text())
    return root


@pytest.mark.parametrize("args", [
    ["query", "neighbors", "fm:pid", "--direction", "sideways"],
    ["query", "neighbors", "fm:pid", "--min-review", "approved"],
    ["query", "differential", "symptom:uniform-power-loss", "--k", "0"],
])
def test_cli_bad_arguments_exit_2_without_traceback(tmp_path, args):
    root = _repo(tmp_path)
    runner = CliRunner()
    assert runner.invoke(app, ["build", "--root", str(root), "--out", str(tmp_path / "b")]).exit_code == 0
    result = runner.invoke(app, args + ["--db", str(tmp_path / "b" / "graph.sqlite")])
    assert result.exit_code == 2, result.output


def test_cli_missing_graph_exits_2(tmp_path):
    result = CliRunner().invoke(app, ["query", "resolve", "PID", "--db", str(tmp_path / "none.sqlite")])
    assert result.exit_code == 2 and "solar-kb build" in result.output


def test_build_outputs_are_replaced_all_or_nothing(tmp_path, monkeypatch):
    root, out = _repo(tmp_path), tmp_path / "b"
    runner = CliRunner()
    assert runner.invoke(app, ["build", "--root", str(root), "--out", str(out)]).exit_code == 0
    before = {p.name: p.read_bytes() for p in out.iterdir() if p.is_file()}
    write_record(root, "symptoms", "extra", "id: symptom:extra\ntype: Symptom\nname: Extra")

    def boom(*a, **k):
        raise RuntimeError("OWL generator crashed")

    monkeypatch.setattr("solar_kb.cli.export_all", boom)
    result = runner.invoke(app, ["build", "--root", str(root), "--out", str(out)])
    assert result.exit_code != 0
    assert {p.name: p.read_bytes() for p in out.iterdir() if p.is_file()} == before
