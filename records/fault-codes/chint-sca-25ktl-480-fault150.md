---
id: fc:chint-sca-25ktl-480-fault150
type: FaultCode
name: CPS SCA25KTL-480 Fault0150
aliases:
- Fault0150
- fault150
- CPS Fault0150
- Open-loop self-check failure
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-480
family_name: CPS SCA25KTL-DO-R/US-480
code: Fault0150
code_key: fault150
display_message: Open-loop self-check failure
vendor_severity: Fault
page: 112
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-25kw-user-manual-rev-2-1
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=63.r1
    h: 13ce51ed0442
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=63.r1
    h: 13ce51ed0442
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r3
    h: 68e9a06d8e3c
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=63.r1
    h: 13ce51ed0442
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r6
    h: 4814f3e0bbc1
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r3
    h: 69a4a4901678
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r5
    h: 4814f3e0bbc1
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r5
    h: 9d6ef2316c23
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r3
    h: 68e9a06d8e3c
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=63.r1
    h: 13ce51ed0442
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r6
    h: 4814f3e0bbc1
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r3
    h: 69a4a4901678
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r5
    h: 4814f3e0bbc1
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r5
    h: 9d6ef2316c23
  review: drafted
  review_note: 'support check: partial - The remedies restart or replace the inverter, but no passage
    names the inverter as the affected component beyond that.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r3
    h: 68e9a06d8e3c
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=63.r1
    h: 13ce51ed0442
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r6
    h: 4814f3e0bbc1
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r3
    h: 69a4a4901678
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r5
    h: 4814f3e0bbc1
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r5
    h: 9d6ef2316c23
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if a power cycle does not clear the fault.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r3
    h: 68e9a06d8e3c
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=63.r1
    h: 13ce51ed0442
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r6
    h: 4814f3e0bbc1
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r3
    h: 69a4a4901678
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r5
    h: 4814f3e0bbc1
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r5
    h: 9d6ef2316c23
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; replace inverter if the fault persists.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r3
    h: 68e9a06d8e3c
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=63.r1
    h: 13ce51ed0442
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r6
    h: 4814f3e0bbc1
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r3
    h: 69a4a4901678
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r5
    h: 4814f3e0bbc1
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r5
    h: 9d6ef2316c23
  review: drafted
---
