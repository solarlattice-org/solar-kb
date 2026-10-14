# Records

One markdown file per entity: YAML front matter (validated against `schema/solar_kb.yaml`)
followed by original prose. File name = id slug; directory = type.

| Directory | Type | Id prefix |
|---|---|---|
| failure-modes | FailureMode | fm: |
| stressors | Stressor | stressor: |
| symptoms | Symptom | symptom: |
| measurements | Measurement | meas: |
| detection-methods | DetectionMethod | method: |
| mitigations | Mitigation | mit: |
| components | Component | comp: |
| sources | Source (also the public manifest entry) | src: |

`Case` and `DataExample` records live only in the private overlay.

Links in prose are Obsidian path links: `[[<directory>/<slug>|label]]`, e.g.
`[[detection-methods/el-imaging|EL imaging]]`. Open this `records/` folder as an Obsidian vault
and the graph view shows the same graph agents query.

Rules (enforced by `solar-kb validate`): every claim cites ≥1 source; public claims cite only
`open`/`reference` sources; numbers carry a QUDT unit and conditions; relation targets exist and
have the right type; `distinguished_from` names the DetectionMethod that tells the two apart;
every `[[link]]` in prose resolves.
