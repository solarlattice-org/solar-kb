---
id: fc:sungrow-sg-cx-us-105
type: FaultCode
name: Sungrow SG-CX-US 105
aliases:
- '105'
- Sungrow 105
- Protection self-check failure on grid side
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '105'
code_key: '105'
display_message: Protection self-check failure on grid side
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r4
    h: e3dfad5dad15
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r4
    h: e3dfad5dad15
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r4
    h: e3dfad5dad15
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r4
    h: e3dfad5dad15
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r4
    h: e3dfad5dad15
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r4
    h: e3dfad5dad15
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r4
    h: e3dfad5dad15
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r4
    h: e3dfad5dad15
  review: drafted
  review_note: 'support check: partial - Self-check failure needing restart or clearing implies a fault,
    but the classification is not explicit.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Restart or clear via App first; contact service if it persists.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r4
    h: e3dfad5dad15
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r4
    h: e3dfad5dad15
  review: drafted
---
