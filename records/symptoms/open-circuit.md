---
id: symptom:open-circuit
type: Symptom
name: Open string circuit
aliases:
- OC substrings
- open-circuited
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-warm-substring
  note: Open-circuited substrings or module strings show up warmer than active ones in thermography taken
    under load. Seen in batches of modules with cold solder joints in the outer junction box.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: fig=43
    h: 2e3076402aaa
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=23.r2
    h: 007cda150de8
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - Passages say OC substrings appear hotter in IRT and are seen
    from cold solder joints in outer junction box batches, but ''under load'' and the ''neighbouring modules
    under same irradiance'' conditions are not stated.'
- claim_id: c2
  attr: temperature_rise
  value:
    min: 5
    max: 10
    unit: unit:K
  conditions: Open-circuited substrings or module strings compared with active strings during IR thermography
    inspection
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: fig=43
    h: 2e3076402aaa
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:low-voc
  note: An open-circuited substring loses its power and lowers module Voc.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=23.r2
    h: 007cda150de8
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Passage says open sub-string loses power and Voc is reduced,
    but does not mention string voltage or module voltage comparison against peers.'
- claim_id: c4
  rel: observed_as
  target: meas:production-loss-alarm
  note: Monitoring tools may flag a performance loss when a junction box failure leaves an open-circuit
    configuration.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Monitoring tools might detect performance loss from open-circuit
    configurations is stated, but string current dropping to zero and DC power falling at constant irradiance
    are not specified.'
---
An open circuit is a break in the current path of a module substring, a whole module or a full string, so that part stops producing. Common causes are connector defects, damaged DC cables and junction box failures, including cold solder joints and loose or corroded contacts. In IR thermography under load, an open substring or module string looks warmer than the active strings. A full string loss can be seen this way too, but the faulty module can stay hard to locate. Electrically, an open substring loses its power and lowers module Voc. A string Voc check against identical strings or the expected value also catches missing interconnections. In monitoring data, look for a loss in performance and compare string currents to find the string that is underperforming. To tell the causes apart, first inspect connectors and cables visually and by touch under safe isolation. Then check junction boxes for burn marks, open lids or detachment, and use IR to find hot connections. If an open circuit traces back to the junction box, replacing the module is advised because repairs may start new fires.

<!-- review notes
- sentence 1: support check: partial - Passages describe open-circuited module/cell strings and substring power loss, but do not define an open circuit as a break in the current path; it is mostly implied.
- sentence 4: support check: partial - Substring power loss and Voc reduction are stated, and string Voc comparison catches missing interconnections, though the latter is about missing module interconnections in strings rather than open substrings specifically.
- sentence 6: support check: partial - Visual/tactile inspection under isolation and IR are supported, and junction box visual/thermal inspection is stated, but the sequencing and specific checks for burn marks, open lids or detachment are only partly in the passages, though lid defects and burnt boxes are mentioned.
-->
