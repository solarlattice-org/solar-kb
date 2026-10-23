---
id: fc:huawei-sun2000-25-30ktl-us-412
type: FaultCode
name: Huawei SUN2000-25-30KTL-US 412
aliases:
- '412'
- Huawei 412
- DC Arc Fault
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-25-30ktl-us
family_name: Huawei SUN2000-25KTL-US / SUN2000-30KTL-US
code: '412'
code_key: '412'
display_message: DC Arc Fault
vendor_severity: Major
page: 102
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r3
    h: f7f0a54214b7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r3
    h: f7f0a54214b7
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r3
    h: f7f0a54214b7
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r3
    h: f7f0a54214b7
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r5
    h: 4d991c2dbd56
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r3
    h: f7f0a54214b7
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r5
    h: 4d991c2dbd56
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r3
    h: f7f0a54214b7
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=8.2
    h: db4d98f32335
  review: drafted
---
