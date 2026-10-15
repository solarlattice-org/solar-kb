"""Record prose -> safe HTML (site spec §3.2).

Raw HTML is disabled because records come from outside contributors. Obsidian links [[<type-dir>/<slug>|label]]
survive markdown rendering as escaped text and are then turned into links, except inside code."""
from __future__ import annotations

import html
import re
from collections.abc import Mapping

from markdown_it import MarkdownIt

from solar_kb.records import TYPE_DIRS
from solar_kb.site.paths import href, record_path

_MD = MarkdownIt("commonmark", {"html": False})
_WIKILINK = re.compile(r"\[\[([^\]|]*)(?:\|([^\]]*))?\]\]")
_CODE = re.compile(r"(<pre>.*?</pre>|<code>.*?</code>)", re.S)


def render_prose(body: str, page_path: str, names: Mapping[str, str]) -> str:
    """Markdown body -> HTML for the page at site path `page_path`. `names` maps record id -> display name and
    is the set of records a wikilink may point at; any other wikilink raises ValueError."""
    parts = _CODE.split(_MD.render(body))
    return "".join(part if i % 2 else _WIKILINK.sub(lambda m: _link(m, page_path, names), part)
                   for i, part in enumerate(parts))


def _link(match: re.Match, page_path: str, names: Mapping[str, str]) -> str:
    target = html.unescape(match.group(1))
    # Obsidian heading/block suffixes ([[a/b#Heading]]) are accepted and dropped: bodies have no heading anchors.
    path = re.split(r"[#^]", target, maxsplit=1)[0].strip()
    type_dir, _, slug = path.partition("/")
    prefix = TYPE_DIRS.get(type_dir, (None, None))[1]
    rid = f"{prefix}:{slug}"
    if prefix is None or rid not in names:
        raise ValueError(f"wikilink [[{target}]] does not resolve")
    label = match.group(2) if match.group(2) is not None else html.escape(names[rid])  # group(2) is escaped text
    return f'<a href="{html.escape(href(page_path, record_path(rid)))}">{label}</a>'
