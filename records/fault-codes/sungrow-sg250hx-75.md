---
id: fc:sungrow-sg250hx-75
type: FaultCode
name: Sungrow SG250HX 75
aliases:
- '75'
- Sungrow 75
- Inverter Parallel Communication Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '75'
code_key: '75'
display_message: Inverter Parallel Communication Alarm
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r3
    h: 52e99e7ea7b1
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r3
    h: 52e99e7ea7b1
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r3
    h: 52e99e7ea7b1
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r3
    h: 52e99e7ea7b1
  review: drafted
---
