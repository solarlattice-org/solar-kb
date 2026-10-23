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
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r3
    h: 06a9bde43cd3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r3
    h: 06a9bde43cd3
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r3
    h: 06a9bde43cd3
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r3
    h: 06a9bde43cd3
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r3
    h: 06a9bde43cd3
  review: drafted
  review_note: 'support check: partial - The row says device anomaly requiring a restart, which loosely
    implies a fault, but ''fault'' is not explicitly stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: 'Escalation: power-cycle after 15 minutes, then contact service.'
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r3
    h: 06a9bde43cd3
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r3
    h: 06a9bde43cd3
  review: drafted
  review_note: 'support check: partial - Waiting for recovery is implied, and the power-cycle then service
    escalation is stated, but auto-reset is not explicit.'
---
