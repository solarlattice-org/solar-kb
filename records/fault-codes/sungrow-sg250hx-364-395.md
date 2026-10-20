---
id: fc:sungrow-sg250hx-364-395
type: FaultCode
name: Sungrow SG250HX 364-395
aliases:
- 364-395
- Sungrow 364-395
- Boost Capacitor Overvoltage Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: 364-395
code_key: 364-395
code_from: 364
code_to: 395
display_message: Boost Capacitor Overvoltage Fault
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r4
    h: aec721cb344b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:boost-capacitor-overvoltage
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r4
    h: aec721cb344b
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r4
    h: aec721cb344b
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Implied because the inverter must be restarted.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r4
    h: aec721cb344b
  review: drafted
  review_note: 'support check: partial - The row requires an inverter restart, which implies stopping,
    but production stop is not stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: First a delayed AC/DC power cycle; contact service if the fault remains.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r4
    h: aec721cb344b
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r4
    h: aec721cb344b
  review: drafted
---
