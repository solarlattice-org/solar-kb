---
id: fc:huawei-sun2000-25-30ktl-us-301
type: FaultCode
name: Huawei SUN2000-25-30KTL-US 301
aliases:
- '301'
- Huawei 301
- Grid Voltage Abnormal
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-25-30ktl-us
family_name: Huawei SUN2000-25KTL-US / SUN2000-30KTL-US
code: '301'
code_key: '301'
display_message: Grid Voltage Abnormal
vendor_severity: Major
page: 98
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r2
    h: 2feb59c683c4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r2
    h: 2feb59c683c4
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-voltage-out-of-range
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r2
    h: 2feb59c683c4
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=55.r2
    h: b7b0f9eea084
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r2
    h: 2feb59c683c4
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=55.r2
    h: b7b0f9eea084
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r2
    h: 2feb59c683c4
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=55.r2
    h: b7b0f9eea084
  review: drafted
- claim_id: c6
  rel: reports
  target: symptom:phase-imbalance
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=40.r1
    h: 2626070b1a42
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=55.r2
    h: b7b0f9eea084
  review: drafted
- claim_id: c7
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=40.r1
    h: 2626070b1a42
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=55.r2
    h: b7b0f9eea084
  review: drafted
- claim_id: c8
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r2
    h: 2feb59c683c4
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=40.r1
    h: 2626070b1a42
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=56.r1
    h: d0831968242d
  review: drafted
  review_note: 'support check: partial - The AC circuit, output cables and phase-to-PE impedance are involved,
    but impact on the AC cable is only implied.'
- claim_id: c9
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r2
    h: 2feb59c683c4
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=40.r1
    h: 2626070b1a42
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=55.r2
    h: b7b0f9eea084
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:grid-settings-check
  note: Protection thresholds changed only with the grid operator's consent
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r2
    h: 2feb59c683c4
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=55.r2
    h: b7b0f9eea084
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r2
    h: 2feb59c683c4
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=40.r1
    h: 2626070b1a42
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=56.r1
    h: d0831968242d
  review: drafted
- claim_id: c12
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r2
    h: 2feb59c683c4
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=8.2
    h: db4d98f32335
  review: drafted
- claim_id: c13
  rel: has_recovery
  target: ec:auto-reset
  note: Occasional grid excursions recover automatically; frequent ones need a grid check and settings
    review
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r2
    h: 2feb59c683c4
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=55.r2
    h: b7b0f9eea084
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
