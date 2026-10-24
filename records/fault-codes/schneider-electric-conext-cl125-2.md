---
id: fc:schneider-electric-conext-cl125-2
type: FaultCode
name: Schneider Electric CL125 002
aliases:
- '002'
- '2'
- Schneider Electric 002
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '002'
code_key: '2'
page: 123
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r1
    h: c01eaaedd782
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r1
    h: 031fce53e2af
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r1
    h: c01eaaedd782
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r1
    h: 031fce53e2af
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r1
    h: c01eaaedd782
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r1
    h: 031fce53e2af
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: When measured voltage is out of range; if within range, escalate to technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r1
    h: c01eaaedd782
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r1
    h: 031fce53e2af
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Grid protection with utility-defined thresholds and protection time.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r1
    h: c01eaaedd782
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r1
    h: 031fce53e2af
  review: drafted
  review_note: 'review: partial - The row''s mention of protection time and utility-defined thresholds
    supports the note, but no passage says production stops or the inverter trips.'
- claim_id: c7
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r1
    h: c01eaaedd782
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r1
    h: 031fce53e2af
  review: drafted
---
