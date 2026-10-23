---
id: fc:schneider-electric-conext-cl125-3
type: FaultCode
name: Schneider Electric CL125 003
aliases:
- '003'
- '3'
- Schneider Electric 003
- Grid transient voltage exceeds the permissible range.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '003'
code_key: '3'
display_message: Grid transient voltage exceeds the permissible range.
page: 123
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r2
    h: 9551a69bbbf5
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r2
    h: 35334eae191d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-voltage-out-of-range
  note: Short-term grid voltage transient.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r2
    h: 9551a69bbbf5
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r2
    h: 35334eae191d
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Contact technical support if the event persists.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=47.r2
    h: 9551a69bbbf5
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=27.r2
    h: 35334eae191d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
