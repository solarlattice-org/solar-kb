---
id: fc:sungrow-sg250hx-36
type: FaultCode
name: Sungrow SG250HX 36
aliases:
- '36'
- Sungrow 36
- System Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '36'
code_key: '36'
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
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:clear-heat-dissipation-path
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:fan-replacement
  note: When a fan anomaly alarm is also present.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  review: drafted
- claim_id: c7
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
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: 'Escalation: switch restart after 15 minutes, then service if persistent.'
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  review: drafted
---
