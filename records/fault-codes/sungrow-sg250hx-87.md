---
id: fc:sungrow-sg250hx-87
type: FaultCode
name: Sungrow SG250HX 87
aliases:
- '87'
- Sungrow 87
- System Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '87'
code_key: '87'
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
  rel: indicates
  target: fm:arc-detector-failure
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r2
    h: 51764d4962cb
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r2
    h: 51764d4962cb
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r2
    h: 51764d4962cb
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:arc-board-connector-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r2
    h: 51764d4962cb
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the condition persists after checking cabling and surroundings.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r2
    h: 51764d4962cb
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  review: drafted
---
