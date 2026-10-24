---
id: fc:schneider-electric-conext-cl125-31
type: FaultCode
name: Schneider Electric CL125 031
aliases:
- '031'
- '31'
- Schneider Electric 031
- Clamp capacitance under-voltage event is detected.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '031'
code_key: '31'
display_message: Clamp capacitance under-voltage event is detected.
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r11
    h: bf2fbfd1094b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r8
    h: 41230dae8642
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:clamp-capacitor-undervoltage
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r11
    h: bf2fbfd1094b
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r8
    h: 41230dae8642
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Contact technical support if the event persists.
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r8
    h: 41230dae8642
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Auto recovery stated, but contact-support note is absent.'
- claim_id: c5
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r11
    h: bf2fbfd1094b
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r8
    h: 41230dae8642
  review: drafted
---
