---
id: fc:sungrow-sg250hx-28
type: FaultCode
name: Sungrow SG250HX 28
aliases:
- '28'
- Sungrow 28
- PV Reserve Con-nection Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '28'
code_key: '28'
display_message: PV Reserve Con-nection Fault
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r2
    h: ef214f6e526a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r2
    h: ef214f6e526a
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r2
    h: ef214f6e526a
  review: drafted
  review_note: 'support check: partial - The passages say to check whether the string is of reverse polarity,
    but they don''t mention polarity measurement as a method.'
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r2
    h: ef214f6e526a
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Correct polarity only after string current falls below the stated threshold; service if the fault
    persists.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r2
    h: ef214f6e526a
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r2
    h: ef214f6e526a
  review: drafted
  review_note: 'support check: partial - The row names code 28 as a PV reverse connection fault, but it
    doesn''t state a fault classification beyond the…'
- claim_id: c7
  rel: applies_to
  target: prod:sungrow-sg250hx
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r2
    h: ef214f6e526a
  review: drafted
---
