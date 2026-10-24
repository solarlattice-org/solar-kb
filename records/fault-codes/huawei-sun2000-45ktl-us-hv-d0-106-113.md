---
id: fc:huawei-sun2000-45ktl-us-hv-d0-106-113
type: FaultCode
name: Huawei SUN2000-45KTL-US-HV-D0 106-113
aliases:
- 106-113
- Huawei 106-113
- Abnormal String 1-8
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-45ktl-us-hv-d0
family_name: Huawei SUN2000-45KTL-US-HV-D0
code: 106-113
code_key: 106-113
code_from: 106
code_to: 113
display_message: Abnormal String 1-8
vendor_severity: Warning
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r2
    h: 3cdeedc59a8a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r2
    h: 3cdeedc59a8a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:string-current-low
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r2
    h: 3cdeedc59a8a
  review: drafted
  review_note: 'support check: partial - The passage describes abnormal strings and checks whether the
    current is lower than other strings, but it does not state…'
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r2
    h: 3cdeedc59a8a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: detected_by
  target: method:string-current-measurement
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r2
    h: 3cdeedc59a8a
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r2
    h: 3cdeedc59a8a
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: sec=9.2
    h: 37ed3fc315be
  review: drafted
  review_note: 'support check: partial - Warning is defined as output power decreasing due to external
    factors, but this alarm''s own causes are shading or string…'
- claim_id: c7
  rel: applies_to
  target: prod:huawei-sun2000-45ktl-us-hv-d0
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r2
    h: 3cdeedc59a8a
  review: drafted
---
