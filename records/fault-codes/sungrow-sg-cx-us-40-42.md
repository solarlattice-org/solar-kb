---
id: fc:sungrow-sg-cx-us-40-42
type: FaultCode
name: Sungrow SG-CX-US 40-42
aliases:
- 40-42
- Sungrow 40-42
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 40-42
code_key: 40-42
code_from: 40
code_to: 42
display_message: Device anomaly
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r4
    h: 8a5b02233bf8
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r4
    h: 8a5b02233bf8
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears on its own; otherwise power-cycle AC and DC after 15 minutes, then contact service.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r4
    h: 8a5b02233bf8
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r4
    h: 8a5b02233bf8
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the fault persists after restart.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=43.r4
    h: d22720cf1a21
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r4
    h: 8a5b02233bf8
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
