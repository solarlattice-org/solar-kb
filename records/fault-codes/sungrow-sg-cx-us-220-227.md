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
  rel: reports
  target: symptom:pv-input-abnormal
  note: Codes map to PV inputs 5 to 12.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r3
    h: 95887f37002c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r3
    h: 95887f37002c
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r3
    h: 95887f37002c
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:fuse-replacement
  note: When the corresponding DC fuse is damaged.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r3
    h: 95887f37002c
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if wiring and fuse checks do not resolve it.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r3
    h: 95887f37002c
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:warning
  note: Row treats it as an alarm that may be ignored for unused inputs.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r3
    h: 95887f37002c
  review: drafted
  review_note: 'support check: partial - Row says ignore the alarm for unused strings, but does not state
    the device continues operating, so the warning class…'
---
