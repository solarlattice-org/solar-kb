---
id: fc:schneider-electric-conext-cl125-13
type: FaultCode
name: Schneider Electric CL125 013
aliases:
- '013'
- '13'
- Schneider Electric 013
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '013'
code_key: '13'
page: 125
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r2
    h: c05cac074a82
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r1
    h: 6f599899013a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-voltage-out-of-range
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r2
    h: c05cac074a82
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r1
    h: 6f599899013a
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r2
    h: c05cac074a82
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r1
    h: 6f599899013a
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Recovers within minutes; persistent events go to technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r2
    h: c05cac074a82
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r1
    h: 6f599899013a
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r2
    h: c05cac074a82
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r1
    h: 6f599899013a
  review: drafted
---
