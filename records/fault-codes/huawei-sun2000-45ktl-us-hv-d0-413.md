---
id: fc:huawei-sun2000-45ktl-us-hv-d0-413
type: FaultCode
name: Huawei SUN2000-45KTL-US-HV-D0 413
aliases:
- '413'
- Huawei 413
- Abnormal PV String Connectio n
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-45ktl-us-hv-d0
family_name: Huawei SUN2000-45KTL-US-HV-D0
code: '413'
code_key: '413'
display_message: Abnormal PV String Connectio n
vendor_severity: Major
page: 119
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r6
    h: b10dca48ffc1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r6
    h: b10dca48ffc1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:pv-input-abnormal
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r6
    h: b10dca48ffc1
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=59.r1
    h: ded585775bec
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r6
    h: b10dca48ffc1
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=59.r1
    h: ded585775bec
  review: drafted
  review_note: 'support check: partial - The passages say the PV string does not properly connect to the
    MPPT circuit, which only loosely implies a PV…'
- claim_id: c5
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r6
    h: b10dca48ffc1
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r6
    h: b10dca48ffc1
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: sec=9.2
    h: 37ed3fc315be
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
