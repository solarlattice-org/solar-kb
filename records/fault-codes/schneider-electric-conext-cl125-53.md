---
id: fc:schneider-electric-conext-cl125-53
type: FaultCode
name: Schneider Electric CL125 053
aliases:
- '053'
- '53'
- Schneider Electric 053
- Grid voltage redundancy event is detected.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '053'
code_key: '53'
display_message: Grid voltage redundancy event is detected.
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r7
    h: c8d91f333638
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r6
    h: 89c275f9767a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-voltage-out-of-range
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r7
    h: c8d91f333638
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r6
    h: 89c275f9767a
  review: drafted
  review_note: 'support check: partial - A grid voltage redundancy event with a check against permissible
    limits suggests out-of-range voltage, but the passages do not state…'
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r7
    h: c8d91f333638
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r6
    h: 89c275f9767a
  review: drafted
  review_note: 'support check: partial - Measuring grid voltage is the remedy step; the detection is a
    redundancy event, not stated as measurement.'
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: Applies when measured grid voltage exceeds the permitted limit; otherwise escalate to technical
    support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r7
    h: c8d91f333638
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r6
    h: 89c275f9767a
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r7
    h: c8d91f333638
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r6
    h: 89c275f9767a
  review: drafted
---
