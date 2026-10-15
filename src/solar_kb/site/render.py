"""Jinja2 rendering into the site directory (site spec §3.2)."""
from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, PackageLoader, StrictUndefined

from solar_kb.site.paths import href


class Renderer:
    """Writes pages and files under `out_dir` and records every site path written, in order."""

    def __init__(self, out_dir: Path, schema_version: str):
        self.out_dir = Path(out_dir)
        self.env = Environment(loader=PackageLoader("solar_kb.site", "templates"), autoescape=True,
                               undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
        self.env.globals["schema_version"] = schema_version
        self.written: list[str] = []
        self.origins: dict[str, list[str]] = {}  # site path -> what wrote it, for collision messages

    def page(self, template: str, path: str | None, origin: str | None = None, **context) -> None:
        """Render `template` to site path `path`. path=None renders 404.html, whose links are root-absolute
        because Pages serves it at whatever URL was missing."""
        if path is None:
            out = "404.html"

            def rel(to: str, fragment: str = "") -> str:
                return "/" + href("index.html", to, fragment).removeprefix("./")
        else:
            out = path

            def rel(to: str, fragment: str = "") -> str:
                return href(path, to, fragment)
        context.setdefault("canonical", None)
        self.write(out, self.env.get_template(template).render(rel=rel, **context), origin or template)

    def write(self, path: str, text: str, origin: str = "file") -> None:
        target = self.out_dir / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        self.written.append(path)
        self.origins.setdefault(path, []).append(origin)
