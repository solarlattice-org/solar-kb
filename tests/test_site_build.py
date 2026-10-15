"""The whole site: `solar-kb site`, output safety, and every IRI resolving (site spec §3.1, §5)."""
import pytest
import rdflib
from typer.testing import CliRunner

from solar_kb.cli import app
from solar_kb.iri import KB
from solar_kb.records import load_corpus
from solar_kb.site.build import SiteError, build_site
from solar_kb.site.linkcheck import broken_links
from solar_kb.site.paths import iri_to_path
from tests.helpers import FIXTURES, REPO, SCHEMA, copy_fixture, write_record

runner = CliRunner()
EXPORTS = ("solar_kb.owl.ttl", "solar_kb.context.jsonld", "solar_kb.schema.json", "solar_kb.yaml", "records.jsonld")


def _repo(tmp_path, fixture="mini"):
    root = copy_fixture(tmp_path, fixture) if fixture else tmp_path / "repo"
    (root / "records").mkdir(parents=True, exist_ok=True)
    (root / "schema").mkdir()
    (root / "schema" / "solar_kb.yaml").write_text((REPO / "schema" / "solar_kb.yaml").read_text())
    return root


def test_every_iri_resolves_and_no_link_is_dead(tmp_path):
    site = tmp_path / "site"
    build_site(load_corpus(FIXTURES / "mini"), SCHEMA, site)
    assert broken_links(site) == []
    g = rdflib.Graph().parse(site / "kb/solar_kb.owl.ttl", format="turtle")
    iris = {str(s) for s in g.subjects() if str(s).startswith(KB)}  # every term, the schema, every enum value
    iris |= {KB + "fm/pid", KB + "fm/pid#c8", KB + "src/nrel-pid-guide", KB, KB + "fm/"}
    for iri in sorted(iris):
        path, fragment = iri_to_path(iri)
        assert (site / path).is_file(), iri
        if fragment:
            assert f'id="{fragment}"' in (site / path).read_text(), iri
    assert (site / "CNAME").read_text() == "solarlattice.org\n"
    assert all((site / "kb" / name).is_file() for name in EXPORTS)


def test_build_site_refuses_private_records(tmp_path):
    with pytest.raises(SiteError, match="non-public records: .*case:wo-1001"):
        build_site(load_corpus(FIXTURES / "mini", FIXTURES / "overlay"), SCHEMA, tmp_path / "site")


def test_alias_that_is_another_records_id_is_a_collision(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    pid = root / "records/failure-modes/pid.md"
    pid.write_text(pid.read_text().replace("aliases: [PID, PID-s]", "aliases: [PID, 'fm:soiling']"))
    with pytest.raises(SiteError, match="collide: kb/fm/soiling.html vs kb/fm/soiling.html"):
        build_site(load_corpus(root), SCHEMA, tmp_path / "site")


def test_cli_site_replaces_a_previous_build(tmp_path):
    root, out = _repo(tmp_path), tmp_path / "_site"
    out.mkdir()
    (out / "CNAME").write_text("solarlattice.org\n")
    (out / "stale.html").write_text("old")
    result = runner.invoke(app, ["site", "--root", str(root), "--out", str(out)])
    assert result.exit_code == 0, result.output
    assert (out / "kb/fm/pid.html").is_file() and not (out / "stale.html").exists()
    assert not list(tmp_path.glob(".site-*")) and not list(tmp_path.glob("._site.old"))


def test_cli_site_with_no_records(tmp_path):
    root, out = _repo(tmp_path, fixture=None), tmp_path / "_site"
    result = runner.invoke(app, ["site", "--root", str(root), "--out", str(out)])
    assert result.exit_code == 0, result.output
    assert "No records have been published yet" in (out / "index.html").read_text()
    assert broken_links(out) == []


def test_cli_site_failure_keeps_the_previous_build(tmp_path):
    root, out = _repo(tmp_path), tmp_path / "_site"
    out.mkdir()
    (out / "CNAME").write_text("solarlattice.org\n")
    (out / "index.html").write_text("previous")
    write_record(root, "failure-modes", "bad", "id: fm:bad\ntype: FailureMode\nname: B\nclaims:\n"
                 "  - claim_id: c1\n    rel: leads_to\n    target: fm:missing\n"
                 '    cite: [{src: "src:iea-t13-failures", loc: "sec=1", h: "a1b2c3d4e5f6"}]\n    review: drafted')
    result = runner.invoke(app, ["site", "--root", str(root), "--out", str(out)])
    assert result.exit_code == 1 and (out / "index.html").read_text() == "previous"
    assert not list(tmp_path.glob(".site-*"))


def test_cli_site_refuses_to_replace_the_repo_or_a_foreign_directory(tmp_path):
    root = _repo(tmp_path)
    result = runner.invoke(app, ["site", "--root", str(root), "--out", str(root)])
    assert result.exit_code == 2 and "contains the repository root" in result.output
    assert (root / "schema" / "solar_kb.yaml").is_file()
    other = tmp_path / "docs"
    other.mkdir()
    (other / "notes.md").write_text("keep me")
    result = runner.invoke(app, ["site", "--root", str(root), "--out", str(other)])
    assert result.exit_code == 2 and "not a previous site build" in result.output
    assert (other / "notes.md").read_text() == "keep me"
