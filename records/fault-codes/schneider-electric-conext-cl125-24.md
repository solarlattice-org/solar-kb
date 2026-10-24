---
id: fc:schneider-electric-conext-cl125-24
type: FaultCode
name: Schneider Electric CL125 024
aliases:
- '024'
- '24'
- Schneider Electric 024
- Voltage imbalance at neutral point
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '024'
code_key: '24'
display_message: Voltage imbalance at neutral point
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r6
    h: 1f47f6d4b4e8
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r3
    h: 7ecdfa86e7ce
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:neutral-point-voltage-imbalance
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r6
    h: 1f47f6d4b4e8
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r3
    h: 7ecdfa86e7ce
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes when deviation returns within range; contact support if persistent.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r6
    h: 1f47f6d4b4e8
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r3
    h: 7ecdfa86e7ce
  review: drafted
  review_note: 'support check: partial - Automatic recovery when deviation within range is stated, but
    the ''contact support if persistent'' note is not in the passages.'
- claim_id: c5
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r6
    h: 1f47f6d4b4e8
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r3
    h: 7ecdfa86e7ce
  review: drafted
---
