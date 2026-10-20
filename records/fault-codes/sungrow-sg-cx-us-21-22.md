---
id: fc:sungrow-sg-cx-us-21-22
type: FaultCode
name: Sungrow SG-CX-US 021-022
aliases:
- 021-022
- 21-22
- Sungrow 021-022
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 021-022
code_key: 21-22
code_from: 21
code_to: 22
display_message: Device anomaly
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r3
    h: 06a9bde43cd3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r3
    h: 06a9bde43cd3
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r3
    h: 06a9bde43cd3
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
    loc: tbl=50.r3
    h: 06a9bde43cd3
  review: drafted
  review_note: 'support check: partial - The row says to wait for the inverter to return to normal, which
    suggests auto-reset, but it also needs a…'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r3
    h: 06a9bde43cd3
  review: drafted
---
