---
id: fc:sungrow-sg350hx-9
type: FaultCode
name: Sungrow SG350HX 009
aliases:
- '009'
- '9'
- Sungrow 009
- Grid Underfrequency
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '009'
code_key: '9'
display_message: Grid Underfrequency
page: 88
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=30.r2
    h: 372720d4ee1d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r2
    h: 097b3595b2db
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r2
    h: f9e97e4c8044
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r2
    h: 097b3595b2db
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r2
    h: f9e97e4c8044
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Row is called a fault and requires contacting Sungrow, but the
    passages do not classify it explicitly as fault vs…'
- claim_id: c4
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r2
    h: 097b3595b2db
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r2
    h: f9e97e4c8044
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r2
    h: 097b3595b2db
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r2
    h: f9e97e4c8044
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sungrow-sg350hx
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=30.r2
    h: 372720d4ee1d
  review: drafted
---
