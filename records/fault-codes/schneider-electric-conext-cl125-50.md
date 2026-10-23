---
id: fc:schneider-electric-conext-cl125-50
type: FaultCode
name: Schneider Electric CL125 050
aliases:
- '050'
- '50'
- Schneider Electric 050
- Phase-T current sampling channel event
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '050'
code_key: '50'
display_message: Phase-T current sampling channel event
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r6
    h: b44affffa890
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r4
    h: 081cf1f2ed1f
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r6
    h: b44affffa890
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r4
    h: 081cf1f2ed1f
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, escalate to technical support.
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r4
    h: 081cf1f2ed1f
  review: drafted
---
