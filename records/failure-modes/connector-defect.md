---
id: fm:connector-defect
type: FailureMode
name: Connector Defect
claims:
- claim_id: c1
  rel: affects
  target: comp:dc-connector
  note: MC4 is the most common type. Connectors join modules to each other and to combiner boxes, fuse
    boxes or inverters.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=h4
    h: 3be1d95ede61
  - src: src:pv-root-cause-connector-defect
    loc: sec=h3
    h: b866045455bd
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:installation-error
  note: Sources say failures are most likely linked to installation issues, for example connectors not
    fitted according to the instructions.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=h4
    h: 3be1d95ede61
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r3
    h: 091be96f279b
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r3
    h: 091be96f279b
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:connector-mismatch
  note: Connectors sold as 'compatible' can seal less well against water and vapour, or use materials
    that do not match. This happens mostly at string ends with extension cables, or at the inverter or
    combiner box.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=h4
    h: 3be1d95ede61
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r3
    h: 091be96f279b
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r3
    h: 091be96f279b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=26.r3
    h: 01a24e3b5d2a
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=44.r3
    h: 7a134889c7e8
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:improper-crimping
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=h4
    h: 3be1d95ede61
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r3
    h: 091be96f279b
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r3
    h: 091be96f279b
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:low-quality-material
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=h4
    h: 3be1d95ede61
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r3
    h: 091be96f279b
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r3
    h: 091be96f279b
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c6
  rel: caused_by
  target: stressor:moisture-exposure
  note: This includes rain or dirt getting in before installation, and badly fixed connectors that stay
    wet without drying out.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=h4
    h: 3be1d95ede61
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r3
    h: 091be96f279b
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r3
    h: 091be96f279b
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c7
  rel: caused_by
  target: stressor:component-aging
  note: Corrosion after long weather exposure to UV and humidity. Sources rank this as less likely than
    installation issues.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=h4
    h: 3be1d95ede61
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c8
  rel: leads_to
  target: fm:arc-fault
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  - src: src:pv-root-cause-connector-defect
    loc: sec=h4
    h: 3be1d95ede61
  review: drafted
- claim_id: c9
  rel: leads_to
  target: fm:insulation-loss
  note: Low insulation faults can come and go as humidity changes.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=h3
    h: b866045455bd
  - src: src:pv-root-cause-connector-defect
    loc: sec=h6
    h: e7691a95e9d7
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:burn-marks
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: fig=1
    h: 4e82f7c0b6b2
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:melted-component
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c12
  rel: presents_as
  target: symptom:cracked-housing
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  review: drafted
- claim_id: c13
  rel: presents_as
  target: symptom:contact-corrosion
  note: Seen once the connector is opened.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  review: drafted
- claim_id: c14
  rel: presents_as
  target: symptom:hotspot-ir-image
  note: Often visible early, before other signs.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  - src: src:pv-root-cause-connector-defect
    loc: sec=h6
    h: e7691a95e9d7
  review: drafted
- claim_id: c15
  rel: presents_as
  target: symptom:series-resistance-increase
  note: First phase of failure. The rise may be too small to detect electrically or visually.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=h6
    h: e7691a95e9d7
  review: drafted
- claim_id: c16
  rel: presents_as
  target: symptom:ground-fault
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h4
    h: 3be1d95ede61
  - src: src:pv-root-cause-connector-defect
    loc: sec=h6
    h: e7691a95e9d7
  review: drafted
- claim_id: c17
  rel: presents_as
  target: symptom:open-circuit
  note: Final phase, when the connector has burst.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h3
    h: b866045455bd
  - src: src:pv-root-cause-connector-defect
    loc: sec=h6
    h: e7691a95e9d7
  review: drafted
- claim_id: c18
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r2
    h: a141b04a3d40
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=44.r2
    h: fa398a15890a
  - src: src:pv-root-cause-connector-defect
    loc: sec=h6
    h: e7691a95e9d7
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r2
    h: a141b04a3d40
  review: drafted
- claim_id: c19
  rel: detected_by
  target: method:tactile-inspection
  note: Only with the circuit safely isolated.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  review: drafted
- claim_id: c20
  rel: detected_by
  target: method:ir-thermography
  note: Done under load. It picks up early symptoms.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r2
    h: a141b04a3d40
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  - src: src:pv-root-cause-connector-defect
    loc: sec=h6
    h: e7691a95e9d7
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r2
    h: a141b04a3d40
  review: drafted
- claim_id: c21
  rel: detected_by
  target: method:string-current-measurement
  note: Compare currents between strings.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  review: drafted
- claim_id: c22
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  review: drafted
- claim_id: c23
  rel: mitigated_by
  target: mit:connector-replacement
  note: Replace connectors that are damaged or mismatched.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  review: drafted
- claim_id: c24
  rel: mitigated_by
  target: mit:correct-crimping
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  review: drafted
- claim_id: c25
  rel: mitigated_by
  target: mit:connector-compatibility-check
  note: Check that connector types match across repaired circuits.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c26
  rel: mitigated_by
  target: mit:proper-installation
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=h6
    h: e7691a95e9d7
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
  review_note: 'support check: partial - Passage emphasizes need for proper installation to prevent damage,
    but it is a generic statement rather than a stated mitigation for this defect in detail.'
- claim_id: c27
  rel: mitigated_by
  target: mit:regular-maintenance
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=h6
    h: e7691a95e9d7
  review: drafted
  review_note: 'support check: partial - Regular maintenance is mentioned as needed to prevent long-term
    damage, though only generally.'
---
A connector defect is a damaged or badly made DC connection between modules, or between modules and combiner boxes or inverters. It can cause resistive heating, open circuits, ground faults, arcing and fire. Most cases come from installation problems: poor crimping, joining different connector types, or using low-quality parts. Aging and corrosion from weather play a smaller role. Look for connectors that are melted, burned, brittle, cracked or whitened. Opened connectors may show corrosion. In the early stage the only sign is often heat at the connector, which shows as a hotspot on an infrared scan under load. Later on, the connector may cause intermittent insulation faults, a ground fault, or burst open and break the string circuit. To confirm, use visual and tactile checks with the circuit safely isolated, infrared inspection, string current comparison and insulation resistance testing. Replace damaged or mismatched connectors, fix crimping and installation errors, and check that connector types match across every repaired circuit.

<!-- review notes
- sentence 4: support check: partial - Early hot spots under thermography are stated, but 'only sign' and 'under load' are not explicitly supported (the latter is in the summary metadata only).
-->
