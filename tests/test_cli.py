import json

from typer.testing import CliRunner

from solar_kb.cli import app
from tests.helpers import REPO, copy_fixture, write_record

runner = CliRunner()


def _repo(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    (root / "schema").mkdir()
    (root / "schema" / "solar_kb.yaml").write_text((REPO / "schema" / "solar_kb.yaml").read_text())
    return root


def test_validate_ok_and_failure(tmp_path):
    root = _repo(tmp_path)
    result = runner.invoke(app, ["validate", "--root", str(root)])
    assert result.exit_code == 0 and "0 violations" in result.output
    write_record(root, "failure-modes", "bad", "id: fm:bad\ntype: FailureMode\nname: B\nclaims:\n"
                 "  - claim_id: c1\n    rel: leads_to\n    target: fm:missing\n"
                 '    cite: [{src: "src:iea-t13-failures", loc: "sec=1", h: "a1b2c3d4e5f6"}]\n    review: drafted')
    result = runner.invoke(app, ["validate", "--root", str(root)])
    assert result.exit_code == 1 and "[targets] fm:bad#c1" in result.output


def test_build_then_query(tmp_path):
    root = _repo(tmp_path)
    out = tmp_path / "build"
    result = runner.invoke(app, ["build", "--root", str(root), "--out", str(out)])
    assert result.exit_code == 0, result.output
    db = str(out / "graph.sqlite")
    resolved = json.loads(runner.invoke(app, ["query", "resolve", "PID", "--db", db]).output)
    assert resolved[0]["id"] == "fm:pid"
    diff = runner.invoke(app, ["query", "differential", "symptom:uniform-power-loss", "--db", db])
    assert json.loads(diff.output)["candidates"][0]["id"] == "fm:pid"
    code = json.loads(runner.invoke(app, ["query", "resolve-code", "event 3501", "--db", db]).output)
    assert code[0]["id"] == "fc:sma-stp-core1-us-3501" and code[0]["match"] == "exact"
    ranked = json.loads(runner.invoke(app, ["query", "resolve-code", "IsolationErr", "--db", db,
                                            "--family", "sca-50-60ktl"]).output)
    assert ranked[0]["id"] == "fc:chint-sca-50-60ktl-isolationerr"
    missing = runner.invoke(app, ["query", "entity", "fm:nope", "--db", db])
    assert missing.exit_code == 1


def test_build_refuses_invalid_corpus(tmp_path):
    root = _repo(tmp_path)
    (root / "records" / "symptoms" / "broken.md").write_text("nope")
    result = runner.invoke(app, ["build", "--root", str(root), "--out", str(tmp_path / "b")])
    assert result.exit_code == 1 and not (tmp_path / "b" / "graph.sqlite").exists()
