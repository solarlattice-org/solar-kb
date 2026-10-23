---
id: fc:huawei-sun2000-25-30ktl-us-313
type: FaultCode
name: Huawei SUN2000-25-30KTL-US 313
aliases:
- '313'
- Huawei 313
- Low Array Insulation Resistance
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-25-30ktl-us
family_name: Huawei SUN2000-25KTL-US / SUN2000-30KTL-US
code: '313'
code_key: '313'
display_message: Low Array Insulation Resistance
vendor_severity: Major
page: 100
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r2
    h: d9e7fcd4952e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r2
    h: d9e7fcd4952e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r2
    h: d9e7fcd4952e
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r2
    h: 641402213d00
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:insulation-loss
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r2
    h: d9e7fcd4952e
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r2
    h: 641402213d00
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r2
    h: d9e7fcd4952e
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r2
    h: 641402213d00
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r2
    h: d9e7fcd4952e
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r2
    h: 641402213d00
  review: drafted
  review_note: 'support check: partial - Passages say to check the insulation resistance of strings, but
    not that the alarm is detected by an insulation resistance test.'
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only when low resistance is due to rainy or moist conditions, not a short circuit
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r2
    h: d9e7fcd4952e
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r2
    h: 641402213d00
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=41.r2
    h: d9e7fcd4952e
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=8.2
    h: db4d98f32335
  review: drafted
---
