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
