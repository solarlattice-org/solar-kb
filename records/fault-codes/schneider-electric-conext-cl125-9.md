---
id: fc:schneider-electric-conext-cl125-9
type: FaultCode
name: Schneider Electric CL125 009
aliases:
- '009'
- '9'
- Schneider Electric 009
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '009'
code_key: '9'
page: 124
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r3
    h: 1b966c7b1528
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r3
    h: 06287a06189c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r3
    h: 1b966c7b1528
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r3
    h: 06287a06189c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r3
    h: 1b966c7b1528
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r3
    h: 06287a06189c
  review: drafted
  review_note: 'support check: partial - The grid frequency check is implied by the solution, but the
    passage doesn''t explicitly say to measure it (the ''Measure''…'
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: When frequency is outside range; if within range and persisting, escalate to technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r3
    h: 1b966c7b1528
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r3
    h: 06287a06189c
  review: drafted
---
