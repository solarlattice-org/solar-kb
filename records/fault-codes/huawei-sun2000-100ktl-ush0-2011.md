---
id: fc:huawei-sun2000-100ktl-ush0-2011
type: FaultCode
name: Huawei SUN2000-100KTL-USH0 2011
aliases:
- '2011'
- Huawei 2011
- String Reverse Connection
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-100ktl-ush0
family_name: Huawei SUN2000-100KTL-USH0
code: '2011'
code_key: '2011'
display_message: String Reverse Connection
vendor_severity: Major
page: 118
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r3
    h: 828d432ce27c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r3
    h: 828d432ce27c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r3
    h: 828d432ce27c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r3
    h: 828d432ce27c
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r3
    h: 828d432ce27c
  review: drafted
  review_note: 'support check: partial - The passages say to check whether the string is reversely connected,
    which is not clearly a polarity measurement method.'
- claim_id: c6
  rel: mitigated_by
  target: mit:polarity-correction
  note: Correct only at night once string current is low and DC switches are off.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r3
    h: 828d432ce27c
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r3
    h: 828d432ce27c
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=8.3
    h: 06c0aa7071c6
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:huawei-sun2000-100ktl-ush0
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=54.r3
    h: 828d432ce27c
  review: drafted
---
