---
id: fc:schneider-electric-conext-cl125-7
type: FaultCode
name: Schneider Electric CL125 007
aliases:
- '007'
- '7'
- Schneider Electric 007
- Transient AC over current
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '007'
code_key: '7'
display_message: Transient AC over current
page: 124
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r1
    h: cf7aec938656
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r1
    h: 2a565762793b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-overcurrent
  note: Transient overcurrent.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r1
    h: cf7aec938656
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r1
    h: 2a565762793b
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Recovers within minutes; persistent events go to technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r1
    h: cf7aec938656
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r1
    h: 2a565762793b
  review: drafted
---
