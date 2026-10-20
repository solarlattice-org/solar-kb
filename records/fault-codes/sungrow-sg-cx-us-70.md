---
id: fc:sungrow-sg-cx-us-70
type: FaultCode
name: Sungrow SG-CX-US 070
aliases:
- '070'
- '70'
- Sungrow 070
- Fan alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '070'
code_key: '70'
display_message: Fan alarm
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r5
    h: 0282b01ad881
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r5
    h: 0282b01ad881
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:fan-failure
  note: Applies when the fan does not run normally.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r5
    h: 0282b01ad881
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r5
    h: 0282b01ad881
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r5
    h: 0282b01ad881
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r5
    h: 0282b01ad881
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:fan-replacement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r5
    h: 0282b01ad881
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:warning
  note: Labelled as an alarm rather than a fault.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r5
    h: 0282b01ad881
  review: drafted
---
