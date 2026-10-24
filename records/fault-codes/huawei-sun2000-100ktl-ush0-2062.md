---
id: fc:huawei-sun2000-100ktl-ush0-2062
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2062
aliases:
- '2062'
- Huawei 2062
- Low Insulation Resistance
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2062'
code_key: '2062'
display_message: Low Insulation Resistance
vendor_severity: Major
page: 122
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r4
    h: 12e4573bb704
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r4
    h: 12e4573bb704
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r4
    h: 12e4573bb704
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:insulation-loss
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r4
    h: 12e4573bb704
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r4
    h: 12e4573bb704
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r4
    h: 12e4573bb704
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r4
    h: 12e4573bb704
  review: drafted
  review_note: 'support check: partial - Evidence says to check impedance between PV string and PE, which
    is similar to an insulation resistance test but is…'
- claim_id: c8
  rel: mitigated_by
  target: mit:ground-conductor-check
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r4
    h: 12e4573bb704
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r4
    h: 12e4573bb704
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:huawei-sun2000-100ktl-ush0
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=58.r4
    h: 12e4573bb704
  review: drafted
---
