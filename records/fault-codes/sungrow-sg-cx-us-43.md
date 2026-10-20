---
id: fc:sungrow-sg-cx-us-43
type: FaultCode
name: Sungrow SG-CX-US 43
aliases:
- '43'
- Sungrow 43
- Low ambient temperature
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '43'
code_key: '43'
display_message: Low ambient temperature
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r1
    h: a5b9c9505cd8
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-undertemperature
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r3
    h: eb9ec451e098
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r1
    h: a5b9c9505cd8
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r3
    h: eb9ec451e098
  review: drafted
  review_note: 'support check: partial - The passage says to stop and disconnect the inverter, which implies
    a fault, but doesn''t state the classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r3
    h: eb9ec451e098
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r1
    h: a5b9c9505cd8
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Operator restarts once ambient temperature is back within operating range.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=41.r3
    h: eb9ec451e098
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r1
    h: a5b9c9505cd8
  review: drafted
---
