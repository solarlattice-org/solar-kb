---
id: fc:sungrow-sg250hx-2
type: FaultCode
name: Sungrow SG250HX 2
aliases:
- '2'
- Sungrow 2
- Grid Overvoltage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '2'
code_key: '2'
display_message: Grid Overvoltage
page: 90
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
  review_note: 'support check: partial - Passages list it as a fault code in a troubleshooting table,
    but no row explicitly classifies it as a fault…'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  review: drafted
  review_note: 'support check: partial - Inverter reconnects after grid normalizes implies it disconnected,
    but stopping production is not explicitly stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Reconnects when grid normalizes; if repeated, check grid and settings, then contact service.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  review: drafted
- claim_id: c8
  rel: affects
  target: comp:ac-cable
  note: Cable cross-section check when fault repeats.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:sungrow-sg250hx
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  review: drafted
---
