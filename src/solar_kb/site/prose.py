"""Record prose -> safe HTML (site spec §3.2).

Raw HTML is disabled because records come from outside contributors. Obsidian links [[<type-dir>/<slug>|label]]
are found in markdown-it's text tokens, before the `text_join` core rule merges escapes into them: so `\\[\\[x\\]\\]`,
`&#91;&#91;x&#93;&#93;`, code and link titles stay literal text, and only links the validator also sees are rendered."""
from __future__ import annotations

import html
import re
from collections.abc import Container, Mapping

from markdown_it import MarkdownIt
from markdown_it.rules_core import StateCore
from markdown_it.token import Token

from solar_kb.records import TYPE_DIRS
from solar_kb.site.paths import href, record_path

_WIKILINK = re.compile(r"\[\[([^\]|]*)(?:\|([^\]]*))?\]\]")


def render_prose(body: str, page_path: str, names: Mapping[str, str], proposed: Container[str] = frozenset()) -> str:
    """Markdown body -> HTML for the page at site path `page_path`. `names` maps record id -> display name and
    is the set of records a wikilink may point at; any other wikilink raises ValueError. Links to ids in
    `proposed` (status: proposed stubs) get the *proposed* tag, as claim links do."""
    return _MD.render(body, {"page_path": page_path, "names": names, "proposed": proposed})


def _wikilinks(state: StateCore) -> None:
    page_path, names, proposed = state.env["page_path"], state.env["names"], state.env["proposed"]
    for block in state.tokens:
        if block.type != "inline" or not block.children:
            continue
        children: list[Token] = []
        for token in block.children:
            if token.type != "text" or "[[" not in token.content:
                children.append(token)
                continue
            pos = 0
            for match in _WIKILINK.finditer(token.content):
                children.append(_token("text", token.content[pos:match.start()]))
                children.append(_token("html_inline", _link(match, page_path, names, proposed)))
                pos = match.end()
            children.append(_token("text", token.content[pos:]))
        block.children = [t for t in children if t.type != "text" or t.content]


def _token(kind: str, content: str) -> Token:
    token = Token(kind, "", 0)
    token.content = content
    return token


def _link(match: re.Match, page_path: str, names: Mapping[str, str], proposed: Container[str]) -> str:
    target = match.group(1)
    # Obsidian heading/block suffixes ([[a/b#Heading]]) are accepted and dropped: bodies have no heading anchors.
    path = re.split(r"[#^]", target, maxsplit=1)[0].strip()
    type_dir, _, slug = path.partition("/")
    prefix = TYPE_DIRS.get(type_dir, (None, None))[1]
    rid = f"{prefix}:{slug}"
    if prefix is None or rid not in names:
        raise ValueError(f"wikilink [[{target}]] does not resolve")
    label = match.group(2) if match.group(2) is not None else names[rid]
    tag = ' <span class="badge proposed">proposed</span>' if rid in proposed else ""
    return f'<a href="{html.escape(href(page_path, record_path(rid)))}">{html.escape(label)}</a>{tag}'


_MD = MarkdownIt("commonmark", {"html": False})
_MD.core.ruler.before("text_join", "wikilinks", _wikilinks)
