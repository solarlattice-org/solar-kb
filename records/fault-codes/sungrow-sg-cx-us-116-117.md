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
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r2
    h: 747d97e2371d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r2
    h: 6bdc7459089f
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r2
    h: 747d97e2371d
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r2
    h: 6bdc7459089f
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r2
    h: 747d97e2371d
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: First wait for self-recovery; then power-cycle AC and DC; then contact service.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r2
    h: 6bdc7459089f
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r2
    h: 747d97e2371d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Passages say wait for the inverter to return to normal (self-recovery),
    then power cycle, then contact service (u14), but they…'
- claim_id: c6
  rel: applies_to
  target: prod:sungrow-sg-cx-us
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r2
    h: 6bdc7459089f
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r2
    h: 747d97e2371d
  review: drafted
---
