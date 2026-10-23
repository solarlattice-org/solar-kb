---
id: fc:sungrow-sg350hx-75
type: FaultCode
name: Sungrow SG350HX 75
aliases:
- '75'
- Sungrow 75
- Inverter Parallel Communication Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '75'
code_key: '75'
display_message: Inverter Parallel Communication Alarm
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r1
    h: 6c672d899eff
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r3
    h: 5a617aa68a17
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:communication-cable-check
  note: Contact service if the alarm persists.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r3
    h: 5a617aa68a17
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r3
    h: 5a617aa68a17
  review: drafted
---
