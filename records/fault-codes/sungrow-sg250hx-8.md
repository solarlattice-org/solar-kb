---
id: fc:sungrow-sg250hx-8
type: FaultCode
name: Sungrow SG250HX 8
aliases:
- '8'
- Sungrow 8
- Grid Overfrequency
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '8'
code_key: '8'
display_message: Grid Overfrequency
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r1
    h: 3e9d58d91341
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
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c7
  rel: applies_to
  target: prod:sungrow-sg250hx
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r1
    h: 3e9d58d91341
  review: drafted
---
