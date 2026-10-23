---
id: fc:schneider-electric-conext-cl125-15
type: FaultCode
name: Schneider Electric CL125 015
aliases:
- '015'
- '15'
- Schneider Electric 015
- Grid impedance exceeds inverter's limit.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '015'
code_key: '15'
display_message: Grid impedance exceeds inverter's limit.
page: 125
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r4
    h: 462781d51469
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r3
    h: d2952de8a0d5
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-impedance-high
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r4
    h: 462781d51469
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r3
    h: d2952de8a0d5
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r4
    h: 462781d51469
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r3
    h: d2952de8a0d5
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:impedance-matching
  note: Cable type, size and transformer impedance per design guides.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r4
    h: 462781d51469
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r3
    h: d2952de8a0d5
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r4
    h: 462781d51469
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r3
    h: d2952de8a0d5
  review: drafted
  review_note: 'support check: partial - The row does not state the fault versus warning class. A fault
    is only loosely implied.'
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r4
    h: 462781d51469
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r3
    h: d2952de8a0d5
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
