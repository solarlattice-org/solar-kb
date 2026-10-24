---
id: fc:huawei-sun2000-100ktl-ush0-2037
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2037
aliases:
- '2037'
- Huawei 2037
- Grid Underfrequency
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2037'
code_key: '2037'
display_message: Grid Underfrequency
vendor_severity: Major
page: 121
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=57.r2
    h: c35add4b5619
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=57.r2
    h: c35add4b5619
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=57.r2
    h: c35add4b5619
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=57.r2
    h: c35add4b5619
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=57.r2
    h: c35add4b5619
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:grid-settings-check
  note: Threshold change only with grid operator consent.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=57.r2
    h: c35add4b5619
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=57.r2
    h: c35add4b5619
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Frequent alarms escalate to frequency check and operator contact.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=57.r2
    h: c35add4b5619
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c9
  rel: applies_to
  target: prod:huawei-sun2000-100ktl-ush0
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=57.r2
    h: c35add4b5619
  review: drafted
---
