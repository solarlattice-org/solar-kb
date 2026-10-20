---
id: fc:sungrow-sg-cx-us-564-571
type: FaultCode
name: Sungrow SG-CX-US 564-571
aliases:
- 564-571
- Sungrow 564-571
- String x reverse connection alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 564-571
code_key: 564-571
code_from: 564
code_to: 571
display_message: String x reverse connection alarm
page: 98
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r3
    h: 178d89245341
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  note: Codes map to strings 17 to 24.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r3
    h: 178d89245341
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r3
    h: 178d89245341
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r3
    h: 178d89245341
  review: drafted
  review_note: 'support check: partial - The row says to check whether the string is reverse polarity,
    but does not state the detection method is a…'
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Correct polarity only at low irradiance with string current below 0.5 A and DC switch open.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r3
    h: 178d89245341
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if polarity is correct and the alarm persists.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r3
    h: 178d89245341
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:warning
  note: Labelled as an alarm, distinct from the fault variant.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r3
    h: 178d89245341
  review: drafted
  review_note: 'support check: partial - Labelled an alarm, which suggests a warning, but the row does
    not state device behavior.'
---
