---
id: fc:schneider-electric-conext-cl125-30
type: FaultCode
name: Schneider Electric CL125 030
aliases:
- '030'
- '30'
- Schneider Electric 030
- Clamp capacitance over-voltage event is detected.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '030'
code_key: '30'
display_message: Clamp capacitance over-voltage event is detected.
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r10
    h: d5a4aa130807
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r7
    h: ceacacae7f06
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:clamp-capacitor-overvoltage
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r10
    h: d5a4aa130807
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r7
    h: ceacacae7f06
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Contact technical support if the event persists.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r10
    h: d5a4aa130807
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r7
    h: ceacacae7f06
  review: drafted
  review_note: 'support check: partial - Auto recovery stated, but contact-support note is absent.'
- claim_id: c5
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r10
    h: d5a4aa130807
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r7
    h: ceacacae7f06
  review: drafted
---
