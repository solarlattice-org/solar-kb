"""YAML loading with YAML 1.2-style scalars.

PyYAML's SafeLoader follows YAML 1.1: `yes`/`no`/`on`/`off` become booleans,
`2026-11-02` becomes a datetime.date, `010` is octal 8 and `1:30` is base-60 90.
These break validation or silently change numbers, so this loader uses YAML 1.2
core-schema rules: only true/false are booleans, dates stay strings, integers are
decimal unless prefixed 0o/0x, and there is no base-60.
"""
from __future__ import annotations

import re

import yaml

_BOOL = "tag:yaml.org,2002:bool"
_TIMESTAMP = "tag:yaml.org,2002:timestamp"
_INT = "tag:yaml.org,2002:int"
_FLOAT = "tag:yaml.org,2002:float"
_REPLACED = (_BOOL, _TIMESTAMP, _INT, _FLOAT)


class KBLoader(yaml.SafeLoader):
    pass


KBLoader.yaml_implicit_resolvers = {
    first: [(tag, rx) for tag, rx in resolvers if tag not in _REPLACED]
    for first, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
KBLoader.add_implicit_resolver(
    _BOOL, re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$"), list("tTfF")
)
KBLoader.add_implicit_resolver(
    _INT, re.compile(r"^(?:[-+]?[0-9]+|0o[0-7]+|0x[0-9a-fA-F]+)$"), list("-+0123456789")
)
KBLoader.add_implicit_resolver(
    _FLOAT,
    re.compile(r"^(?:[-+]?(?:\.[0-9]+|[0-9]+(?:\.[0-9]*)?)(?:[eE][-+]?[0-9]+)?"
               r"|[-+]?\.(?:inf|Inf|INF)|\.(?:nan|NaN|NAN))$"),
    list("-+.0123456789"),
)


def _construct_int(loader: yaml.SafeLoader, node: yaml.Node) -> int:
    value = loader.construct_scalar(node)
    if value.startswith("0o"):
        return int(value[2:], 8)
    if value.startswith("0x"):
        return int(value[2:], 16)
    return int(value, 10)


KBLoader.add_constructor(_INT, _construct_int)


class FrontMatterError(ValueError):
    pass


def load_yaml(text: str):
    return yaml.load(text, Loader=KBLoader)


def drop_nulls(value):
    """Recursively remove null mapping values and null list items: null means absent."""
    if isinstance(value, dict):
        return {k: drop_nulls(v) for k, v in value.items() if v is not None}
    if isinstance(value, list):
        return [drop_nulls(v) for v in value if v is not None]
    return value


def split_front_matter(text: str) -> tuple[dict, str]:
    """Split a record file into (front matter dict, markdown body)."""
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        raise FrontMatterError("file must start with a '---' front matter line")
    end = text.find("\n---", 3)
    if end == -1:
        raise FrontMatterError("front matter has no closing '---' line")
    after = text[end + 4 :]
    if after and not after.startswith("\n"):
        raise FrontMatterError("closing '---' must be on its own line")
    try:
        data = load_yaml(text[4:end])
    except yaml.YAMLError as exc:
        raise FrontMatterError(f"invalid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise FrontMatterError("front matter must be a YAML mapping")
    return data, after.lstrip("\n")
