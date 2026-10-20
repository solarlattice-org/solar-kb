---
id: fc:sungrow-sg-cx-us-448-471
type: FaultCode
name: Sungrow SG-CX-US 448-471
aliases:
- 448-471
- Sungrow 448-471
- String x reverse connection fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 448-471
code_key: 448-471
code_from: 448
code_to: 471
display_message: String x reverse connection fault
page: 97
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r4
    h: 4fb9f1339aab
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  note: Codes map to strings 1 to 24.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r4
    h: 4fb9f1339aab
  review: drafted
  review_note: 'support check: partial - Reverse connection fault is stated, but the mapping is strings
    1 to 24 for codes 448-471, which matches the note.'
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r4
    h: 4fb9f1339aab
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r4
    h: 4fb9f1339aab
  review: drafted
  review_note: 'support check: partial - The row says to check whether the string is reverse polarity,
    but does not state the detection method is a…'
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Correct polarity only at low irradiance with string current below 0.5 A and DC switch open.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r4
    h: 4fb9f1339aab
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if polarity is correct and the fault persists.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r4
    h: 4fb9f1339aab
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  note: Labelled as a fault, distinct from the alarm variant.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r4
    h: 4fb9f1339aab
  review: drafted
  review_note: 'support check: partial - Described as a ''fault'' in the description, but the row gives
    no device behavior to confirm a fault classification.'
---
