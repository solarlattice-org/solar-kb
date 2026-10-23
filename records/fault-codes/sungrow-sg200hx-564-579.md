---
id: fc:sungrow-sg200hx-564-579
type: FaultCode
name: Sungrow SG200HX 564-579
aliases:
- 564-579
- Sungrow 564-579
- PV Reverse Connection Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: 564-579
code_key: 564-579
code_from: 564
code_to: 579
display_message: PV Reverse Connection Alarm
page: 90
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r3
    h: e686ceb2bfaa
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r3
    h: e686ceb2bfaa
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  note: Codes 564 to 579 map to strings 17 to 32.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r3
    h: e686ceb2bfaa
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r3
    h: e686ceb2bfaa
  review: drafted
  review_note: 'support check: partial - Only a check of string polarity is stated, not a measurement
    method.'
- claim_id: c5
  rel: mitigated_by
  target: mit:polarity-correction
  note: Contact service if the alarm persists.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r3
    h: e686ceb2bfaa
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r3
    h: e686ceb2bfaa
  review: drafted
---
