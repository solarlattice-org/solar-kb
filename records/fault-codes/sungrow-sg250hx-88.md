---
id: fc:sungrow-sg250hx-88
type: FaultCode
name: Sungrow SG250HX 88
aliases:
- '88'
- Sungrow 88
- Electric Arc Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '88'
code_key: '88'
display_message: Electric Arc Fault
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r3
    h: 133cd990681b
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r3
    h: 133cd990681b
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r3
    h: 133cd990681b
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r3
    h: 133cd990681b
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  review: drafted
  review_note: 'support check: partial - Terminals and fuses are mentioned, loose terminals/weak contact,
    but ''DC connector'' is not explicitly named.'
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r3
    h: 133cd990681b
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  review: drafted
  review_note: 'support check: partial - Checking for damaged cables, loose terminals and burnt parts
    implies visual inspection but it is not stated.'
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r3
    h: 133cd990681b
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:cable-replacement
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r3
    h: 133cd990681b
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r3
    h: 133cd990681b
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
  review_note: 'support check: partial - Arc fault must be cleared and intervention is needed, implying
    a fault, but the classification isn''t explicitly stated.'
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  note: Inverter returns to normal only after the arc fault is cleared.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r3
    h: 133cd990681b
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  review: drafted
  review_note: 'support check: partial - Inverter returns to normal after clearing the arc fault implies
    it stopped, but stopping production is not explicitly stated.'
- claim_id: c10
  rel: has_recovery
  target: ec:manual-reset
  note: Fault cleared via App or LCD after repair; service if it persists.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r3
    h: 133cd990681b
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  review: drafted
- claim_id: c11
  rel: applies_to
  target: prod:sungrow-sg250hx
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r3
    h: 133cd990681b
  review: drafted
---
