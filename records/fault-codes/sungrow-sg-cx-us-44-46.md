---
id: fc:sungrow-sg-cx-us-44-46
type: FaultCode
name: Sungrow SG-CX-US 044-046
aliases:
- 044-046
- 44-46
- Sungrow 044-046
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 044-046
code_key: 44-46
code_from: 44
code_to: 46
display_message: Device anomaly
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r2
    h: 34ef19307761
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r2
    h: 34ef19307761
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r2
    h: 34ef19307761
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
  review_note: 'support check: partial - The row says device anomaly, and u3 only says fault codes are
    listed, so the fault class is implied rather…'
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Waiting clears the normal case; otherwise do a delayed AC/DC restart.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r2
    h: 34ef19307761
  review: drafted
  review_note: 'support check: partial - The row says to wait for the inverter to return to normal, which
    suggests auto-reset, but the delayed restart is…'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r2
    h: 34ef19307761
  review: drafted
---
