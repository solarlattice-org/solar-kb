---
id: fc:sungrow-sg-cx-us-78-81
type: FaultCode
name: Sungrow SG-CX-US 078-081
aliases:
- 078-081
- 78-81
- Sungrow 078-081
- PVx abnormal
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 078-081
code_key: 78-81
code_from: 78
code_to: 81
display_message: PVx abnormal
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r1
    h: 8d971d4be264
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:pv-input-abnormal
  note: Codes map to PV inputs 1 to 4.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r1
    h: 8d971d4be264
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r1
    h: 8d971d4be264
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r1
    h: 8d971d4be264
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:fuse-replacement
  note: When the corresponding DC fuse is damaged.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r1
    h: 8d971d4be264
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if wiring and fuse checks do not resolve it.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r1
    h: 8d971d4be264
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:warning
  note: Row treats it as an alarm that may be ignored for unused inputs.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r1
    h: 8d971d4be264
  review: drafted
---
