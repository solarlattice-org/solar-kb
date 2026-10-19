"""The fault-code key grammar (Plan 4d). A FaultCode id ends in `code_key(code)`, the graph's `fault_codes`
table stores it, and `Graph.resolve_code` normalizes a technician's spelling with the same rules.

Copied verbatim from solar-brain `solar_brain/faults/codes.py` (parse_code, query_code); the two copies are kept
equal by tests in both repos, so a key computed by the compiler is the key the public graph looks up."""
from __future__ import annotations

import re
from dataclasses import dataclass

_CODE = re.compile(r"([a-z]*)-?(\d+)(?:-(\d+))?")
_FILLER = re.compile(r"^\s*(?:(?:(?:event|error|alarm|code|no|number|nr|id)\b\.?|#)\s*)+", re.I)


@dataclass(frozen=True)
class CodeKey:
    key: str
    prefix: str
    number: int | None
    number_end: int | None


def parse_code(code: str) -> CodeKey:
    """Normalize a printed code for lookup: case, spaces and zero padding never matter."""
    s = re.sub(r"\s+", "", code).lower()
    m = _CODE.fullmatch(s)
    if m:
        prefix, start = m.group(1), int(m.group(2))
        end = int(m.group(3)) if m.group(3) else None
        return CodeKey(f"{prefix}{start}" + (f"-{end}" if end is not None else ""), prefix, start, end)
    return CodeKey(re.sub(r"[^a-z0-9]", "", s), "", None, None)


def query_code(text: str) -> CodeKey:
    """A user's spelling ("event 3501", "Error no. 0104"): generic filler words go, vendor prefixes stay."""
    return parse_code(_FILLER.sub("", text.strip()))


def code_key(code: str) -> str:
    """The id/lookup key of a printed code: "Protect0090" -> "protect90", "6002-6412" -> "6002-6412"."""
    return parse_code(code).key
