---
id: fc:sungrow-sg250hx-608
type: FaultCode
name: Sungrow SG250HX 608
aliases:
- '608'
- Sungrow 608
- System Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '608'
code_key: '608'
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
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  review: drafted
- claim_id: c4
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
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Implied by the inverter-failure context and the instruction to wait for return to normal or restart.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
  review_note: 'support check: partial - The row implies the inverter needs restart, but it never states
    that production stops; the trip effect is inferred.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears by itself; if not, AC/DC power cycle restart, then manufacturer service if it
    persists.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  review: drafted
  review_note: 'support check: partial - ''Wait for the inverter to return to normal'' suggests self-recovery,
    but auto-reset is not explicitly stated, and manual restart is…'
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  note: Used when the fault does not clear by itself.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Used if the fault persists after a restart.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  review: drafted
---
