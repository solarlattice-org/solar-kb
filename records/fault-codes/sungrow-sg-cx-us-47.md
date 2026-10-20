---
id: fc:sungrow-sg-cx-us-47
type: FaultCode
name: Sungrow SG-CX-US 047
aliases:
- '047'
- '47'
- Sungrow 047
- PV input configuration abnormal
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '047'
code_key: '47'
display_message: PV input configuration abnormal
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r3
    h: 96a10b9de9c0
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r3
    h: 96a10b9de9c0
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r3
    h: 96a10b9de9c0
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
  review_note: 'support check: partial - The row describes a configuration abnormality, and u3 only says
    fault codes are listed, so the fault class is implied…'
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: An operator shuts down the inverter and resets the PV input mode; contact service if the fault
    persists.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r3
    h: 96a10b9de9c0
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r3
    h: 96a10b9de9c0
  review: drafted
  review_note: 'support check: partial - The row says to shut down and disconnect the inverter, but the
    fault is a PV input configuration or mode…'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-parameter-change
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r3
    h: 96a10b9de9c0
  review: drafted
---
