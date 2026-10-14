from __future__ import annotations

import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCHEMA = REPO / "schema" / "solar_kb.yaml"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


def copy_fixture(tmp_path: Path, name: str) -> Path:
    """Copy tests/fixtures/<name> to tmp_path/<name> and return the copy's root."""
    dest = tmp_path / name
    shutil.copytree(FIXTURES / name, dest)
    return dest


def write_record(root: Path, type_dir: str, slug: str, front_matter: str, body: str = "") -> Path:
    path = root / "records" / type_dir / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{front_matter.strip()}\n---\n{body}", encoding="utf-8")
    return path


def rules_hit(violations) -> set[str]:
    return {v.rule for v in violations}
