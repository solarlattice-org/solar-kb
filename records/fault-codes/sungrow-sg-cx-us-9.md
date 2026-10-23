---
id: fc:sungrow-sg-cx-us-9
type: FaultCode
name: Sungrow SG-CX-US 009
aliases:
- '009'
- '9'
- Sungrow 009
- Grid underfrequency
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '009'
code_key: '9'
display_message: Grid underfrequency
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r2
    h: 097b3595b2db
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r2
    h: 097b3595b2db
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r2
    h: 097b3595b2db
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r2
    h: f9e97e4c8044
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r2
    h: 097b3595b2db
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r2
    h: f9e97e4c8044
  review: drafted
  review_note: 'support check: partial - Row is called a fault and requires contacting Sungrow, but the
    passages do not classify it explicitly as fault vs…'
- claim_id: c5
  rel: detected_by
  target: method:inverter-settings-review
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
- claim_id: c6
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
---
