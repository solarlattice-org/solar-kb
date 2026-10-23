---
id: fc:chint-sch-350ktl-tempover
type: FaultCode
name: CPS SCH350KTL TempOver
aliases:
- TempOver
- tempover
- CPS TempOver
- over temperature protection
category: Inverters
make: chint
make_name: CPS
model_family: sch-350ktl
family_name: CPS SCH350KTL-DO/US-800
code: TempOver
code_key: tempover
display_message: over temperature protection
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r1
    h: ffdec9ffbb70
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r6
    h: 7e8e2a500b96
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r7
    h: 8b87a4997b5b
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r5
    h: cca74c616770
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r7
    h: ad7a81528003
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r3
    h: 9f5e482be93a
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r6
    h: 953304ecee92
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r1
    h: ffdec9ffbb70
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r6
    h: 7e8e2a500b96
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r8
    h: 4f85bff0c978
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r7
    h: ad7a81528003
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r3
    h: 9f5e482be93a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r1
    h: ffdec9ffbb70
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r6
    h: 7e8e2a500b96
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r7
    h: c06a2fc65fc7
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r8
    h: 4f85bff0c978
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r7
    h: ad7a81528003
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r3
    h: 9f5e482be93a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r1
    h: ffdec9ffbb70
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:adequate-cooling
  note: Applies when ambient temperature or installation location is outside the specified environment.
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r6
    h: 7e8e2a500b96
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r9
    h: 0755d1b9c0a5
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r7
    h: ad7a81528003
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r3
    h: 9f5e482be93a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r1
    h: ffdec9ffbb70
  review: drafted
  review_note: 'support check: partial - Passages say to check ambient temperature and installation location
    but don''t frame it as adequate cooling mitigation.'
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r11
    h: f815619675d0
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r5
    h: cca74c616770
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r7
    h: ad7a81528003
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r3
    h: 9f5e482be93a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r1
    h: ffdec9ffbb70
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  note: Protection-class code; inverter stops feeding in while overheated.
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r6
    h: 7e8e2a500b96
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r7
    h: ad7a81528003
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r3
    h: 9f5e482be93a
  review: drafted
  review_note: 'support check: partial - It is a protection code, but passages do not state that production
    stops.'
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Alarm expected to clear by itself within about 30 minutes; otherwise escalate to service.
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r6
    h: 7e8e2a500b96
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r10
    h: 5773f4c744f1
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r7
    h: ad7a81528003
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r3
    h: 9f5e482be93a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r1
    h: ffdec9ffbb70
  review: drafted
---
