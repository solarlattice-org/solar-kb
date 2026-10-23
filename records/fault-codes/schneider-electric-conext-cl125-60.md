---
id: fc:schneider-electric-conext-cl125-60
type: FaultCode
name: Schneider Electric CL125 060
aliases:
- '060'
- '60'
- Schneider Electric 060
- Main DSP data comparison event is detected.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '060'
code_key: '60'
display_message: Main DSP data comparison event is detected.
page: 129
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r5
    h: 099769e75bd5
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r4
    h: efb99bb3bec8
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r5
    h: 099769e75bd5
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r4
    h: efb99bb3bec8
  review: drafted
  review_note: 'support check: partial - Main DSP data comparison event suggests internal fault but is
    not explicitly called a device fault.'
- claim_id: c4
  rel: affects
  target: comp:control-board
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r5
    h: 099769e75bd5
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r4
    h: efb99bb3bec8
  review: drafted
  review_note: 'support check: partial - Main DSP is implied as control board but not stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, escalate to technical support.
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r4
    h: efb99bb3bec8
  review: drafted
  review_note: 'support check: partial - u31 says wait to recover automatically; escalation note not present.'
---
