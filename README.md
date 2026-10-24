# Solar Lattice — solar-kb

Open, cited, typed knowledge about solar PV for people and AI agents.

Every fact here is a **claim** that cites the passage it came from, and carries a review state:
`drafted` (passed automated checks — a lead), `verified` (approved by a human — a fact) or
`disputed` (flagged, or conflicting with another claim — always surfaced, never silently used).
The prose is original; sources are cited by locator (section, page, table, figure, video timestamp),
never copied. Each citation also records `h`, a 12-hex-character hash of the cited text, so a revised
source can never silently re-point a citation at different text:
`{src: "src:iea-pvps-t13-01-2014", loc: "sec=4.3", h: "ff7ac62c1dc0"}`.

The one exception: a Requirement may quote the clause text of a code or standard verbatim, attributed by
`quote_source` (designator, edition, clause); that text stays its publisher's copyright (see `LICENSE-CONTENT`).

- `schema/solar_kb.yaml` — the LinkML schema (the open ontology), split into modules `schema/solar_kb_<module>.yaml`.
  Exports to JSON Schema, OWL, JSON-LD. Record types by module:
  - core: Source, Organization, Region, Role
  - failure: FailureMode, Stressor, Symptom, Measurement, DetectionMethod, Mitigation
  - equipment: Component, Product (family / model / variant), FirmwareRelease, Tool
  - events: FaultCode, EventConcept, OperatingState
  - control: Function, Parameter, GridProfile
  - communication: Protocol, Register
  - practice: Procedure, Hazard
  - regulation: Standard (an edition), Requirement (a clause), Program
  - engineering: Concept, Metric, CalculationMethod, Architecture
  - overlay (private): Case, DataExample

  Claims may carry a structured `scope` (products, firmware range, hardware revision, regions, applications,
  architecture, standard edition, dates) and `negated: true` for an explicit negative statement.
- `records/` — one markdown file per entity. Open `records/` as an Obsidian vault to browse the graph.
  Vendor fault codes (`fc:`) are records too: identity slots from the manual row, meaning as cited claims, no
  drafted prose (see `records/README.md`).
- `src/solar_kb/` — validator, graph build, queries (`resolve`, `resolve-code`, `neighbors`, `differential`), exports.

## Quick start

```bash
pip install -e ".[dev]"
solar-kb validate            # schema + rules; exits 1 on any violation
solar-kb build               # build/graph.sqlite + build/*.jsonld, *.ttl, *.schema.json
solar-kb query resolve "PID"
solar-kb query resolve-code "event 3501" --make sma   # a printed or spoken code -> fc: records
solar-kb query differential symptom:uniform-power-loss
solar-kb query differential fc:chint-sca-50-60ktl-isolationerr   # a code counts as the symptoms it reports
```

## Website

`solar-kb site --out _site` builds [solarlattice.org](https://solarlattice.org) from the public records: a page at
every record IRI (`https://solarlattice.org/kb/fm/pid`) and schema-term IRI (`https://solarlattice.org/kb/FailureMode`),
with the record's JSON-LD embedded in the page and alongside it (`/kb/fm/pid.jsonld`), plus the exports under `/kb/`.
Fault codes get their own pages (`/kb/fc/`, one table per make and family, a "Find a code" box over `/kb/fc/codes.json`).
It never reads the private overlay. `.github/workflows/pages.yml` deploys it on every push to `main`.
Install the extra first: `pip install -e ".[site]"`.

## Licenses

Code: Apache-2.0 (`LICENSE`). Schema and records: CC BY 4.0 (`LICENSE-CONTENT`).
