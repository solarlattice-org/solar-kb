---
id: fc:sungrow-sg250hx-264-283
type: FaultCode
name: Sungrow SG250HX 264-283
aliases:
- 264-283
- Sungrow 264-283
- MPPT Reverse Connection
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: 264-283
code_key: 264-283
code_from: 264
code_to: 283
display_message: MPPT Reverse Connection
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r2
    h: a863e081c095
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r2
    h: a863e081c095
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r2
    h: a863e081c095
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  note: Codes map to individual strings of the MPPT inputs.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r2
    h: a863e081c095
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r2
    h: a863e081c095
  review: drafted
  review_note: 'support check: partial - The row says to check whether the string is reverse polarity,
    but it does not specify a polarity measurement method.'
- claim_id: c6
  rel: mitigated_by
  target: mit:safety-isolation
  note: Open DC switch once string current falls below the stated low threshold before rework.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r2
    h: a863e081c095
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Correct reversed string polarity; contact service if the fault persists.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r2
    h: a863e081c095
  review: drafted
---
