---
id: fc:huawei-sun2000-100ktl-ush0-2001
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2001
aliases:
- '2001'
- Huawei 2001
- High string input voltage
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2001'
code_key: '2001'
display_message: High string input voltage
vendor_severity: Major
page: 118
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r1
    h: adf353208ad7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r1
    h: adf353208ad7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r1
    h: adf353208ad7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r1
    h: adf353208ad7
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r1
    h: adf353208ad7
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r1
    h: adf353208ad7
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Alarm clears once the string configuration is corrected.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r1
    h: adf353208ad7
  review: drafted
---
