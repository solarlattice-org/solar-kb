---
id: fc:schneider-electric-conext-cl125-74
type: FaultCode
name: Schneider Electric CL125 074
aliases:
- '074'
- '74'
- Schneider Electric 074
- Communication event
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '074'
code_key: '74'
display_message: Communication event
page: 130
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r1
    h: f52da0a2d88d
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r8
    h: bef89b18f51b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r1
    h: f52da0a2d88d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r8
    h: bef89b18f51b
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r1
    h: f52da0a2d88d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r8
    h: bef89b18f51b
  review: drafted
  review_note: 'support check: partial - Inverter continues feeding, consistent with a warning, but not
    labeled as such.'
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  note: The inverter keeps feeding into the grid.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r1
    h: f52da0a2d88d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r8
    h: bef89b18f51b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
