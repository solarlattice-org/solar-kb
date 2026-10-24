"""CURIE -> IRI expansion with the schema's prefixes: the one place ids become IRIs."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

KB = "https://solarlattice.org/kb/"
CURIE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_]*):(\S+)$")


def load_prefixes(schema_path: Path) -> dict[str, str]:
    """The `prefixes:` map of the LinkML schema, e.g. {"fm": "https://solarlattice.org/kb/fm/", ...}: the root file's
    map plus those of its local imports (schema/modules/*.yaml, schema 0.5.0), the root winning on a clash."""
    path = Path(schema_path)
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    prefixes: dict[str, str] = {}
    for module in data.get("imports") or []:
        local = path.parent / f"{module}.yaml"
        if isinstance(module, str) and ":" not in module and local.is_file():
            prefixes.update(load_prefixes(local))
    prefixes.update(data.get("prefixes") or {})
    return prefixes


def expand(value: str, prefixes: dict[str, str]) -> str:
    """'fm:pid' -> 'https://solarlattice.org/kb/fm/pid'. A fragment survives ('fm:pid#c3'); absolute http(s)
    IRIs pass through. Raises ValueError for a prefix the schema does not declare."""
    if value.startswith(("http://", "https://")):
        return value
    m = CURIE_RE.match(value)
    if m is None or m.group(1) not in prefixes:
        raise ValueError(f"cannot expand {value!r}: undeclared prefix")
    return prefixes[m.group(1)] + m.group(2)
