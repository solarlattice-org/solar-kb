---
id: fc:huawei-sun2000-100ktl-ush0-2036
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2036
aliases:
- '2036'
- Huawei 2036
- Grid Overfrequency
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2036'
code_key: '2036'
display_message: Grid Overfrequency
vendor_severity: Major
page: 120
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r4
    h: 8d0d670b411c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r4
    h: 8d0d670b411c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r4
    h: 8d0d670b411c
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r4
    h: 8d0d670b411c
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=57.r1
    h: aa2e45f09028
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r4
    h: 8d0d670b411c
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Frequent alarms escalate to frequency check and operator contact.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r4
    h: 8d0d670b411c
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:huawei-sun2000-100ktl-ush0
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r4
    h: 8d0d670b411c
  review: drafted
---
