---
id: fc:schneider-electric-conext-cl125-33
type: FaultCode
name: Schneider Electric CL125 033
aliases:
- '033'
- '33'
- Schneider Electric 033
- Clamp capacitance pre-charge ground fault is detected
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '033'
code_key: '33'
display_message: Clamp capacitance pre-charge ground fault is detected
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r13
    h: 70fb66b2c29c
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r10
    h: 40c105975eae
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ground-fault
  note: Detected during clamp capacitor pre-charge.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r13
    h: 70fb66b2c29c
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r10
    h: 40c105975eae
  review: drafted
  review_note: 'support check: partial - Pre-charge ground fault is stated, but ''alarm or trip'' is not.'
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Contact technical support if the event persists.
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r10
    h: 40c105975eae
  review: drafted
  review_note: 'support check: partial - Auto recovery stated, but contact-support note is absent.'
---
