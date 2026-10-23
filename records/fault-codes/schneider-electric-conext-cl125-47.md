---
id: fc:schneider-electric-conext-cl125-47
type: FaultCode
name: Schneider Electric CL125 047
aliases:
- '047'
- '47'
- Schneider Electric 047
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '047'
code_key: '47'
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r3
    h: 66703b315156
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r1
    h: 790a3791e300
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r3
    h: 66703b315156
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r1
    h: 790a3791e300
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r3
    h: 66703b315156
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r1
    h: 790a3791e300
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r3
    h: 66703b315156
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r1
    h: 790a3791e300
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r3
    h: 66703b315156
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r1
    h: 790a3791e300
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Disconnecting from all power sources implies intervention, but
    ''fault'' is not explicitly stated.'
---
