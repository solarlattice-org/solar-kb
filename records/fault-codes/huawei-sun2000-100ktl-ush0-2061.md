---
id: fc:huawei-sun2000-100ktl-ush0-2061
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2061
aliases:
- '2061'
- Huawei 2061
- Abnormal Grounding
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2061'
code_key: '2061'
display_message: Abnormal Grounding
vendor_severity: Major
page: 122
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r3
    h: a3d5bcb7d9bc
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r3
    h: a3d5bcb7d9bc
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:missing-ground-connection
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r3
    h: a3d5bcb7d9bc
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:ground-conductor-check
  note: Also verify isolation transformer on output when PV string output is grounded.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r3
    h: a3d5bcb7d9bc
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r3
    h: a3d5bcb7d9bc
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:huawei-sun2000-100ktl-ush0
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r3
    h: a3d5bcb7d9bc
  review: drafted
---
