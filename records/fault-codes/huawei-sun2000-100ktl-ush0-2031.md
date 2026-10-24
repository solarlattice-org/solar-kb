---
id: fc:huawei-sun2000-100ktl-ush0-2031
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2031
aliases:
- '2031'
- Huawei 2031
- Phase Wire Short-Circuited to PE
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2031'
code_key: '2031'
display_message: Phase Wire Short-Circuited to PE
vendor_severity: Major
page: 119
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r4
    h: 01ef2742bfad
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r4
    h: 01ef2742bfad
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r4
    h: 01ef2742bfad
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r4
    h: 01ef2742bfad
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r4
    h: 01ef2742bfad
  review: drafted
  review_note: 'support check: partial - Measures say to check impedance of phase wire to PE, which is
    akin to insulation/impedance checking, but no insulation resistance…'
- claim_id: c6
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r4
    h: 01ef2742bfad
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r4
    h: 01ef2742bfad
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:huawei-sun2000-100ktl-ush0
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r4
    h: 01ef2742bfad
  review: drafted
---
