"""View models: plain data the templates print (site spec §3.4)."""
from __future__ import annotations

from dataclasses import dataclass

from solar_kb.records import Corpus
from solar_kb.site.paths import href, record_path


@dataclass(frozen=True)
class Ref:
    """A link as a template prints it. href None = plain text; proposed adds a *proposed* tag."""
    label: str
    href: str | None = None
    proposed: bool = False


def record_ref(corpus: Corpus, rid: str, page_path: str, fragment: str = "") -> Ref:
    record = corpus.records.get(rid)
    if record is None:
        return Ref(rid + (f"#{fragment}" if fragment else ""))
    label = record.data["name"] + (f" ({fragment})" if fragment else "")
    return Ref(label, href(page_path, record_path(rid), fragment), record.data.get("status") == "proposed")
