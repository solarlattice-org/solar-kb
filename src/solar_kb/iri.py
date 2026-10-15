"""CURIE -> IRI expansion with the schema's prefixes: the one place ids become IRIs."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

KB = "https://solarlattice.org/kb/"
CURIE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_]*):(\S+)$")


def load_prefixes(schema_path: Path) -> dict[str, str]:
    """The `prefixes:` map of the LinkML schema, e.g. {"fm": "https://solarlattice.org/kb/fm/", ...}."""
    data = yaml.safe_load(Path(schema_path).read_text(encoding="utf-8"))
    return dict(data.get("prefixes") or {})


def expand(value: str, prefixes: dict[str, str]) -> str:
    """'fm:pid' -> 'https://solarlattice.org/kb/fm/pid'. A fragment survives ('fm:pid#c3'); absolute http(s)
    IRIs pass through. Raises ValueError for a prefix the schema does not declare."""
    if value.startswith(("http://", "https://")):
        return value
    m = CURIE_RE.match(value)
    if m is None or m.group(1) not in prefixes:
        raise ValueError(f"cannot expand {value!r}: undeclared prefix")
    return prefixes[m.group(1)] + m.group(2)
