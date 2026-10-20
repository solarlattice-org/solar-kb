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
| fault-codes | FaultCode (one vendor code per make, model family and `code_key`) | fc: |
| event-concepts | EventConcept (a value on the event_class, production_effect or recovery axis) | ec: |
| sources | Source (also the public manifest entry) | src: |

`Case` and `DataExample` records live only in the private overlay.

A `FaultCode` has no prose: its id is `fc:<make>-<model_family>-<code_key>`, its only vendor text is the
short `display_message` and `vendor_severity`, and what it means is carried by claims (`reports`, `indicates`,
`has_event_class`, `has_production_effect`, `has_recovery`, `affects`, `detected_by`, `mitigated_by`,
`defined_in`) that cite the manual row. `EventConcept` records are hand-written vocabulary with a reading rule
in the body and carry no claims.

Links in prose are Obsidian path links: `[[<directory>/<slug>|label]]`, e.g.
`[[detection-methods/el-imaging|EL imaging]]`. Open this `records/` folder as an Obsidian vault
and the graph view shows the same graph agents query.

Rules (enforced by `solar-kb validate`): every claim cites ≥1 source, and every citation has
`src`, `loc` and `h` (the cited unit's content hash from the evidence layer); public claims cite only
`open`/`reference` sources; numbers carry a QUDT unit and conditions; relation targets exist and
have the right type; `distinguished_from` names the DetectionMethod that tells the two apart;
every `[[link]]` in prose resolves.
