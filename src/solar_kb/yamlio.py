"""YAML loading with YAML 1.2-style scalars.

PyYAML's SafeLoader follows YAML 1.1: `yes`/`no`/`on`/`off` become booleans and
`2026-11-02` becomes a datetime.date. Both break schema validation (tdm_ok is the
string "yes"; dates are validated as strings), so this loader keeps them as strings
and only treats true/false as booleans.
"""
from __future__ import annotations

import re

import yaml

_BOOL = "tag:yaml.org,2002:bool"
_TIMESTAMP = "tag:yaml.org,2002:timestamp"


class KBLoader(yaml.SafeLoader):
    pass


KBLoader.yaml_implicit_resolvers = {
    first: [(tag, rx) for tag, rx in resolvers if tag not in (_BOOL, _TIMESTAMP)]
    for first, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
KBLoader.add_implicit_resolver(
    _BOOL, re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$"), list("tTfF")
)


class FrontMatterError(ValueError):
    pass


def load_yaml(text: str):
    return yaml.load(text, Loader=KBLoader)


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
