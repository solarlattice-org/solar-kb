---
id: fc:schneider-electric-conext-cl125-19
type: FaultCode
name: Schneider Electric CL125 019
aliases:
- '019'
- '19'
- Schneider Electric 019
- High transient DC bus voltage
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '019'
code_key: '19'
display_message: High transient DC bus voltage
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r1
    h: f6b7e6e95294
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r6
    h: f90663236cdc
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  note: Transient overvoltage on the DC bus.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r1
    h: f6b7e6e95294
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r6
    h: f90663236cdc
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r1
    h: f6b7e6e95294
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r6
    h: f90663236cdc
  review: drafted
  review_note: 'support check: partial - The fault class is not explicitly stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, contact technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r1
    h: f6b7e6e95294
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r6
    h: f90663236cdc
  review: drafted
---
