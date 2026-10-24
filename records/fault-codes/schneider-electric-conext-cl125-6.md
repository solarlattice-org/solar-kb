---
id: fc:schneider-electric-conext-cl125-6
type: FaultCode
name: Schneider Electric CL125 006
aliases:
- '006'
- '6'
- Schneider Electric 006
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '006'
code_key: '6'
page: 123
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r5
    h: e0137487ea1d
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r5
    h: 4f63f2ad340a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r5
    h: e0137487ea1d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r5
    h: 4f63f2ad340a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r5
    h: e0137487ea1d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r5
    h: 4f63f2ad340a
  review: drafted
  review_note: 'support check: partial - Resumes operation implies it stopped, but a trip is not explicitly
    stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes once current drops below limit; persistent events go to technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r5
    h: e0137487ea1d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r5
    h: 4f63f2ad340a
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r5
    h: e0137487ea1d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r5
    h: 4f63f2ad340a
  review: drafted
---
