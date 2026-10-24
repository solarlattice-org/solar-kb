---
id: fc:huawei-sun2000-45ktl-us-hv-d0-400
type: FaultCode
name: Huawei SUN2000-45KTL-US-HV-D0 400
aliases:
- '400'
- Huawei 400
- System Fault
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-45ktl-us-hv-d0
family_name: Huawei SUN2000-45KTL-US-HV-D0
code: '400'
code_key: '400'
display_message: System Fault
vendor_severity: Major
page: 119
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r2
    h: 2c4dcfc84ebf
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r2
    h: 2c4dcfc84ebf
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r5
    h: 1612f494ec6c
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r2
    h: 2c4dcfc84ebf
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r5
    h: 1612f494ec6c
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r2
    h: 2c4dcfc84ebf
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r5
    h: 1612f494ec6c
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r2
    h: 2c4dcfc84ebf
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the fault persists after the power cycle.
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r5
    h: 1612f494ec6c
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r2
    h: 2c4dcfc84ebf
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r5
    h: 1612f494ec6c
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=8.2
    h: db4d98f32335
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle AC and DC switches first; contact support if it persists.
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r5
    h: 1612f494ec6c
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r2
    h: 2c4dcfc84ebf
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:huawei-sun2000-45ktl-us-hv-d0
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r2
    h: 2c4dcfc84ebf
  review: drafted
---
