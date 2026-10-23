---
id: fc:schneider-electric-conext-cl125-49
type: FaultCode
name: Schneider Electric CL125 049
aliases:
- '049'
- '49'
- Schneider Electric 049
- Phase-S current sampling channel event
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '049'
code_key: '49'
display_message: Phase-S current sampling channel event
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r5
    h: 51797bb3e012
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r3
    h: 1918ab4a8986
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r5
    h: 51797bb3e012
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r3
    h: 1918ab4a8986
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, escalate to technical support.
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r3
    h: 1918ab4a8986
  review: drafted
---
