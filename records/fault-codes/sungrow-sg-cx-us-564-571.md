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
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r3
    h: 178d89245341
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r3
    h: 178d89245341
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r3
    h: 178d89245341
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r3
    h: 178d89245341
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r3
    h: 178d89245341
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r3
    h: 178d89245341
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r3
    h: 178d89245341
  review: drafted
  review_note: 'support check: partial - Checking string polarity stated but no explicit measurement method.'
- claim_id: c6
  rel: mitigated_by
  target: mit:polarity-correction
  note: Correct only with DC switch open and string current below 0.5 A.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r3
    h: 178d89245341
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r3
    h: 178d89245341
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c7
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r3
    h: 178d89245341
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r3
    h: 178d89245341
  review: drafted
---
