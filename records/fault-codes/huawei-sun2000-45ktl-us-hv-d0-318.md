---
id: fc:huawei-sun2000-45ktl-us-hv-d0-318
type: FaultCode
name: Huawei SUN2000-45KTL-US-HV-D0 318
aliases:
- '318'
- Huawei 318
- Abnormal Residual Current
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-45ktl-us-hv-d0
family_name: Huawei SUN2000-45KTL-US-HV-D0
code: '318'
code_key: '318'
display_message: Abnormal Residual Current
vendor_severity: Major
page: 118
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r3
    h: 5d3f9a245613
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r3
    h: 5d3f9a245613
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r1
    h: 53a521edab18
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r3
    h: 5d3f9a245613
  review: drafted
  review_note: 'support check: partial - Alarm is abnormal residual current, which is excessively high
    residual current, but ''leakage current'' is not named.'
- claim_id: c4
  rel: indicates
  target: fm:insulation-loss
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r1
    h: 53a521edab18
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r3
    h: 5d3f9a245613
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r1
    h: 53a521edab18
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r3
    h: 5d3f9a245613
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: detected_by
  target: method:insulation-resistance-test
  note: When the alarm repeats or persists
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r1
    h: 53a521edab18
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r3
    h: 5d3f9a245613
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r1
    h: 53a521edab18
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=8.2
    h: db4d98f32335
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r1
    h: 53a521edab18
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r3
    h: 5d3f9a245613
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:huawei-sun2000-45ktl-us-hv-d0
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r3
    h: 5d3f9a245613
  review: drafted
---
