---
id: fc:schneider-electric-conext-cl125-32
type: FaultCode
name: Schneider Electric CL125 032
aliases:
- '032'
- '32'
- Schneider Electric 032
- Clamp capacitance imbalance event is detected.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '032'
code_key: '32'
display_message: Clamp capacitance imbalance event is detected.
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r12
    h: 475197cf5a2f
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r9
    h: 96ddee851f12
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:clamp-capacitor-imbalance
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r12
    h: 475197cf5a2f
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r9
    h: 96ddee851f12
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Contact technical support if the event persists.
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r9
    h: 96ddee851f12
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Auto recovery stated, but contact-support note is absent.'
---
