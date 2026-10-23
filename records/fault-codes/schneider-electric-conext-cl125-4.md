---
id: fc:schneider-electric-conext-cl125-4
type: FaultCode
name: Schneider Electric CL125 004
aliases:
- '004'
- '4'
- Schneider Electric 004
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '004'
code_key: '4'
page: 123
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r3
    h: b63d6b6f6819
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r3
    h: d46a1865646f
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r3
    h: b63d6b6f6819
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r3
    h: d46a1865646f
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r3
    h: b63d6b6f6819
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r3
    h: d46a1865646f
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: When measured voltage is below limit; if within range and persisting, escalate to technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r3
    h: b63d6b6f6819
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r3
    h: d46a1865646f
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Grid protection with utility-defined thresholds and protection time.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r3
    h: b63d6b6f6819
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r3
    h: d46a1865646f
  review: drafted
  review_note: 'support check: partial - Utility-defined thresholds and protection time stated, but no
    trip/production stop stated.'
---
