---
id: fc:schneider-electric-conext-cl125-5
type: FaultCode
name: Schneider Electric CL125 005
aliases:
- '005'
- '5'
- Schneider Electric 005
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '005'
code_key: '5'
page: 123
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r4
    h: 62c01cc007dd
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r4
    h: ea1a3e0da599
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r4
    h: 62c01cc007dd
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r4
    h: ea1a3e0da599
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Contact technical support if the event persists.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r4
    h: 62c01cc007dd
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r4
    h: ea1a3e0da599
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r4
    h: 62c01cc007dd
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r4
    h: ea1a3e0da599
  review: drafted
---
