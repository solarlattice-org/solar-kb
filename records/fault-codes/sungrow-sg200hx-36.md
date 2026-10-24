---
id: fc:sungrow-sg200hx-36
type: FaultCode
name: Sungrow SG200HX 036
aliases:
- '036'
- '36'
- Sungrow 036
- System Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: '036'
code_key: '36'
display_message: System Fault
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r1
    h: b64052214890
  review: drafted
- claim_id: c2
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
- claim_id: c3
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
  review: drafted
  review_note: 'support check: partial - 036 appears in the ''System Fault'' row, which supports a fault
    label, but device-stop behavior is not explicitly stated.'
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
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
- claim_id: c8
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
- claim_id: c9
  rel: applies_to
  target: prod:sungrow-sg200hx
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r1
    h: b64052214890
  review: drafted
---
