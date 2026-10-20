---
id: fc:sungrow-sg250hx-901
type: FaultCode
name: Sungrow SG250HX 901
aliases:
- '901'
- Sungrow 901
- System Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '901'
code_key: '901'
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
  note: Row states the inverter can continue running while the alarm is flagged.
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
  note: Inspect related wiring, terminals, foreign materials and environmental abnormalities.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r1
    h: e08f19fa548f
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation only if the alarm persists after inspection and correction.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r1
    h: e08f19fa548f
  review: drafted
---
