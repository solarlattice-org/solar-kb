---
id: fc:sungrow-sg200hx-514
type: FaultCode
name: Sungrow SG200HX 514
aliases:
- '514'
- Sungrow 514
- Meter Communication Abnormal Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: '514'
code_key: '514'
display_message: Meter Communication Abnormal Alarm
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r1
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
---
