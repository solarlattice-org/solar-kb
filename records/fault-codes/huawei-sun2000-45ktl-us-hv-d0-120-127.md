---
id: fc:huawei-sun2000-45ktl-us-hv-d0-120-127
type: FaultCode
name: Huawei SUN2000-45KTL-US-HV-D0 120-127
aliases:
- 120-127
- Huawei 120-127
- String 1-8 Reversed
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-45ktl-us-hv-d0
family_name: Huawei SUN2000-45KTL-US-HV-D0
code: 120-127
code_key: 120-127
code_from: 120
code_to: 127
display_message: String 1-8 Reversed
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r3
    h: f53d68c14ac1
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r3
    h: f53d68c14ac1
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r3
    h: f53d68c14ac1
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:polarity-correction
  note: For cause 1, reversed string connection.
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r3
    h: f53d68c14ac1
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: For cause 2, too few modules in series.
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r3
    h: f53d68c14ac1
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  note: Major for cause 1; cause 2 is only a warning.
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r3
    h: f53d68c14ac1
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: sec=9.2
    h: 37ed3fc315be
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Major (cause 1) is a shutdown fault, but cause 2 is a warning;
    fault class holds only for cause 1.'
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  note: Holds for cause 1 (Major); cause 2 warning implies reduced output.
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r3
    h: f53d68c14ac1
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: sec=9.2
    h: 37ed3fc315be
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:huawei-sun2000-45ktl-us-hv-d0
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=53.r3
    h: f53d68c14ac1
  review: drafted
---
