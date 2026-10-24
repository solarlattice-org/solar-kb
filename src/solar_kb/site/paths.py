"""The one map from IRIs to files in the built site (site spec §2). Pure functions, no I/O.

GitHub Pages serves foo.html at /foo with a 200, so every record and term IRI is a file, never a directory
(a directory would 301 /foo to /foo/ and change the IRI)."""
from __future__ import annotations

import posixpath
import re
from collections import defaultdict
from collections.abc import Iterable

from solar_kb.iri import KB
from solar_kb.records import OVERLAY_ONLY_TYPES, TYPE_DIRS

SITE_ROOT = "https://solarlattice.org/"
# (record type, id prefix, records/ directory) for every type the public site shows
PUBLIC_TYPES: tuple[tuple[str, str, str], ...] = tuple(
    (rtype, prefix, type_dir) for type_dir, (rtype, prefix) in TYPE_DIRS.items() if rtype not in OVERLAY_ONLY_TYPES
)


def record_path(rid: str) -> str:
    """fm:pid -> kb/fm/pid.html"""
    prefix, _, slug = rid.partition(":")
    return f"kb/{prefix}/{slug}.html"


def record_jsonld_path(rid: str) -> str:
    """fm:pid -> kb/fm/pid.jsonld"""
    return record_path(rid)[: -len(".html")] + ".jsonld"


def type_index_path(prefix: str) -> str:
    """fm -> kb/fm/index.html"""
    return f"kb/{prefix}/index.html"


def make_index_path(make: str) -> str:
    """chint -> kb/fc/chint.html: one page per make listing its fault codes by family (Plan 4d). A flat file beside the
    records; it cannot clash with a record because every fc: slug carries a family and a code."""
    return f"kb/fc/{make}.html"


def codes_json_path() -> str:
    """The fault-code lookup table the static filter box reads (Plan 4d)."""
    return "kb/fc/codes.json"


def term_path(iri: str) -> str:
    """https://solarlattice.org/kb/FailureMode -> kb/FailureMode.html. Only flat kb: IRIs are terms."""
    name = iri[len(KB):] if iri.startswith(KB) else ""
    if not name or "/" in name or "#" in name:
        raise ValueError(f"not a term IRI: {iri!r}")
    return f"kb/{name}.html"


def iri_to_path(iri: str) -> tuple[str, str]:
    """(file, fragment) that serves a solarlattice.org IRI, by the Pages rules above."""
    if not iri.startswith(SITE_ROOT):
        raise ValueError(f"not a solarlattice.org IRI: {iri!r}")
    rest, _, fragment = iri[len(SITE_ROOT):].partition("#")
    if rest == "" or rest.endswith("/"):
        return rest + "index.html", fragment
    return (rest if posixpath.splitext(rest)[1] else rest + ".html"), fragment


def href(from_path: str, to_path: str, fragment: str = "") -> str:
    """Relative link between two site files, written the way Pages serves them: no .html, and a directory
    index as its directory with a trailing slash."""
    is_index = posixpath.basename(to_path) == "index.html"
    if is_index:
        target = posixpath.dirname(to_path)
    else:
        target = to_path[: -len(".html")] if to_path.endswith(".html") else to_path
    rel = posixpath.relpath(target or ".", posixpath.dirname(from_path) or ".")
    if is_index:
        rel = "./" if rel == "." else rel + "/"
    return rel + (f"#{fragment}" if fragment else "")


def collisions(paths: Iterable[str]) -> list[tuple[str, ...]]:
    """Output paths that would clash:
    - the same file twice, or two names equal except for case (one file on a case-insensitive filesystem);
    - a page X.html next to a directory X/: Pages would have to choose what /X serves. Compared exactly,
      because Pages URLs are case-sensitive (kb/Stressor.html beside kb/stressor/ is fine)."""
    paths = list(paths)
    groups: dict[str, list[str]] = defaultdict(list)
    for p in paths:
        groups[p.lower()].append(p)
    clashes = [tuple(sorted(g)) for g in groups.values() if len(g) > 1]
    dirs: dict[str, str] = {}
    for p in sorted(paths):
        parent = posixpath.dirname(p)
        while parent:
            dirs.setdefault(parent, p)
            parent = posixpath.dirname(parent)
    for p in sorted(set(paths)):
        if p.endswith(".html") and p[: -len(".html")] in dirs:
            clashes.append((p, dirs[p[: -len(".html")]]))
    return sorted(clashes)


# Every public record prefix but src: (sources are not renamed into other types).
_FORMER_ID = re.compile(r"^(" + "|".join(p for _, p, _ in PUBLIC_TYPES if p != "src") + r"):[a-z0-9]+(-[a-z0-9]+)*$")


def alias_ids(rid: str, aliases: Iterable[object]) -> list[str]:
    """Aliases that are former ids of this record (a record-type prefix and a valid slug). Each gets a redirect
    stub (spec rule 4.5.7). The prefix may differ from the record's own: a stub merged into a record of another
    type (a "stressor" that was really a failure mode) keeps its old address. Free-text aliases such as 'PID' are
    names, not ids, and get nothing."""
    return sorted({a for a in aliases if isinstance(a, str) and _FORMER_ID.match(a) and a != rid})
