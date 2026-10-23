---
id: fc:chint-sch-350ktl-warn100
type: FaultCode
name: CPS SCH350KTL Warn0100
aliases:
- Warn0100
- warn100
- CPS Warn0100
- AC SPD fault
category: Inverters
make: chint
make_name: CPS
model_family: sch-350ktl
family_name: CPS SCH350KTL-DO/US-800
code: Warn0100
code_key: warn100
display_message: AC SPD fault
vendor_severity: Warning
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r8
    h: 358fe21ec377
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r8
    h: 358fe21ec377
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:spd-alarm
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r5
    h: '039191519821'
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r4
    h: aa8bfc6c4d12
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=34.r5
    h: d8695550946c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r5
    h: 19d64f589251
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=25.r5
    h: d8695550946c
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:surge-protection-device
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r4
    h: aa8bfc6c4d12
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  note: Alarm is reserved in these manuals and may be ignored in the field.
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r5
    h: '039191519821'
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=34.r5
    h: d8695550946c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r5
    h: 19d64f589251
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=25.r5
    h: d8695550946c
  review: drafted
  review_note: 'support check: partial - The passages say the alarm is reserved and can be ignored, but
    don''t explicitly state that it has no production effect.'
---
