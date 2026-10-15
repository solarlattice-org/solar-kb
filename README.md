# Solar Lattice — solar-kb

Open, cited, typed knowledge about solar PV for people and AI agents.

Every fact here is a **claim** that cites the passage it came from, and carries a review state:
`drafted` (passed automated checks — a lead), `verified` (approved by a human — a fact) or
`disputed` (flagged, or conflicting with another claim — always surfaced, never silently used).
The prose is original; sources are cited by locator (section, page, table, figure, video timestamp),
never copied. Each citation also records `h`, a 12-hex-character hash of the cited text, so a revised
source can never silently re-point a citation at different text:
`{src: "src:iea-pvps-t13-01-2014", loc: "sec=4.3", h: "ff7ac62c1dc0"}`.

- `schema/solar_kb.yaml` — the LinkML schema (the open ontology). Exports to JSON Schema, OWL, JSON-LD.
- `records/` — one markdown file per entity. Open `records/` as an Obsidian vault to browse the graph.
- `src/solar_kb/` — validator, graph build, queries (`resolve`, `neighbors`, `differential`), exports.

## Quick start

```bash
pip install -e ".[dev]"
solar-kb validate            # schema + rules; exits 1 on any violation
solar-kb build               # build/graph.sqlite + build/*.jsonld, *.ttl, *.schema.json
solar-kb query resolve "PID"
solar-kb query differential symptom:uniform-power-loss
```

## Licenses

Code: Apache-2.0 (`LICENSE`). Schema and records: CC BY 4.0 (`LICENSE-CONTENT`).
