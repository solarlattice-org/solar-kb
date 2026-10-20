---
id: fc:sungrow-sg-cx-us-3
type: FaultCode
name: Sungrow SG-CX-US 3
aliases:
- '3'
- Sungrow 3
- Grid transient overvoltage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '3'
code_key: '3'
display_message: Grid transient overvoltage
page: 89
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r2
    h: 8a8b6ec00b3f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  note: Transient grid overvoltage.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r2
    h: 8a8b6ec00b3f
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
  review_note: 'support check: partial - Listed in a fault table but the passages never explicitly classify
    it as a fault rather than a warning.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r2
    h: 8a8b6ec00b3f
  review: drafted
  review_note: 'support check: partial - Reconnection after the grid normalizes implies a disconnection,
    but production stop is not explicit.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Contact service only if the fault repeats.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r2
    h: 8a8b6ec00b3f
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  review: drafted
---
