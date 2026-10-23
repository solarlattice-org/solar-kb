---
id: fc:schneider-electric-conext-cl125-14
type: FaultCode
name: Schneider Electric CL125 014
aliases:
- '014'
- '14'
- Schneider Electric 014
- Average grid over-voltage (10 minutes)
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '014'
code_key: '14'
display_message: Average grid over-voltage (10 minutes)
page: 125
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r3
    h: e16c926506c3
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r2
    h: 32d1dd5528cc
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r3
    h: e16c926506c3
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r2
    h: 32d1dd5528cc
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r3
    h: e16c926506c3
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r2
    h: 32d1dd5528cc
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r3
    h: e16c926506c3
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r2
    h: 32d1dd5528cc
  review: drafted
  review_note: 'support check: partial - The row says it is an alarm that recovers automatically, but
    never states fault versus warning. Classing it as a…'
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Inverter stops on 10-minute average overvoltage and recovers afterwards.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r3
    h: e16c926506c3
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r2
    h: 32d1dd5528cc
  review: drafted
  review_note: 'support check: partial - The passages say the inverter can recover automatically but do
    not state that it stops feeding in. The trip is…'
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, contact technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r3
    h: e16c926506c3
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r2
    h: 32d1dd5528cc
  review: drafted
---
