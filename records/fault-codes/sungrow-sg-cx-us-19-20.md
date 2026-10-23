---
id: fc:sungrow-sg-cx-us-19-20
type: FaultCode
name: Sungrow SG-CX-US 019-020
aliases:
- 019-020
- 19-20
- Sungrow 019-020
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 019-020
code_key: 19-20
code_from: 19
code_to: 20
display_message: Device anomaly
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r2
    h: 98f7472ec6a0
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r2
    h: 98f7472ec6a0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r2
    h: 98f7472ec6a0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r2
    h: 98f7472ec6a0
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r2
    h: 98f7472ec6a0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r2
    h: 98f7472ec6a0
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: 'Escalation: power-cycle after 15 minutes, then contact service.'
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r2
    h: 98f7472ec6a0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r2
    h: 98f7472ec6a0
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
