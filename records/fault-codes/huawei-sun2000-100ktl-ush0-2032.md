---
id: fc:huawei-sun2000-100ktl-ush0-2032
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2032
aliases:
- '2032'
- Huawei 2032
- Grid Loss
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2032'
code_key: '2032'
display_message: Grid Loss
vendor_severity: Major
page: 119
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r5
    h: d22262b4547e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r5
    h: d22262b4547e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r5
    h: d22262b4547e
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r5
    h: d22262b4547e
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-disconnect
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r5
    h: d22262b4547e
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r5
    h: d22262b4547e
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r5
    h: d22262b4547e
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Clears when grid returns; otherwise check AC cable and switch.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r5
    h: d22262b4547e
  review: drafted
---
