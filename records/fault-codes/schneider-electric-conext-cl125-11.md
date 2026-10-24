---
id: fc:schneider-electric-conext-cl125-11
type: FaultCode
name: Schneider Electric CL125 011
aliases:
- '011'
- '11'
- Schneider Electric 011
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '011'
code_key: '11'
page: 124
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r5
    h: f41d6b0d52db
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r5
    h: 913c8a6f3028
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-injection-high
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r5
    h: f41d6b0d52db
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r5
    h: 913c8a6f3028
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Recovers within minutes; persistent events go to technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r5
    h: f41d6b0d52db
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r5
    h: 913c8a6f3028
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r5
    h: f41d6b0d52db
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r5
    h: 913c8a6f3028
  review: drafted
---
