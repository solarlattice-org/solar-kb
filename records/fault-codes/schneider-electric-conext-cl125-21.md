---
id: fc:schneider-electric-conext-cl125-21
type: FaultCode
name: Schneider Electric CL125 021
aliases:
- '021'
- '21'
- Schneider Electric 021
- PV input over current
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '021'
code_key: '21'
display_message: PV input over current
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r3
    h: 7ee05476d019
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r8
    h: 54a09f44ce42
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r3
    h: 7ee05476d019
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r8
    h: 54a09f44ce42
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r3
    h: 7ee05476d019
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r8
    h: 54a09f44ce42
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Check PV configuration and connections; contact support if it persists.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r3
    h: 7ee05476d019
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r8
    h: 54a09f44ce42
  review: drafted
---
