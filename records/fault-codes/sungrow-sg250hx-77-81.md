---
id: fc:sungrow-sg250hx-77-81
type: FaultCode
name: Sungrow SG250HX 77-81
aliases:
- 77-81
- Sungrow 77-81
- System Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: 77-81
code_key: 77-81
code_from: 77
code_to: 81
display_message: System Alarm
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r1
    h: e08f19fa548f
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r1
    h: e08f19fa548f
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r1
    h: e08f19fa548f
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:visual-inspection
  note: Inspect related wiring, terminals, foreign material and environment.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r1
    h: e08f19fa548f
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the alarm persists after checks.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r1
    h: e08f19fa548f
  review: drafted
---
