---
id: fc:huawei-sun2000-45ktl-us-hv-d0-410
type: FaultCode
name: Huawei SUN2000-45KTL-US-HV-D0 410
aliases:
- '410'
- Huawei 410
- Abnormal Auxiliary Power
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-45ktl-us-hv-d0
family_name: Huawei SUN2000-45KTL-US-HV-D0
code: '410'
code_key: '410'
display_message: Abnormal Auxiliary Power
vendor_severity: Major
page: 119
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r3
    h: ab1a62a388fa
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r3
    h: ab1a62a388fa
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r1
    h: 956f7f83d356
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r3
    h: ab1a62a388fa
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - The passages describe an abnormal voltage on the sampling control
    board from a faulty power chip or detection circuit, but…'
- claim_id: c4
  rel: indicates
  target: fm:internal-power-supply-fault
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r1
    h: 956f7f83d356
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r3
    h: ab1a62a388fa
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:control-board
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r1
    h: 956f7f83d356
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r3
    h: ab1a62a388fa
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the alarm persists after automatic restart.
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r1
    h: 956f7f83d356
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r3
    h: ab1a62a388fa
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r1
    h: 956f7f83d356
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r3
    h: ab1a62a388fa
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Restarts automatically once rectified; support if persistent.
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r1
    h: 956f7f83d356
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r3
    h: ab1a62a388fa
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:huawei-sun2000-45ktl-us-hv-d0
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=58.r3
    h: ab1a62a388fa
  review: drafted
---
