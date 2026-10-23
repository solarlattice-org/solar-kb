---
id: fc:schneider-electric-conext-cl125-43
type: FaultCode
name: Schneider Electric CL125 043
aliases:
- '043'
- '43'
- Schneider Electric 043
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '043'
code_key: '43'
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r1
    h: ad3a500e572d
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r8
    h: 1bbf529920ec
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-undertemperature
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r1
    h: ad3a500e572d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r8
    h: 1bbf529920ec
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r1
    h: ad3a500e572d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r8
    h: 1bbf529920ec
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Operation is stopped while the ambient temperature is below the permitted range.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r1
    h: ad3a500e572d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r8
    h: 1bbf529920ec
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Operator restarts once the ambient temperature is back within range.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r1
    h: ad3a500e572d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r8
    h: 1bbf529920ec
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r1
    h: ad3a500e572d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r8
    h: 1bbf529920ec
  review: drafted
---
