---
id: fc:sungrow-sg-cx-us-14
type: FaultCode
name: Sungrow SG-CX-US 014
aliases:
- '014'
- '14'
- Sungrow 014
- 10-minute grid overvoltage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '014'
code_key: '14'
display_message: 10-minute grid overvoltage
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r2
    h: b3913e1065ce
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r2
    h: b3913e1065ce
  review: drafted
- claim_id: c3
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
  review: drafted
- claim_id: c4
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
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r2
    h: b3913e1065ce
  review: drafted
  review_note: 'support check: partial - Reconnection after grid normal implies disconnect, but production
    stop not explicit.'
- claim_id: c6
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
---
