---
id: fc:sungrow-sg-cx-us-17
type: FaultCode
name: Sungrow SG-CX-US 17
aliases:
- '17'
- Sungrow 17
- Grid voltage unbalance
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '17'
code_key: '17'
display_message: Grid voltage unbalance
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:phase-imbalance
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r1
    h: 3d7464a5ab51
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r1
    h: 3d7464a5ab51
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
  review_note: 'support check: partial - The passages show it is a listed fault code in the troubleshooting
    table, but they give no explicit fault classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r1
    h: 3d7464a5ab51
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  review: drafted
  review_note: 'support check: partial - Reconnection after the grid returns to normal implies the inverter
    disconnected, but the passages don''t explicitly state that production stops.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: If repeated, measure phases, adjust imbalance parameter if within limits, then service.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r1
    h: 3d7464a5ab51
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r1
    h: 3d7464a5ab51
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only when phase difference is within utility-permitted range.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r1
    h: 3d7464a5ab51
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  review: drafted
---
