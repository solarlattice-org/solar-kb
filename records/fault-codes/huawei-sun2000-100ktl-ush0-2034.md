---
id: fc:huawei-sun2000-100ktl-ush0-2034
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2034
aliases:
- '2034'
- Huawei 2034
- Grid Overvoltage
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2034'
code_key: '2034'
display_message: Grid Overvoltage
vendor_severity: Major
page: 120
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r2
    h: 19bc75c0c721
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r2
    h: 19bc75c0c721
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r2
    h: 19bc75c0c721
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r2
    h: 19bc75c0c721
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r2
    h: 19bc75c0c721
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:grid-settings-check
  note: Threshold change only with grid operator consent.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r2
    h: 19bc75c0c721
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=56.r2
    h: 19bc75c0c721
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: drafted
---
