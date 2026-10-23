---
id: fc:huawei-sun2000-100ktl-ush0-2012
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2012
aliases:
- '2012'
- Huawei 2012
- String current backfeed
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2012'
code_key: '2012'
display_message: String current backfeed
vendor_severity: Warning
page: 118
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r4
    h: 82f3b5a828cf
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r4
    h: 82f3b5a828cf
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:string-reverse-current
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r4
    h: 82f3b5a828cf
  review: drafted
  review_note: 'support check: partial - The alarm is named String current backfeed, which is close to
    reverse current, but the passages are truncated.'
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r4
    h: 82f3b5a828cf
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r1
    h: a7ce5507da5e
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Applies when the string has fewer series modules than other strings.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r4
    h: 82f3b5a828cf
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=55.r1
    h: a7ce5507da5e
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r4
    h: 82f3b5a828cf
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
