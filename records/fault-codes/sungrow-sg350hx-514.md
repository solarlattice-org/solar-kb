---
id: fc:sungrow-sg350hx-514
type: FaultCode
name: Sungrow SG350HX 514
aliases:
- '514'
- Sungrow 514
- Meter Communication Abnormal Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '514'
code_key: '514'
display_message: Meter Communication Abnormal Alarm
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=33.r4
    h: fc8d5a2ed1e8
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r1
    h: fc8d5a2ed1e8
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:energy-meter
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r1
    h: fc8d5a2ed1e8
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:communication-cable-check
  note: Contact service if the alarm persists.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r1
    h: fc8d5a2ed1e8
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r1
    h: fc8d5a2ed1e8
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sungrow-sg350hx
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=33.r4
    h: fc8d5a2ed1e8
  review: drafted
---
