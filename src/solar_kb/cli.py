from __future__ import annotations

import json
import subprocess
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
    """Validate, then write graph.sqlite and the public exports."""
    corpus = _validated(root, overlay)
    build_graph(corpus, out / "graph.sqlite", _kb_version(root))
    for path in export_all(corpus, _schema(root), out):
        typer.echo(f"wrote {path}")
    typer.echo(f"wrote {out / 'graph.sqlite'}")


def _print(obj) -> None:
    typer.echo(json.dumps(obj, indent=2))


@query_app.command("resolve")
def q_resolve(text: str, db: Path = DB, limit: int = 5) -> None:
    _print(Graph(db).resolve(text, limit=limit))


@query_app.command("entity")
def q_entity(record_id: str, db: Path = DB) -> None:
    entity = Graph(db).get_entity(record_id)
    if entity is None:
        typer.echo(f"no such record: {record_id}", err=True)
        raise typer.Exit(1)
    _print(entity)


@query_app.command("neighbors")
def q_neighbors(record_id: str, db: Path = DB, rel: Optional[str] = None,
                direction: str = "out", min_review: str = "drafted") -> None:
    _print(Graph(db).neighbors(record_id, rel=rel, direction=direction, min_review=min_review))


@query_app.command("differential")
def q_differential(observations: list[str], db: Path = DB, k: int = 5,
                   min_review: str = "drafted") -> None:
    _print(Graph(db).differential(observations, min_review=min_review, k=k))
