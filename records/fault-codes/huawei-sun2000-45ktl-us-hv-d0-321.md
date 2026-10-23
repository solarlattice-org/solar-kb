---
id: fc:huawei-sun2000-45ktl-us-hv-d0-321
type: FaultCode
name: Huawei SUN2000-45KTL-US-HV-D0 321
aliases:
- '321'
- Huawei 321
- Cabinet Overtempe rature
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-45ktl-us-hv-d0
family_name: Huawei SUN2000-45KTL-US-HV-D0
code: '321'
code_key: '321'
display_message: Cabinet Overtempe rature
vendor_severity: Major
page: 118
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r4
    h: 8cc1cda60aae
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r4
    h: 8cc1cda60aae
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r2
    h: bdc729b2548c
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r4
    h: 8cc1cda60aae
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:high-ambient-temperature
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r2
    h: bdc729b2548c
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r4
    h: 8cc1cda60aae
  review: drafted
- claim_id: c5
  rel: indicates
  target: fm:fan-failure
  note: One of the listed causes besides poor ventilation and high ambient temperature
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r2
    h: bdc729b2548c
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r4
    h: 8cc1cda60aae
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r2
    h: bdc729b2548c
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r4
    h: 8cc1cda60aae
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r2
    h: bdc729b2548c
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r4
    h: 8cc1cda60aae
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If ventilation and ambient temperature are within requirements
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r4
    h: 8cc1cda60aae
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r2
    h: bdc729b2548c
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=8.2
    h: db4d98f32335
  review: drafted
---
