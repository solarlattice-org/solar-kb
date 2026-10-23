---
id: fc:sungrow-sg-cx-us-36
type: FaultCode
name: Sungrow SG-CX-US 036
aliases:
- '036'
- '36'
- Sungrow 036
- Temperature anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '036'
code_key: '36'
display_message: Temperature anomaly
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r5
    h: a74a3da25ad0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  note: Power module temperature beyond safe range.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r5
    h: a74a3da25ad0
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r5
    h: a74a3da25ad0
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Per system fault row; escalation is restart, then service.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
  review_note: 'support check: partial - The system fault row says wait for the inverter to return to
    normal, then restart, then service, but doesn''t explicitly…'
- claim_id: c6
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r5
    h: a74a3da25ad0
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:clear-heat-dissipation-path
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r5
    h: a74a3da25ad0
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:fan-replacement
  note: When a fan anomaly alarm is also present.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r5
    h: a74a3da25ad0
  review: drafted
- claim_id: c9
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r5
    h: a74a3da25ad0
  review: drafted
  review_note: 'support check: partial - Cooling fan is only referenced via the 070 fan anomaly check
    and replacement, not stated as directly affected by 036.'
---
