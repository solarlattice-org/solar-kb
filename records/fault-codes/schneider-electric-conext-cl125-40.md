---
id: fc:schneider-electric-conext-cl125-40
type: FaultCode
name: Schneider Electric CL125 040
aliases:
- '040'
- '40'
- Schneider Electric 040
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '040'
code_key: '40'
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r5
    h: 9b59322c46b9
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r5
    h: 9feff9f175be
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r5
    h: 9b59322c46b9
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r5
    h: 9feff9f175be
  review: drafted
  review_note: 'support check: partial - Description says AC (or DC) over-current, so AC overcurrent is
    possible but not definite.'
- claim_id: c4
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r5
    h: 9b59322c46b9
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r5
    h: 9feff9f175be
  review: drafted
  review_note: 'support check: partial - DC over-current is only an alternative in ''AC (or DC) over-current''.'
- claim_id: c5
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r5
    h: 9b59322c46b9
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r5
    h: 9feff9f175be
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Implied by the instruction to wait for the inverter to recover.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r5
    h: 9b59322c46b9
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r5
    h: 9feff9f175be
  review: drafted
  review_note: 'support check: partial - Trip is only implied by wait to recover; not explicit.'
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Contact technical support if the event persists.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r5
    h: 9b59322c46b9
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r5
    h: 9feff9f175be
  review: drafted
---
