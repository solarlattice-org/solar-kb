---
id: fc:schneider-electric-conext-cl125-12
type: FaultCode
name: Schneider Electric CL125 012
aliases:
- '012'
- '12'
- Schneider Electric 012
- Residual current leakagedetected is high.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '012'
code_key: '12'
display_message: Residual current leakagedetected is high.
page: 125
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r1
    h: e0fa32436489
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r6
    h: f7dcd0f40d75
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r1
    h: e0fa32436489
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r6
    h: f7dcd0f40d75
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r1
    h: e0fa32436489
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r6
    h: f7dcd0f40d75
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:inverter
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r1
    h: e0fa32436489
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r6
    h: f7dcd0f40d75
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r1
    h: e0fa32436489
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r6
    h: f7dcd0f40d75
  review: drafted
  review_note: 'support check: partial - Checking insulation is suggested, but insulation resistance testing
    as a detection method is not stated.'
---
