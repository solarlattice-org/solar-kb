---
id: fc:schneider-electric-conext-cl125-23
type: FaultCode
name: Schneider Electric CL125 023
aliases:
- '023'
- '23'
- Schneider Electric 023
- PV configuration mode has changed during normal operation.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '023'
code_key: '23'
display_message: PV configuration mode has changed during normal operation.
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r5
    h: 71301dc2379c
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r2
    h: 75ab46f00c43
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  note: PV configuration mode changed during operation.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r5
    h: 71301dc2379c
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r2
    h: 75ab46f00c43
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r5
    h: 71301dc2379c
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r2
    h: 75ab46f00c43
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  note: After checking the PV configuration.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r5
    h: 71301dc2379c
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r2
    h: 75ab46f00c43
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r5
    h: 71301dc2379c
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r2
    h: 75ab46f00c43
  review: drafted
  review_note: 'support check: partial - The fault class is not explicitly stated, though the required
    restart suggests a fault.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r5
    h: 71301dc2379c
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r2
    h: 75ab46f00c43
  review: drafted
---
