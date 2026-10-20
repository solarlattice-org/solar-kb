---
id: fc:sungrow-sg-cx-us-59-60
type: FaultCode
name: Sungrow SG-CX-US 059-060
aliases:
- 059-060
- 59-60
- Sungrow 059-060
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 059-060
code_key: 59-60
code_from: 59
code_to: 60
display_message: Device anomaly
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Normal case clears on its own; escalate to manual AC/DC power cycle, then manufacturer service.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the anomaly persists after restart.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  review: drafted
---
