---
id: fc:sungrow-sg250hx-9
type: FaultCode
name: Sungrow SG250HX 9
aliases:
- '9'
- Sungrow 9
- Grid Underfrequency
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '9'
code_key: '9'
display_message: Grid Underfrequency
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r2
    h: 22c6c28d3439
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r2
    h: 22c6c28d3439
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r2
    h: 097b3595b2db
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r2
    h: 22c6c28d3439
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
  review_note: 'support check: partial - The passages show it is a listed fault code in the troubleshooting
    table, but they give no explicit fault classification.'
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r2
    h: 22c6c28d3439
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:grid-settings-check
  note: Contact service if grid and settings are ruled out.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r2
    h: 22c6c28d3439
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r2
    h: 097b3595b2db
  review: drafted
---
