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
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r4
    h: 4fb9f1339aab
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r4
    h: 4fb9f1339aab
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r4
    h: 4fb9f1339aab
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r4
    h: 4fb9f1339aab
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r4
    h: 4fb9f1339aab
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r4
    h: 4fb9f1339aab
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r4
    h: 4fb9f1339aab
  review: drafted
  review_note: 'support check: partial - Check method has checking whether the string is reverse polarity,
    but no explicit detection method of polarity measurement is stated.'
- claim_id: c6
  rel: mitigated_by
  target: mit:polarity-correction
  note: Correct only with DC switch open and string current below 0.5 A.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r4
    h: 4fb9f1339aab
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r4
    h: 4fb9f1339aab
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r4
    h: 4fb9f1339aab
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r4
    h: 4fb9f1339aab
  review: drafted
---
