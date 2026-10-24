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
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r4
    h: 53fe3ee9226d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r4
    h: 53fe3ee9226d
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r4
    h: 53fe3ee9226d
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r4
    h: 53fe3ee9226d
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r4
    h: 53fe3ee9226d
  review: drafted
  review_note: 'support check: partial - The row says device anomaly requiring a restart, which loosely
    implies a fault, but ''fault'' is not explicitly stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: 'Escalation: power-cycle after 15 minutes, then contact service.'
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r4
    h: 53fe3ee9226d
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r4
    h: 53fe3ee9226d
  review: drafted
  review_note: 'support check: partial - Waiting for recovery is implied, and the escalation is stated,
    but auto-reset is not explicit.'
- claim_id: c6
  rel: applies_to
  target: prod:sungrow-sg-cx-us
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r4
    h: 53fe3ee9226d
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r4
    h: 53fe3ee9226d
  review: drafted
---
