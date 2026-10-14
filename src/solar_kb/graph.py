"""Build the SQLite graph (build/graph.sqlite) from a validated Corpus."""
from __future__ import annotations

import json
import re
import sqlite3
from pathlib import Path

from solar_kb.records import Corpus

SCHEMA_SQL = """
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE nodes (
    id TEXT PRIMARY KEY, type TEXT NOT NULL, name TEXT NOT NULL, status TEXT NOT NULL,
    layer TEXT NOT NULL, path TEXT NOT NULL, body TEXT NOT NULL, data_json TEXT NOT NULL
);
CREATE TABLE aliases (norm TEXT NOT NULL, id TEXT NOT NULL REFERENCES nodes(id));
CREATE TABLE claims (
    record_id TEXT NOT NULL REFERENCES nodes(id), claim_id TEXT NOT NULL,
    rel TEXT, attr TEXT, target TEXT, by_method TEXT, value_json TEXT,
    conditions TEXT, note TEXT, review TEXT NOT NULL,
    superseded_by TEXT, valid_from TEXT, valid_to TEXT, data_json TEXT NOT NULL,
    PRIMARY KEY (record_id, claim_id)
);
CREATE TABLE citations (
    record_id TEXT NOT NULL, claim_id TEXT NOT NULL, src TEXT NOT NULL, loc TEXT NOT NULL
);
CREATE INDEX claims_target ON claims(target);
CREATE INDEX claims_rel ON claims(rel);
CREATE INDEX aliases_norm ON aliases(norm);
"""


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def build_graph(corpus: Corpus, db_path: Path, kb_version: str) -> None:
    """Write a fresh graph database. Call only on a corpus with no violations."""
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = db_path.with_suffix(".tmp")
    tmp.unlink(missing_ok=True)
    con = sqlite3.connect(tmp)
    try:
        con.executescript(SCHEMA_SQL)
        con.execute("INSERT INTO meta VALUES ('kb_version', ?)", (kb_version,))
        for rid, record in sorted(corpus.records.items()):
            data = record.data
            con.execute(
                "INSERT INTO nodes VALUES (?,?,?,?,?,?,?,?)",
                (rid, record.type, data["name"], data.get("status", "active"), record.layer,
                 str(record.path), record.body, json.dumps(data, sort_keys=True)),
            )
            names = {data["name"], rid, rid.partition(":")[2], *data.get("aliases", [])}
            for norm in sorted({normalize(n) for n in names} - {""}):
                con.execute("INSERT INTO aliases VALUES (?,?)", (norm, rid))
            for claim in record.claims():
                con.execute(
                    "INSERT INTO claims VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (rid, claim["claim_id"], claim.get("rel"), claim.get("attr"),
                     claim.get("target"), claim.get("by"),
                     json.dumps(claim["value"]) if "value" in claim else None,
                     claim.get("conditions"), claim.get("note"), claim["review"],
                     claim.get("superseded_by"), claim.get("valid_from"), claim.get("valid_to"),
                     json.dumps(claim, sort_keys=True)),
                )
                for cite in claim["cite"]:
                    con.execute("INSERT INTO citations VALUES (?,?,?,?)",
                                (rid, claim["claim_id"], cite["src"], cite["loc"]))
        con.commit()
    finally:
        con.close()
    tmp.replace(db_path)
