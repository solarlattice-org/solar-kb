---
id: fc:huawei-sun2000-100ktl-ush0-2033
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2033
aliases:
- '2033'
- Huawei 2033
- Grid Undervoltage
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2033'
code_key: '2033'
display_message: Grid Undervoltage
vendor_severity: Major
page: 119
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r6
    h: 9829b1f4d742
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r6
    h: 9829b1f4d742
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r6
    h: 9829b1f4d742
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r6
    h: 9829b1f4d742
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Frequent or persistent alarms escalate to grid and AC circuit checks.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r6
    h: 9829b1f4d742
  review: drafted
  review_note: 'support check: partial - Auto recovery is stated, but the escalation to grid and AC circuit
    checks is truncated in the passage.'
---
