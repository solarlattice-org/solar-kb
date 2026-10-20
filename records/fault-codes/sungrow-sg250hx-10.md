---
id: fc:sungrow-sg250hx-10
type: FaultCode
name: Sungrow SG250HX 10
aliases:
- '10'
- Sungrow 10
- Grid Power Outage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '10'
code_key: '10'
display_message: Grid Power Outage
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r3
    h: c338b4abeef8
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r3
    h: c338b4abeef8
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r3
    h: e37d4c329c9b
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r3
    h: c338b4abeef8
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
  review_note: 'support check: partial - The passages show it is a listed fault code in the troubleshooting
    table, but they give no explicit fault classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r3
    h: c338b4abeef8
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r3
    h: e37d4c329c9b
  review: drafted
  review_note: 'support check: partial - A grid outage followed by reconnection implies the inverter stops
    feeding in, but the passages don''t explicitly state a trip.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: If repeated, check grid supply, AC wiring and breaker, then contact service.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r3
    h: c338b4abeef8
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r3
    h: e37d4c329c9b
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r3
    h: c338b4abeef8
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r3
    h: e37d4c329c9b
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r3
    h: c338b4abeef8
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r3
    h: e37d4c329c9b
  review: drafted
  review_note: 'support check: partial - The AC cable check is a listed corrective step, but the passages
    don''t say the fault affects the cable.'
---
