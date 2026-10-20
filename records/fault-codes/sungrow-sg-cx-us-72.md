---
id: fc:sungrow-sg-cx-us-72
type: FaultCode
name: Sungrow SG-CX-US 072
aliases:
- '072'
- '72'
- Sungrow 072
- DC-side SPD alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '072'
code_key: '72'
display_message: DC-side SPD alarm
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:spd-alarm
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:surge-protection-device
  note: DC-side surge protector.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  note: Labelled as an alarm rather than a fault.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Normal case clears on its own; escalate to manual AC/DC power cycle.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  review: drafted
---
