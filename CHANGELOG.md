# Changelog

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
