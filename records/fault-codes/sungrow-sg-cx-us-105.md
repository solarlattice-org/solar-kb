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
  rel: reports
  target: symptom:self-test-failure
  note: Grid-side protection self-check.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r4
    h: e3dfad5dad15
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r4
    h: e3dfad5dad15
  review: drafted
  review_note: 'support check: partial - Row doesn''t name a component; inverter restart is implied but
    the affected component is only loosely implied.'
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Restart or clear via app first; contact manufacturer if it persists.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r4
    h: e3dfad5dad15
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r4
    h: e3dfad5dad15
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the failure persists after restart.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r4
    h: e3dfad5dad15
  review: drafted
---
