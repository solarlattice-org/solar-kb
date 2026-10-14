from __future__ import annotations

from pathlib import Path

from solar_kb.records import Corpus
from solar_kb.rules import ALL_RULES
from solar_kb.schema_check import SchemaChecker
from solar_kb.violation import Violation


def validate_corpus(corpus: Corpus, schema_path: Path) -> list[Violation]:
    """All violations: load errors, per-record schema errors, then semantic rules."""
    checker = SchemaChecker(schema_path)
    violations = list(corpus.load_errors)
    for record in corpus.records.values():
        violations += checker.check(record)
    for rule in ALL_RULES:
        violations += rule(corpus)
    return violations
