---
id: fc:schneider-electric-conext-cl125-55
type: FaultCode
name: Schneider Electric CL125 055
aliases:
- '055'
- '55'
- Schneider Electric 055
- Inverter insulation resistance redundancy event is detected.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '055'
code_key: '55'
display_message: Inverter insulation resistance redundancy event is detected.
page: 129
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r2
    h: 0b7fce600905
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r1
    h: 26a2b3cff983
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r2
    h: 0b7fce600905
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r1
    h: 26a2b3cff983
  review: drafted
  review_note: 'support check: partial - Passages describe an insulation resistance redundancy event but
    do not say ''low'' insulation resistance explicitly.'
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, escalate to technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r2
    h: 0b7fce600905
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r1
    h: 26a2b3cff983
  review: drafted
  review_note: 'support check: partial - Auto recovery is stated, but the escalation note about persisting
    is not in the passages.'
---
