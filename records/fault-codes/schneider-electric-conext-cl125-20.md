---
id: fc:schneider-electric-conext-cl125-20
type: FaultCode
name: Schneider Electric CL125 020
aliases:
- '020'
- '20'
- Schneider Electric 020
- High DC bus voltage
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '020'
code_key: '20'
display_message: High DC bus voltage
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r2
    h: 0e3c446f12b9
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r7
    h: 1a4c53e45506
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r2
    h: 0e3c446f12b9
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r7
    h: 1a4c53e45506
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r2
    h: 0e3c446f12b9
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r7
    h: 1a4c53e45506
  review: drafted
  review_note: 'review: partial - The row says the inverter recovers automatically and does not say the
    device stops or needs intervention, so the fault class is…'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, contact technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r2
    h: 0e3c446f12b9
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r7
    h: 1a4c53e45506
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r2
    h: 0e3c446f12b9
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r7
    h: 1a4c53e45506
  review: drafted
---
