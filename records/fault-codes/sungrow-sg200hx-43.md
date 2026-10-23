---
id: fc:sungrow-sg200hx-43
type: FaultCode
name: Sungrow SG200HX 043
aliases:
- '043'
- '43'
- Sungrow 043
- Excessively Low Ambient Temperature
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: '043'
code_key: '43'
display_message: Excessively Low Ambient Temperature
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r3
    h: 1268b23bbfb3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-undertemperature
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r1
    h: a5b9c9505cd8
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r1
    h: a5b9c9505cd8
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r3
    h: 1268b23bbfb3
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r1
    h: a5b9c9505cd8
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r1
    h: a5b9c9505cd8
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r3
    h: 1268b23bbfb3
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Inverter cannot operate below its temperature range and is shut down.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r1
    h: a5b9c9505cd8
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r1
    h: a5b9c9505cd8
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r3
    h: 1268b23bbfb3
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Operator restarts once ambient temperature is back within operating range.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r1
    h: a5b9c9505cd8
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r1
    h: a5b9c9505cd8
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r3
    h: 1268b23bbfb3
  review: drafted
---
