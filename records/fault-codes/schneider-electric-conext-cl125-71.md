---
id: fc:schneider-electric-conext-cl125-71
type: FaultCode
name: Schneider Electric CL125 071
aliases:
- '071'
- '71'
- Schneider Electric 071
- AC side SPD event
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '071'
code_key: '71'
display_message: AC side SPD event
page: 129
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r7
    h: 1b9733b511a6
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r6
    h: 7223c72001d3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:spd-alarm
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r6
    h: 7223c72001d3
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r7
    h: 1b9733b511a6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:surge-protection-device
  note: AC-side surge protector.
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r6
    h: 7223c72001d3
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r7
    h: 1b9733b511a6
  review: drafted
---
