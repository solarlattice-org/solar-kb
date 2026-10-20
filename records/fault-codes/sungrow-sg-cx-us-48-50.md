---
id: fc:sungrow-sg-cx-us-48-50
type: FaultCode
name: Sungrow SG-CX-US 048-050
aliases:
- 048-050
- 48-50
- Sungrow 048-050
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 048-050
code_key: 48-50
code_from: 48
code_to: 50
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
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
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
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  review: drafted
  review_note: 'support check: partial - The row says to wait for the inverter to return to normal, which
    suggests auto-reset, but it also needs a…'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  review: drafted
---
