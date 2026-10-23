---
id: fc:schneider-electric-conext-cl125-22
type: FaultCode
name: Schneider Electric CL125 022
aliases:
- '022'
- '22'
- Schneider Electric 022
- Over current protection
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '022'
code_key: '22'
display_message: Over current protection
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r4
    h: d26d0ac29786
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r1
    h: 8a662aa97327
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:overcurrent
  note: Grid-side or PV-side current exceeded the protection limit.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r4
    h: d26d0ac29786
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r1
    h: 8a662aa97327
  review: drafted
  review_note: 'support check: partial - The row says over current protection, and its solution mentions
    grid or PV current. It does not say which side…'
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r4
    h: d26d0ac29786
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r1
    h: 8a662aa97327
  review: drafted
  review_note: 'support check: partial - The fault class is not explicitly stated.'
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when currents are within permissible range and the event persists.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r4
    h: d26d0ac29786
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r1
    h: 8a662aa97327
  review: drafted
  review_note: 'support check: partial - The row only says to see the note if the event persists. It does
    not name contacting manufacturer service.'
---
