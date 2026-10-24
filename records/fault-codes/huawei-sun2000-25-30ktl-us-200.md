---
id: fc:huawei-sun2000-25-30ktl-us-200
type: FaultCode
name: Huawei SUN2000-25-30KTL-US 200
aliases:
- '200'
- Huawei 200
- DC Bus Voltage Fault
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-25-30ktl-us
family_name: Huawei SUN2000-25KTL-US / SUN2000-30KTL-US
code: '200'
code_key: '200'
display_message: DC Bus Voltage Fault
vendor_severity: Major
page: 97
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=38.r2
    h: b9523735f617
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=38.r2
    h: b9523735f617
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-link-fault
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=38.r2
    h: b9523735f617
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r4
    h: e68939271b75
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r1
    h: 374da4efa227
  review: drafted
  review_note: 'support check: partial - DC bus voltage fault and abnormal DC circuit are stated, which
    loosely matches DC link fault.'
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=38.r2
    h: b9523735f617
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r4
    h: e68939271b75
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=38.r2
    h: b9523735f617
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=8.2
    h: db4d98f32335
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: External causes recover automatically; internal causes 12/15 need a power cycle, then service
    if the fault persists
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=38.r2
    h: b9523735f617
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r4
    h: e68939271b75
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  note: For internal circuit causes 12/15
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=38.r2
    h: b9523735f617
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r4
    h: e68939271b75
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r1
    h: 374da4efa227
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the alarm persists
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=38.r2
    h: b9523735f617
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r1
    h: 374da4efa227
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:huawei-sun2000-25-30ktl-us
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=38.r2
    h: b9523735f617
  review: drafted
---
