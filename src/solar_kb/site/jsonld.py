"""Per-record JSON-LD documents, and embedding them safely in HTML (site spec §2.3)."""
from __future__ import annotations

import json

from solar_kb.export import record_node
from solar_kb.records import Record

CONTEXT_URL = "https://solarlattice.org/kb/solar_kb.context.jsonld"


def record_document(record: Record, prefixes: dict[str, str], context: str | dict = CONTEXT_URL) -> dict:
    """The record as a standalone JSON-LD document. The site references the published context by URL; tests pass
    the context itself so that parsing needs no network."""
    return {"@context": context, **record_node(record, prefixes)}


def to_json(doc: dict) -> str:
    return json.dumps(doc, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def script_json(doc: dict) -> str:
    """JSON for a <script type="application/ld+json"> block. Every '<' is written as \\u003c, so prose containing
    '</script>' cannot end the block early; JSON parsers read it back unchanged."""
    return json.dumps(doc, sort_keys=True, ensure_ascii=False).replace("<", "\\u003c")
