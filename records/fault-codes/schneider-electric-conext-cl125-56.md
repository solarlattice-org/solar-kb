---
id: fc:schneider-electric-conext-cl125-56
type: FaultCode
name: Schneider Electric CL125 056
aliases:
- '056'
- '56'
- Schneider Electric 056
- Inverter leakage current redundancy event is detected.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '056'
code_key: '56'
display_message: Inverter leakage current redundancy event is detected.
page: 129
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r3
    h: e09edb18d925
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r2
    h: c2a216bfed40
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r3
    h: e09edb18d925
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r2
    h: c2a216bfed40
  review: drafted
  review_note: 'support check: partial - Leakage current redundancy event is stated, but ''high'' is implied
    only.'
- claim_id: c4
  rel: affects
  target: comp:pv-array
  note: Check PV strings for a ground fault.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r3
    h: e09edb18d925
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r2
    h: c2a216bfed40
  review: drafted
---
