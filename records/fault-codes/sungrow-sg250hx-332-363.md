---
id: fc:sungrow-sg250hx-332-363
type: FaultCode
name: Sungrow SG250HX 332-363
aliases:
- 332-363
- Sungrow 332-363
- Boost Capacitor Overvoltage Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: 332-363
code_key: 332-363
code_from: 332
code_to: 363
display_message: Boost Capacitor Overvoltage Alarm
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r3
    h: 9e2614a116ad
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:boost-capacitor-overvoltage
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r3
    h: 9e2614a116ad
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r3
    h: 9e2614a116ad
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  note: Inverter keeps running while the alarm is active.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r3
    h: 9e2614a116ad
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only after the wiring, terminal and environment checks; applies if the alarm persists.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r3
    h: 9e2614a116ad
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sungrow-sg250hx
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r3
    h: 9e2614a116ad
  review: drafted
---
