---
id: fc:schneider-electric-conext-cl125-44
type: FaultCode
name: Schneider Electric CL125 044
aliases:
- '044'
- '44'
- Schneider Electric 044
- DC/AC inversion circuit event
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '044'
code_key: '44'
display_message: DC/AC inversion circuit event
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r2
    h: 7b83c6bbf6ad
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r9
    h: b839c2541aec
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r2
    h: 7b83c6bbf6ad
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r9
    h: b839c2541aec
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r2
    h: 7b83c6bbf6ad
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r9
    h: b839c2541aec
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, escalate to technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r2
    h: 7b83c6bbf6ad
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r9
    h: b839c2541aec
  review: drafted
---
