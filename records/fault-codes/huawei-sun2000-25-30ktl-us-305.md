---
id: fc:huawei-sun2000-25-30ktl-us-305
type: FaultCode
name: Huawei SUN2000-25-30KTL-US 305
aliases:
- '305'
- Huawei 305
- Frequency Abnormal
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-25-30ktl-us
family_name: Huawei SUN2000-25KTL-US / SUN2000-30KTL-US
code: '305'
code_key: '305'
display_message: Frequency Abnormal
vendor_severity: Major
page: 100
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r1
    h: cfa68d1b16a8
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r1
    h: cfa68d1b16a8
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r1
    h: cfa68d1b16a8
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=56.r2
    h: 2e215ad1b97b
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r1
    h: cfa68d1b16a8
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=56.r2
    h: 2e215ad1b97b
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:grid-frequency-out-of-range
  note: Includes an excessive rate of frequency change, cause 5
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r1
    h: cfa68d1b16a8
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=56.r2
    h: 2e215ad1b97b
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r1
    h: cfa68d1b16a8
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=56.r2
    h: 2e215ad1b97b
  review: drafted
  review_note: 'support check: partial - Alarm is about grid frequency being abnormal, but passages do
    not explicitly state it is detected by frequency measurement.'
- claim_id: c7
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r1
    h: cfa68d1b16a8
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=56.r2
    h: 2e215ad1b97b
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r1
    h: 493026a89642
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:grid-settings-check
  note: Protection thresholds changed only with the grid operator's consent
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r1
    h: cfa68d1b16a8
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=56.r2
    h: 2e215ad1b97b
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r1
    h: cfa68d1b16a8
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=8.2
    h: db4d98f32335
  review: drafted
- claim_id: c10
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r1
    h: cfa68d1b16a8
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=56.r2
    h: 2e215ad1b97b
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r1
    h: 493026a89642
  review: drafted
---
