---
id: fc:schneider-electric-conext-cl125-26
type: FaultCode
name: Schneider Electric CL125 026
aliases:
- '026'
- '26'
- Schneider Electric 026
- Bus voltage is fluctuating.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '026'
code_key: '26'
display_message: Bus voltage is fluctuating.
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r8
    h: fd543cae4e70
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r5
    h: 8295e1aaf337
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-voltage-fluctuation
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r8
    h: fd543cae4e70
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r5
    h: 8295e1aaf337
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, contact technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r8
    h: fd543cae4e70
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r5
    h: 8295e1aaf337
  review: drafted
  review_note: 'support check: partial - Auto recovery stated, but the contact-technical-support note
    is not in the passages.'
---
