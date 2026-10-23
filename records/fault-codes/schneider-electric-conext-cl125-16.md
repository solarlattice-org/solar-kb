---
id: fc:schneider-electric-conext-cl125-16
type: FaultCode
name: Schneider Electric CL125 016
aliases:
- '016'
- '16'
- Schneider Electric 016
- AC output overload
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '016'
code_key: '16'
display_message: AC output overload
page: 125
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r5
    h: 0f3c81eff73d
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r4
    h: 1fd5270d23a4
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overload
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r5
    h: 0f3c81eff73d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r4
    h: 1fd5270d23a4
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r5
    h: 0f3c81eff73d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r4
    h: 1fd5270d23a4
  review: drafted
  review_note: 'support check: partial - The fault class is not stated, only implied by the alarm and
    auto-recovery.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, contact technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r5
    h: 0f3c81eff73d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r4
    h: 1fd5270d23a4
  review: drafted
---
