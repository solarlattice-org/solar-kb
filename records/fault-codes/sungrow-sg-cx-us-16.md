---
id: fc:sungrow-sg-cx-us-16
type: FaultCode
name: Sungrow SG-CX-US 16
aliases:
- '16'
- Sungrow 16
- Output overload
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '16'
code_key: '16'
display_message: Output overload
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r4
    h: bb1358f62fd2
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overload
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r4
    h: bb1358f62fd2
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Service contact if fault persists.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r4
    h: bb1358f62fd2
  review: drafted
---
