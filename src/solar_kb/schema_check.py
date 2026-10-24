"""Structural validation of each record against the LinkML schema (closed world)."""
from __future__ import annotations

from pathlib import Path

from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

from solar_kb.records import TYPE_PREFIX, Record
from solar_kb.violation import Violation


class SchemaChecker:
    def __init__(self, schema_path: Path):
        # Merge the 0.5.0 modules once: given the path, linkml reloads every import for each record type it meets.
        view = SchemaView(str(schema_path))
        view.merge_imports()
        self._validator = Validator(view.schema, validation_plugins=[JsonschemaValidationPlugin(closed=True)])

    def check(self, record: Record) -> list[Violation]:
        rtype = record.type
        if rtype not in TYPE_PREFIX:
            return [
                Violation(
                    "schema", str(record.path), f"unknown record type {rtype!r}", record_id=record.id
                )
            ]
        report = self._validator.validate(record.data, rtype)
        return [
            Violation("schema", str(record.path), result.message, record_id=record.id)
            for result in report.results
        ]
