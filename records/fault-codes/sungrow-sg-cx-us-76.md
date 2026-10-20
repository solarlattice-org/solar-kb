---
id: fc:sungrow-sg-cx-us-76
type: FaultCode
name: Sungrow SG-CX-US 76
aliases:
- '76'
- Sungrow 76
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '76'
code_key: '76'
display_message: Device anomaly
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r8
    h: 07b2c8eb2e45
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r8
    h: 07b2c8eb2e45
  review: drafted
  review_note: 'support check: partial - Code 076 is described as ''Device anomaly'' with contact SUNGROW,
    which loosely matches an internal device fault but is generic.'
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r1
    h: e08f19fa548f
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r1
    h: e08f19fa548f
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  note: Inspect related wiring, terminals, foreign material and environment.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r1
    h: e08f19fa548f
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the anomaly persists.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r1
    h: e08f19fa548f
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r8
    h: 07b2c8eb2e45
  review: drafted
---
