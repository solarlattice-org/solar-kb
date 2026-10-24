---
id: fc:schneider-electric-conext-cl125-42
type: FaultCode
name: Schneider Electric CL125 042
aliases:
- '042'
- '42'
- Schneider Electric 042
- AC current imbalance
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '042'
code_key: '42'
display_message: AC current imbalance
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r7
    h: 7d6c25f9bcf4
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r7
    h: 54d74faa6b70
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:phase-imbalance
  note: AC output current imbalance between phases.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r7
    h: 7d6c25f9bcf4
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r7
    h: 54d74faa6b70
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Implied by the instruction to wait for the inverter to recover.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r7
    h: 7d6c25f9bcf4
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r7
    h: 54d74faa6b70
  review: drafted
  review_note: 'support check: partial - Trip is only implied by wait to recover; not explicit.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Contact technical support if the event persists.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r7
    h: 7d6c25f9bcf4
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r7
    h: 54d74faa6b70
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r7
    h: 7d6c25f9bcf4
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r7
    h: 54d74faa6b70
  review: drafted
---
