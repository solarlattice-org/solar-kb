---
id: fc:huawei-sun2000-100ktl-ush0-2021
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2021
aliases:
- '2021'
- Huawei 2021
- AFCI Self-Check Failure
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2021'
code_key: '2021'
display_message: AFCI Self-Check Failure
vendor_severity: Major
page: 119
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r3
    h: 26fc6c571dd3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r3
    h: 26fc6c571dd3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r3
    h: 26fc6c571dd3
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r3
    h: 26fc6c571dd3
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r3
    h: 26fc6c571dd3
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r3
    h: 26fc6c571dd3
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle AC and DC first; contact service if fault persists.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r3
    h: 26fc6c571dd3
  review: drafted
---
