"""Assemble the whole site into one directory (site spec §3.1)."""
from __future__ import annotations

import shutil
from importlib.resources import files
from pathlib import Path

from solar_kb.export import export_all
from solar_kb.iri import load_prefixes
from solar_kb.records import Corpus
from solar_kb.site.linkcheck import broken_links
from solar_kb.site.pages import render_index_pages, render_record_pages, render_term_pages
from solar_kb.site.paths import collisions
from solar_kb.site.render import Renderer
from solar_kb.site.terms import load_ontology

DOMAIN = "solarlattice.org"
# Marks a directory as a site build, so `solar-kb site --out` may replace it. Hidden: Pages never publishes it.
SENTINEL = ".solar-kb-site"


class SiteError(RuntimeError):
    """The site cannot be published as built."""


def build_site(corpus: Corpus, schema_path: Path, out_dir: Path) -> list[str]:
    """Write the site into out_dir (normally an empty staging directory). Returns the site paths written.
    Refuses any non-public record, and fails on colliding output paths or a dead internal link."""
    private = sorted(r.id for r in corpus.records.values() if r.layer != "public")
    if private:
        raise SiteError(f"refusing to publish non-public records: {', '.join(private)}")
    out_dir = Path(out_dir)
    kb_dir = out_dir / "kb"
    written = [f"kb/{p.name}" for p in export_all(corpus, schema_path, kb_dir)]
    shutil.copyfile(schema_path, kb_dir / "solar_kb.yaml")
    written.append("kb/solar_kb.yaml")
    ontology = load_ontology(schema_path)
    terms = list(ontology.terms)
    r = Renderer(out_dir, schema_version=ontology.version)
    try:
        render_index_pages(r, corpus, terms)
        render_term_pages(r, corpus, terms, ontology.iri, ontology.description)
        render_record_pages(r, corpus, load_prefixes(schema_path))
    except ValueError as exc:  # e.g. a wikilink to a missing record in a corpus that skipped validation
        raise SiteError(str(exc)) from exc
    for asset in ("style.css", "solar-lattice-mark.svg", "solar-lattice-share.svg"):
        r.write(f"static/{asset}", files("solar_kb.site").joinpath("static", asset).read_text(encoding="utf-8"))
    share_png = Path(str(files("solar_kb.site").joinpath("static", "solar-lattice-share.png")))
    target_png = out_dir / "static/solar-lattice-share.png"
    target_png.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(share_png, target_png)
    r.written.append("static/solar-lattice-share.png")
    r.write("CNAME", f"{DOMAIN}\n")
    r.write(SENTINEL, "Built by `solar-kb site`; it may replace this directory.\n")
    written += r.written
    clashes = collisions(written)
    if clashes:
        raise SiteError("output paths collide: " + "; ".join(" vs ".join(c) for c in clashes))
    dead = broken_links(out_dir)
    if dead:
        raise SiteError("dead links:\n" + "\n".join(f"  {page}: {link}" for page, link in dead))
    return sorted(written)
