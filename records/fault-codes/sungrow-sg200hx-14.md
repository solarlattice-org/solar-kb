---
id: fc:sungrow-sg200hx-14
type: FaultCode
name: Sungrow SG200HX 014
aliases:
- '014'
- '14'
- Sungrow 014
- Grid Overvoltage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: '014'
code_key: '14'
display_message: Grid Overvoltage
page: 88
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  note: Sustained overvoltage over a 10-minute window.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r2
    h: b3913e1065ce
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r2
    h: b3913e1065ce
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r2
    h: b3913e1065ce
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r2
    h: b3913e1065ce
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
  review_note: 'support check: partial - Escalation to service stated, but explicit fault classification
    is not stated.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r2
    h: b3913e1065ce
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Reconnection after grid normal implies disconnect, but production
    stop not explicit.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Repeated occurrence escalates to manufacturer service.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r2
    h: b3913e1065ce
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r2
    h: b3913e1065ce
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sungrow-sg200hx
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
---
