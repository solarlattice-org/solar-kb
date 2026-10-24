---
id: fc:sungrow-sg350hx-364-395
type: FaultCode
name: Sungrow SG350HX 364-395
aliases:
- 364-395
- Sungrow 364-395
- Boost Capacitor Overvoltage Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: 364-395
code_key: 364-395
code_from: 364
code_to: 395
display_message: Boost Capacitor Overvoltage Fault
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=35.r4
    h: 347a060e08dd
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:boost-capacitor-overvoltage
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r5
    h: 347a060e08dd
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r5
    h: 347a060e08dd
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle AC/DC after 15 minutes; contact service if it persists.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r5
    h: 347a060e08dd
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r5
    h: 347a060e08dd
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sungrow-sg350hx
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=35.r4
    h: 347a060e08dd
  review: drafted
---
