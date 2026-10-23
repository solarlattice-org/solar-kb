---
id: fc:huawei-sun2000-100ktl-ush0-2065
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2065
aliases:
- '2065'
- Huawei 2065
- Upgrade Failed
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2065'
code_key: '2065'
display_message: Upgrade Failed
vendor_severity: Minor
page: 123
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=59.r3
    h: 7c4803c7596f
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=59.r3
    h: 7c4803c7596f
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=59.r3
    h: 7c4803c7596f
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:retry-update
  note: Repeated failures escalate to the dealer.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=59.r3
    h: 7c4803c7596f
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  note: 'Minor severity: inverter keeps exporting power.'
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=59.r3
    h: 7c4803c7596f
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: drafted
---
