---
id: fc:sungrow-sg-cx-us-30-34
type: FaultCode
name: Sungrow SG-CX-US 30-34
aliases:
- 30-34
- Sungrow 30-34
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 30-34
code_key: 30-34
code_from: 30
code_to: 34
display_message: Device anomaly
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r4
    h: 53fe3ee9226d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r4
    h: 53fe3ee9226d
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
    loc: tbl=50.r4
    h: 53fe3ee9226d
  review: drafted
---
