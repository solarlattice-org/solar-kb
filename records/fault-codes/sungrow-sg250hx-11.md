---
id: fc:sungrow-sg250hx-11
type: FaultCode
name: Sungrow SG250HX 11
aliases:
- '11'
- Sungrow 11
- System Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '11'
code_key: '11'
display_message: System Fault
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r4
    h: b47f333574e3
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
  note: 'Escalation: switch restart after 15 minutes, then service if persistent.'
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r4
    h: b47f333574e3
  review: drafted
---
