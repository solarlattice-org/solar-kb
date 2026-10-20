---
id: fc:sungrow-sg-cx-us-580-587
type: FaultCode
name: Sungrow SG-CX-US 580-587
aliases:
- 580-587
- Sungrow 580-587
- String x output current anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 580-587
code_key: 580-587
code_from: 580
code_to: 587
display_message: String x output current anomaly
page: 98
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r4
    h: 694087bdfee9
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:abnormal-string-current
  note: Codes map to strings 17 to 24.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r4
    h: 694087bdfee9
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
  review_note: 'support check: partial - String output current anomaly is stated and the mapping is 17
    to 24, but the row gives it as 580…'
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r4
    h: 694087bdfee9
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:visual-inspection
  note: Check modules for shading objects and abnormal aging.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r4
    h: 694087bdfee9
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:avoid-partial-shading
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r4
    h: 694087bdfee9
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:manual-cleaning
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r4
    h: 694087bdfee9
  review: drafted
  review_note: 'support check: partial - Row says to ensure module cleanness after removing shelter, which
    implies cleaning but does not state it explicitly.'
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if shading and aging checks do not explain it.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r4
    h: 694087bdfee9
  review: drafted
---
