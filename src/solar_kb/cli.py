from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Optional

import typer

from solar_kb.export import export_all
from solar_kb.graph import build_graph
from solar_kb.query import Graph
from solar_kb.records import load_corpus
from solar_kb.validate import validate_corpus

app = typer.Typer(no_args_is_help=True, help="Solar Lattice knowledge layer tools.")
query_app = typer.Typer(no_args_is_help=True, help="Query a built graph.")
app.add_typer(query_app, name="query")

ROOT = typer.Option(Path("."), help="solar-kb repository root.")
OVERLAY = typer.Option(None, help="Private overlay root (solar-brain/overlay).")
DB = typer.Option(Path("build/graph.sqlite"), help="Graph database.")


def _schema(root: Path) -> Path:
    return root / "schema" / "solar_kb.yaml"


def _kb_version(root: Path) -> str:
    try:
        out = subprocess.run(["git", "-C", str(root), "describe", "--tags", "--always", "--dirty"],
                             capture_output=True, text=True, check=True)
        return out.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unversioned"


def _validated(root: Path, overlay: Optional[Path]):
    corpus = load_corpus(root, overlay)
    violations = validate_corpus(corpus, _schema(root))
    for v in violations:
        typer.echo(str(v), err=True)
    if violations:
        typer.echo(f"{len(violations)} violation(s) in {len(corpus.records)} record(s)", err=True)
        raise typer.Exit(1)
    return corpus


@app.command()
def validate(root: Path = ROOT, overlay: Optional[Path] = OVERLAY) -> None:
    """Validate records against the schema and the §4.5 rules."""
    corpus = _validated(root, overlay)
    typer.echo(f"ok: {len(corpus.records)} record(s), 0 violations")


@app.command()
def build(root: Path = ROOT, overlay: Optional[Path] = OVERLAY,
          out: Path = typer.Option(Path("build"), help="Output directory.")) -> None:
    """Validate, then write graph.sqlite and the public exports. All outputs are generated into a temporary
    directory first and only then moved into place, so a failure leaves the previous build untouched."""
    corpus = _validated(root, overlay)
    out.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".build-", dir=out))
    try:
        build_graph(corpus, staging / "graph.sqlite", _kb_version(root))
        export_all(corpus, _schema(root), staging)
        for path in sorted(staging.iterdir()):
            os.replace(path, out / path.name)
            typer.echo(f"wrote {out / path.name}")
    finally:
        shutil.rmtree(staging, ignore_errors=True)


def _site_out_problem(out: Path, root: Path, sentinel: str) -> str | None:
    """--out is replaced wholesale, so only an empty directory or a previous site build (it holds `sentinel`) may be
    replaced. A CNAME is not proof: every Pages repo with a custom domain has one."""
    if out == root or root.is_relative_to(out):
        return f"--out {out} contains the repository root"
    if out.exists() and (not out.is_dir() or (any(out.iterdir()) and not (out / sentinel).is_file())):
        return f"--out {out} exists and is not a previous site build (no {sentinel}); refusing to replace it"
    return None


@app.command()
def site(root: Path = ROOT, out: Path = typer.Option(Path("_site"), help="Output directory (replaced).")) -> None:
    """Validate the public records, then build the solarlattice.org site. Never reads the private overlay."""
    try:
        from solar_kb.site.build import SENTINEL, SiteError, build_site
    except ImportError as exc:  # jinja2 / markdown-it-py come from the optional [site] extra
        typer.echo(f"error: {exc}; install with: pip install -e '.[site]'", err=True)
        raise typer.Exit(2)
    root, out = root.resolve(), out.resolve()
    problem = _site_out_problem(out, root, SENTINEL)
    if problem:
        typer.echo(f"error: {problem}", err=True)
        raise typer.Exit(2)
    corpus = _validated(root, None)
    out.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".site-", dir=out.parent))
    try:
        written = build_site(corpus, _schema(root), staging)
        staging.chmod(0o755)  # mkdtemp makes it 0700; Pages needs it readable
        old = None
        if out.exists():  # swap, then delete: the previous build is never gone before the new one is in place
            old = out.with_name(f".{out.name}.old")
            shutil.rmtree(old, ignore_errors=True)
            os.replace(out, old)
        os.replace(staging, out)
        if old is not None:
            shutil.rmtree(old, ignore_errors=True)
    except SiteError as exc:
        typer.echo(f"error: {exc}", err=True)
        raise typer.Exit(1)
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    typer.echo(f"wrote {len(written)} files to {out}")


def _print(obj) -> None:
    typer.echo(json.dumps(obj, indent=2))


def _graph(db: Path) -> Graph:
    try:
        return Graph(db)
    except FileNotFoundError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(2)


def _run(fn):
    """Run a query; invalid arguments (ValueError) become a one-line error and exit code 2."""
    try:
        return fn()
    except ValueError as exc:
        typer.echo(f"error: {exc}", err=True)
        raise typer.Exit(2)


@query_app.command("resolve")
def q_resolve(text: str, db: Path = DB, limit: int = 5) -> None:
    _print(_run(lambda: _graph(db).resolve(text, limit=limit)))


@query_app.command("entity")
def q_entity(record_id: str, db: Path = DB) -> None:
    entity = _graph(db).get_entity(record_id)
    if entity is None:
        typer.echo(f"no such record: {record_id}", err=True)
        raise typer.Exit(1)
    _print(entity)


@query_app.command("neighbors")
def q_neighbors(record_id: str, db: Path = DB, rel: Optional[str] = None,
                direction: str = "out", min_review: str = "drafted") -> None:
    _print(_run(lambda: _graph(db).neighbors(record_id, rel=rel, direction=direction, min_review=min_review)))


@query_app.command("differential")
def q_differential(observations: list[str], db: Path = DB, k: int = 5,
                   min_review: str = "drafted") -> None:
    _print(_run(lambda: _graph(db).differential(observations, min_review=min_review, k=k)))
