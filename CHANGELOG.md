# Changelog

## 0.4.0 (unreleased)

Plan 4d step FC0 (a): fault-code records from manufacturer manuals. Additive: every 0.3.0 record validates unchanged.

### Schema
- Two record types. `FaultCode` (`records/fault-codes/`, prefix `fc:`): one record per make, model family and
  `code_key`, with the deterministic slots `make`, `make_name`, `model_family`, `family_name`, `code`, `code_key`,
  `code_from`/`code_to` (printed ranges), `display_message` (≤ 8 words), `vendor_severity` (≤ 3 words) and `page`.
  `EventConcept` (`records/event-concepts/`, prefix `ec:`): a value on one fault-event axis, slot `axis`
  (enum `EventAxis`: `event_class`, `production_effect`, `recovery`).
- Six relations: `reports` (FaultCode → Symptom), `indicates` (→ FailureMode), `has_event_class`,
  `has_production_effect`, `has_recovery` (→ EventConcept) and `defined_in` (→ Source, citing the defining row).
  `affects`, `detected_by` and `mitigated_by` now also accept a FaultCode as their source.
- Prefixes `fc:` (`https://solarlattice.org/kb/fc/`) and `ec:` (`https://solarlattice.org/kb/ec/`).

### Records
- Ten `ec:` concepts, each with a reading rule in its body: fault / warning / informational; trip / derate /
  no-production-effect; auto-reset / auto-reset-limited / manual-reset / service-required. A collapsed 3/3/4
  vocabulary (Phase 3 had 5/3/5): manuals do not separate alarm from warning or remote from on-site reset
  consistently; the vendor's own word survives in `vendor_severity`. Adding a concept is adding a record.
- The seed vocabulary for fault-code compilation: 38 `proposed` stubs (24 Symptom, 6 FailureMode, 8 Mitigation)
  so every make maps onto the same ids.

### Validation
- New rule `fault-code`: the id is recomputed from `make`, `model_family` and `code_key` and must match;
  `code_key == solar_kb.codes.code_key(code)`; `code_from`/`code_to` are present exactly when `parse_code(code)`
  sees a printed range (a hyphenated single code such as `CRIT-4` or `OV-G-V` takes none), ordered and equal to the
  printed bounds; `name` is `{make_name} … {code}` and ≤ 8 words, every alias ≤ 8 words, `display_message` ≤ 8 words
  and `vendor_severity` ≤ 3 (the only vendor text a public code carries); the body is empty apart from HTML
  comments; no claim carries `quote`; `note`, `conditions` and `review_note` ≤ 25 words; at least one `defined_in`
  claim, one per source, each citation pointing into its own target at a table row (`tbl=N.rM`), table (`tbl=N`)
  or heading unit (`sec=hK`); at most one non-disputed claim per axis; the only quantity is `output_limit`, a
  single `nominal` or `max` in `unit:PERCENT`, `unit:KiloW` or `unit:W`, allowed only with a
  `has_production_effect → ec:derate` claim and with `conditions` starting `basis=rated_power|current_power|absolute`.
- New rule `event-axes`: `has_event_class` / `has_production_effect` / `has_recovery` point at an EventConcept on
  that axis; an EventConcept carries no claims.

### Graph and queries
- `graph.sqlite` gains `fault_codes(record_id, make, model_family, code_key, code_from, code_to)`.
- `Graph.resolve_code(text, make, family)` and `solar-kb query resolve-code`: a printed or spoken code
  ("3701", "event 3501", "Error no. 0104", "Protect0090") → FaultCode records, in the v1 lookup order (exact
  `code_key`, then a printed range containing the number under the same vendor prefix, then the bare number),
  ranked by make match then family match.
- `differential` accepts `fc:` observations and expands each through its `reports` claims (at or above
  `min_review`) into Symptoms before ranking, reported in `via_code`; `indicates` is never scored, so §8.1 scoring
  is unchanged. Nothing vanishes in the expansion: a reported Symptom that is only a proposed stub is listed in
  `unknown_observations` as it would be when given directly, a disputed `reports` claim below the floor is a
  `disputed_matches` entry (`failure_mode` null, `symptom` the target), and a code that reports nothing at the floor
  is itself an unknown observation. The result also carries `known_observations` (the Symptom/Measurement ids that
  were scored). The benchmark accepts `{id: fc:...}` observations and derives its `unresolved` reason from
  `known_observations`, so a pinned code the KB cannot use is a KB gap, never a ranking miss.
- `solar_kb.codes`: `code_key`, `parse_code`, `query_code`, copied from solar-brain and equality-tested so the
  compiler's key is the key the public graph looks up.

### Website
- Fault-code pages (`kb/fc/<make>-<family>-<code_key>`): breadcrumb Fault codes › make › family; Shown as, Vendor
  severity and Page; a card of Class / Production / Clears badges linking to the concept pages, each with its
  claim's review badge ("reduced to 50 % of rated power" when an `output_limit` is stated); a deterministic Decoded
  sentence built from the `reports`, `indicates`, `affects`, `detected_by` and `mitigated_by` claims; the derived
  differential for the reported symptom (failure modes presenting it, the tests that tell them apart); Defined in
  (source, publisher and edition, locator and hash, and the fixed sentence that the manufacturer's cause and
  corrective text is not reproduced); same condition on other equipment (by make) and same code in other families.
  A record with only `defined_in` says "The manual lists this code without further explanation."
- `kb/fc/` lists makes with code counts and families, with a "Find a code" box (`static/fc-lookup.js`, dependency-free
  progressive enhancement over `kb/fc/codes.json`, also in Downloads); `kb/fc/<make>` has one table per family
  (Code | Shown as | Class | Production | Clears | Reports | Page) sorted by vendor prefix and number, filterable
  with the same code-key grammar; an axis whose only claims are a disputed pair shows every contested value with a
  disputed marker, never the first as settled. EventConcept pages list their referencing codes in a table grouped
  by make. A code page prints its page number on the Defined-in line only while one source defines the code (the
  meta row always carries it), since `page` belongs to one defining unit.
  Former `fc:`/`ec:` ids in `aliases` get redirect stubs like any record.

## 0.3.0 (unreleased)

### Schema
- The `src` slot (a citation's source) now has the IRI `kb:cites_source`. Its old IRI `kb:src` clashed with the
  Source namespace `https://solarlattice.org/kb/src/`. Records are unchanged: citations still use the key `src`.
- The enum `Tier` is renamed `SourceTier`, so no two term IRIs differ only by case (`tier` is a slot). Records
  are unchanged.

### Exports
- The OWL export honours `slot_uri` (`use_native_uris=False`). `close_mappings` and `exact_mappings` are now
  `skos:closeMatch` and `skos:exactMatch`, as in the JSON-LD context.
- JSON-LD writes identifier fields as absolute IRIs typed `@id`, so relation targets, `by`, citation sources,
  claim references and units are links between nodes. Source records get their correct IRIs
  (`https://solarlattice.org/kb/src/<slug>`; before, `src:<slug>`).
- `solar_kb.context.jsonld` is now the exact context `records.jsonld` uses.
- Each claim is a JSON-LD node with its claim IRI (`https://solarlattice.org/kb/fm/pid#c3`), so `superseded_by` and
  `conflicts_with` link to real nodes.

### Validation
- New rule `mapping-prefixes`: a `close_mappings`/`exact_mappings` entry is an absolute http(s) IRI or uses a
  prefix the schema declares.

### Website
- `solar-kb site --out _site` builds solarlattice.org: a page at every record and schema-term IRI, per-record
  JSON-LD, and the exports. `.github/workflows/pages.yml` deploys it on every push to `main`.
- Record pages show the record's status; wikilinks to `proposed` stubs carry the *proposed* tag.
- Markdown images in record prose render as links, so no third-party content loads with a page.
- Build errors name the record or alias behind a colliding path; only a missing `[site]` extra gets the
  install hint.
