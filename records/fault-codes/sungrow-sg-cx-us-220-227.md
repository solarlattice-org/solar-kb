---
id: fc:sungrow-sg-cx-us-220-227
type: FaultCode
name: Sungrow SG-CX-US 220-227
aliases:
- 220-227
- Sungrow 220-227
- PVx abnormal
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 220-227
code_key: 220-227
code_from: 220
code_to: 227
display_message: PVx abnormal
page: 97
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r3
    h: 95887f37002c
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r3
    h: f733aab9966e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:pv-input-abnormal
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r3
    h: 95887f37002c
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r3
    h: f733aab9966e
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c4
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r3
    h: 95887f37002c
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r3
    h: f733aab9966e
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r3
    h: 95887f37002c
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r3
    h: f733aab9966e
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:fuse-replacement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r3
    h: 95887f37002c
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r3
    h: f733aab9966e
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:warning
  note: Treated as an alarm; may be ignored if the input is intentionally unused.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r3
    h: 95887f37002c
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r3
    h: f733aab9966e
  review: drafted
  review_note: 'support check: partial - The row says to ignore the alarm if the string is not needed,
    which supports the note, but nothing states…'
---
