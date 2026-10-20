---
id: fc:sungrow-sg-cx-us-8
type: FaultCode
name: Sungrow SG-CX-US 8
aliases:
- '8'
- Sungrow 8
- Grid overfrequency
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '8'
code_key: '8'
display_message: Grid overfrequency
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r1
    h: 3e9d58d91341
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r1
    h: 3e9d58d91341
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
  review_note: 'support check: partial - The passages show it is a listed fault code in the troubleshooting
    table, but they give no explicit fault-versus-warning classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r1
    h: 3e9d58d91341
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  review: drafted
  review_note: 'support check: partial - The inverter reconnects after the grid returns to normal, which
    implies it disconnected, but the passages don''t explicitly say production stops.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Further checks only if the fault repeats.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r1
    h: 3e9d58d91341
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  review: drafted
---
