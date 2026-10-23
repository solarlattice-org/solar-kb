---
id: fc:huawei-sun2000-100ktl-ush0-2013
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2013
aliases:
- '2013'
- Huawei 2013
- Abnormal String Power
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2013'
code_key: '2013'
display_message: Abnormal String Power
vendor_severity: Warning
page: 119
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r2
    h: a95bcc750915
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r2
    h: a95bcc750915
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:string-current-low
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r2
    h: a95bcc750915
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r2
    h: a95bcc750915
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:string-current-measurement
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r2
    h: a95bcc750915
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  note: Inspect for damage when string is clean and unshaded.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r2
    h: a95bcc750915
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:avoid-partial-shading
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r2
    h: a95bcc750915
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When actual string count differs from configured count.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r2
    h: a95bcc750915
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r2
    h: a95bcc750915
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: drafted
---
