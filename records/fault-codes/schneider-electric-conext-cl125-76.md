---
id: fc:schneider-electric-conext-cl125-76
type: FaultCode
name: Schneider Electric CL125 076
aliases:
- '076'
- '76'
- Schneider Electric 076
- PV overload condition
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '076'
code_key: '76'
display_message: PV overload condition
page: 130
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r3
    h: 44cf211d1a75
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=34.r1
    h: 5f40bd979e1d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:pv-input-overload
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r3
    h: 44cf211d1a75
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=34.r1
    h: 5f40bd979e1d
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r3
    h: 44cf211d1a75
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=34.r1
    h: 5f40bd979e1d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r3
    h: 44cf211d1a75
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=34.r1
    h: 5f40bd979e1d
  review: drafted
---
