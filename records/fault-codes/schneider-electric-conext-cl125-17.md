---
id: fc:schneider-electric-conext-cl125-17
type: FaultCode
name: Schneider Electric CL125 017
aliases:
- '017'
- '17'
- Schneider Electric 017
- Grid voltage imbalance
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '017'
code_key: '17'
display_message: Grid voltage imbalance
page: 125
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r6
    h: 33ad00880877
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r5
    h: 8c869e24f9a8
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:phase-imbalance
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r6
    h: 33ad00880877
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r5
    h: 8c869e24f9a8
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r6
    h: 33ad00880877
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r5
    h: 8c869e24f9a8
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r6
    h: 33ad00880877
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r5
    h: 8c869e24f9a8
  review: drafted
  review_note: 'review: partial - The row lists it as an event and says the inverter recovers automatically,
    but nothing in the passages says the device stops…'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, contact technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r6
    h: 33ad00880877
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r5
    h: 8c869e24f9a8
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r6
    h: 33ad00880877
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r5
    h: 8c869e24f9a8
  review: drafted
---
