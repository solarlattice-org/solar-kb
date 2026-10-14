from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Violation:
    rule: str
    path: str
    message: str
    record_id: str | None = None
    claim_id: str | None = None

    def __str__(self) -> str:
        where = self.record_id or self.path
        if self.claim_id:
            where += f"#{self.claim_id}"
        return f"[{self.rule}] {where}: {self.message}"
