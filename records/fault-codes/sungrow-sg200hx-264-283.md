---
id: fc:sungrow-sg200hx-264-283
type: FaultCode
name: Sungrow SG200HX 264-283
aliases:
- 264-283
- Sungrow 264-283
- MPPT Reverse Connection
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: 264-283
code_key: 264-283
code_from: 264
code_to: 283
display_message: MPPT Reverse Connection
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r3
    h: d7c831b6e61d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r3
    h: d7c831b6e61d
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  note: Each code maps to one specific string input.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r3
    h: d7c831b6e61d
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r3
    h: d7c831b6e61d
  review: drafted
  review_note: 'support check: partial - Row says check whether the string is reverse polarity, but no
    polarity measurement method is stated.'
- claim_id: c5
  rel: mitigated_by
  target: mit:polarity-correction
  note: Correct only once string current is below 0.5 A and the DC switch is open; contact service if
    it persists.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r3
    h: d7c831b6e61d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
