"""Dead-link check over a built site, resolving links the way GitHub Pages does (site spec §2.2)."""
from __future__ import annotations

import posixpath
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class _Collector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if value is None:
                continue
            if name in ("href", "src"):
                self.links.append(value)
            elif name == "id":
                self.ids.add(value)


def _parse(path: Path) -> _Collector:
    collector = _Collector()
    collector.feed(path.read_text(encoding="utf-8"))
    return collector


def resolve(site: Path, path: str) -> Path | None:
    """The file Pages serves for site path `path` ('' is the root), or None for a 404."""
    path = path.lstrip("/")
    if path == "" or path.endswith("/"):
        index = site / path / "index.html"
        return index if index.is_file() else None
    for candidate in (site / path, site / f"{path}.html", site / path / "index.html"):  # the last: /dir 301s to /dir/
        if candidate.is_file():
            return candidate
    return None


def broken_links(site: Path) -> list[tuple[str, str]]:
    """(page, link) for every internal href/src that 404s, and every #fragment with no matching id."""
    site = Path(site)
    parsed = {page: _parse(page) for page in sorted(site.rglob("*.html"))}
    out = []
    for page, collector in parsed.items():
        rel_page = page.relative_to(site).as_posix()
        for link in collector.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue  # external: https:, mailto:, //host
            path = unquote(parts.path)
            if path == "":
                target = page
            elif path.startswith("/"):
                target = resolve(site, path)
            else:
                joined = posixpath.normpath(posixpath.join(posixpath.dirname(rel_page), path))
                if joined == ".." or joined.startswith("../"):
                    out.append((rel_page, link))
                    continue
                joined = "" if joined == "." else joined
                target = resolve(site, joined + "/" if path.endswith("/") and joined else joined)
            if target is None:
                out.append((rel_page, link))
            elif parts.fragment and target.suffix == ".html":
                ids = parsed[target].ids if target in parsed else _parse(target).ids
                if parts.fragment not in ids:
                    out.append((rel_page, link))
    return out
