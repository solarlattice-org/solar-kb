---
id: fc:sungrow-sg200hx-13
type: FaultCode
name: Sungrow SG200HX 013
aliases:
- '013'
- '13'
- Sungrow 013
- Grid Abnormal
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: '013'
code_key: '13'
display_message: Grid Abnormal
page: 89
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r5
    h: 40e95c363a32
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-voltage-out-of-range
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r1
    h: 3f4642d9acdb
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c3
  rel: reports
  target: symptom:grid-frequency-out-of-range
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r1
    h: 3f4642d9acdb
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r1
    h: 3f4642d9acdb
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r5
    h: 40e95c363a32
  review: drafted
  review_note: 'support check: partial - Cannot connect to grid and service contact is stated, but explicit
    fault classification is not.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r1
    h: 3f4642d9acdb
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r5
    h: 40e95c363a32
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r1
    h: 3f4642d9acdb
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r5
    h: 40e95c363a32
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r1
    h: 3f4642d9acdb
  review: drafted
  review_note: 'support check: partial - Measuring the actual grid frequency is a check step; not stated
    as detection method.'
- claim_id: c8
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r1
    h: 3f4642d9acdb
  review: drafted
---
