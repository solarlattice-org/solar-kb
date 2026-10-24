---
id: fc:sungrow-sg-cx-us-17
type: FaultCode
name: Sungrow SG-CX-US 017
aliases:
- '017'
- '17'
- Sungrow 017
- Grid voltage unbalance
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '017'
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
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r1
    h: e9dc9b740d24
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:phase-imbalance
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r1
    h: 921005be1f82
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: 'If repeated: measure grid, adjust parameter, then contact service.'
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r1
    h: 921005be1f82
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r1
    h: 921005be1f82
  review: drafted
  review_note: 'support check: partial - The inverter detects unbalanced three-phase voltage, but ''grid
    voltage measurement'' appears only as a manual troubleshooting step, not the detection method.'
- claim_id: c6
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r1
    h: 921005be1f82
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only when phase difference is within utility-permitted range.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r1
    h: 921005be1f82
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r1
    h: 3d7464a5ab51
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: verified
  review_note: 'support check: partial - The passages show it is a listed fault code in the troubleshooting
    table, but they give no explicit fault classification.'
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c9
  rel: applies_to
  target: prod:sungrow-sg-cx-us
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r1
    h: e9dc9b740d24
  review: drafted
---
