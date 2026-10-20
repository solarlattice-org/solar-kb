---
id: fc:sungrow-sg-cx-us-24-25
type: FaultCode
name: Sungrow SG-CX-US 024-025
aliases:
- 024-025
- 24-25
- Sungrow 024-025
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 024-025
code_key: 24-25
code_from: 24
code_to: 25
display_message: Device anomaly
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r4
    h: 53fe3ee9226d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r4
    h: 53fe3ee9226d
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r4
    h: 53fe3ee9226d
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
  review_note: 'support check: partial - The row says device anomaly, and u3 only says fault codes are
    listed, so the fault class is implied rather…'
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Waiting clears the normal case; next a delayed AC/DC restart, then service.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r4
    h: 53fe3ee9226d
  review: drafted
  review_note: 'support check: partial - The row says to wait for the inverter to return to normal, which
    suggests auto-reset, but it also needs a…'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r4
    h: 53fe3ee9226d
  review: drafted
---
