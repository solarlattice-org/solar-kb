---
id: fc:sungrow-sg-cx-us-4
type: FaultCode
name: Sungrow SG-CX-US 4
aliases:
- '4'
- Sungrow 4
- Grid undervoltage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '4'
code_key: '4'
display_message: Grid undervoltage
page: 90
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r2
    h: 74f93b8997f3
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r2
    h: 74f93b8997f3
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
  review_note: 'support check: partial - It is in a fault table, but the passages give no explicit fault-versus-warning
    classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r2
    h: 74f93b8997f3
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  review: drafted
  review_note: 'support check: partial - Reconnection implies disconnection, but production stop is not
    explicitly stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: If repeated, check grid, settings and AC cable, then contact service.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r2
    h: 74f93b8997f3
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r2
    h: 74f93b8997f3
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r2
    h: 74f93b8997f3
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r2
    h: 74f93b8997f3
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  review: drafted
- claim_id: c9
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r2
    h: 74f93b8997f3
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  review: drafted
---
