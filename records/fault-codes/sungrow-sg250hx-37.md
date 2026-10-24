---
id: fc:sungrow-sg250hx-37
type: FaultCode
name: Sungrow SG250HX 37
aliases:
- '37'
- Sungrow 37
- Excessively High Ambient Temperature
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '37'
code_key: '37'
display_message: Excessively High Ambient Temperature
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r2
    h: 89539eb66012
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r2
    h: 89539eb66012
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r1
    h: fb5c20da466e
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r2
    h: 89539eb66012
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r1
    h: fb5c20da466e
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r2
    h: 89539eb66012
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r1
    h: fb5c20da466e
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r2
    h: 89539eb66012
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r1
    h: fb5c20da466e
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:fan-replacement
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r2
    h: 89539eb66012
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r1
    h: fb5c20da466e
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r2
    h: 89539eb66012
  review: drafted
  review_note: 'support check: partial - The row doesn''t state a fault or warning classification, but
    the inverter resuming operation implies it was stopped.'
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r2
    h: 89539eb66012
  review: drafted
  review_note: 'support check: partial - The row says the inverter resumes operation once the temperature
    is normal, which implies it stopped, but it never explicitly…'
- claim_id: c10
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes when temperature normalizes; site checks and service only if it persists.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r2
    h: 89539eb66012
  review: drafted
- claim_id: c11
  rel: applies_to
  target: prod:sungrow-sg250hx
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r2
    h: 89539eb66012
  review: drafted
---
