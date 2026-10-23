---
id: fc:huawei-sun2000-25-30ktl-us-103
type: FaultCode
name: Huawei SUN2000-25-30KTL-US 103
aliases:
- '103'
- Huawei 103
- DC Over Voltage
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-25-30ktl-us
family_name: Huawei SUN2000-25KTL-US / SUN2000-30KTL-US
code: '103'
code_key: '103'
display_message: DC Over Voltage
vendor_severity: Major
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=37.r1
    h: 23546214be7d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=37.r1
    h: 23546214be7d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=37.r1
    h: 23546214be7d
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=52.r1
    h: b1c666901691
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r1
    h: 18c3bbe87d96
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=37.r1
    h: 23546214be7d
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=52.r1
    h: b1c666901691
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=37.r1
    h: 23546214be7d
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=52.r1
    h: b1c666901691
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r1
    h: 18c3bbe87d96
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Major severity means shutdown and no feed-in
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=37.r1
    h: 23546214be7d
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=8.2
    h: db4d98f32335
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Alarm clears by itself once the string configuration has been corrected
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=37.r1
    h: 23546214be7d
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=52.r1
    h: b1c666901691
  review: drafted
---
