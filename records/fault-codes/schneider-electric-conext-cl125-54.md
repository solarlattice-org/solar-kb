---
id: fc:schneider-electric-conext-cl125-54
type: FaultCode
name: Schneider Electric CL125 054
aliases:
- '054'
- '54'
- Schneider Electric 054
- Grid frequency redundancy event is detected.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '054'
code_key: '54'
display_message: Grid frequency redundancy event is detected.
page: 129
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r1
    h: 40e13e059a31
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r7
    h: bd042b332a90
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-frequency-out-of-range
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r1
    h: 40e13e059a31
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r7
    h: bd042b332a90
  review: drafted
  review_note: 'review: partial - The row calls it a grid frequency redundancy event and says to measure
    the frequency; it allows that the frequency may exceed…'
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r1
    h: 40e13e059a31
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r7
    h: bd042b332a90
  review: drafted
  review_note: 'support check: partial - Measuring grid frequency is the remedy step; the detection is
    a redundancy event, not stated as measurement.'
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: When frequency exceeds the range; if within range and persisting, contact technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r1
    h: 40e13e059a31
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r7
    h: bd042b332a90
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r1
    h: 40e13e059a31
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r7
    h: bd042b332a90
  review: drafted
---
