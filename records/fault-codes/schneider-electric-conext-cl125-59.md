---
id: fc:schneider-electric-conext-cl125-59
type: FaultCode
name: Schneider Electric CL125 059
aliases:
- '059'
- '59'
- Schneider Electric 059
- Main DSP communication redundancy event is detected.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '059'
code_key: '59'
display_message: Main DSP communication redundancy event is detected.
page: 129
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r4
    h: 6b4eef1795bd
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r3
    h: 202f4365fc17
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r4
    h: 6b4eef1795bd
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r3
    h: 202f4365fc17
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:control-board
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r4
    h: 6b4eef1795bd
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r3
    h: 202f4365fc17
  review: drafted
  review_note: 'support check: partial - Main DSP is implied as control board but not stated as such.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, escalate to technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r4
    h: 6b4eef1795bd
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r3
    h: 202f4365fc17
  review: drafted
  review_note: 'support check: partial - Auto recovery stated; escalation note for persistence not in
    passages.'
---
