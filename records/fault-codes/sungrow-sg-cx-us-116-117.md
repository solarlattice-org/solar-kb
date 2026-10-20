---
id: fc:sungrow-sg-cx-us-116-117
type: FaultCode
name: Sungrow SG-CX-US 116-117
aliases:
- 116-117
- Sungrow 116-117
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 116-117
code_key: 116-117
code_from: 116
code_to: 117
display_message: Device anomaly
page: 97
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r2
    h: 6bdc7459089f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r2
    h: 6bdc7459089f
  review: drafted
  review_note: 'support check: partial - Row says device anomaly, which loosely matches internal device
    fault.'
- claim_id: c3
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r2
    h: 6bdc7459089f
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Normal case clears on its own; escalate to manual AC/DC power cycle.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r2
    h: 6bdc7459089f
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r2
    h: 6bdc7459089f
  review: drafted
---
