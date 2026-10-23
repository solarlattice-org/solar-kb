---
id: fc:schneider-electric-conext-cl125-25
type: FaultCode
name: Schneider Electric CL125 025
aliases:
- '025'
- '25'
- Schneider Electric 025
- Transient unbalance of voltage neutral point
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '025'
code_key: '25'
display_message: Transient unbalance of voltage neutral point
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r7
    h: 166d9e8dc841
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r4
    h: b732afea072c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:neutral-point-voltage-imbalance
  note: Transient imbalance.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r7
    h: 166d9e8dc841
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r4
    h: b732afea072c
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes when deviation returns within range; contact support if persistent.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r7
    h: 166d9e8dc841
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r4
    h: b732afea072c
  review: drafted
  review_note: 'support check: partial - Auto recovery stated, but contact-support note is absent.'
---
