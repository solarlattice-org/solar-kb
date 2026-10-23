---
id: fc:chint-sch-350ktl-extfanerr
type: FaultCode
name: CPS SCH350KTL ExtFanErr
aliases:
- ExtFanErr
- extfanerr
- CPS ExtFanErr
- cooling fan failure
category: Inverters
make: chint
make_name: CPS
model_family: sch-350ktl
family_name: CPS SCH350KTL-DO/US-800
code: ExtFanErr
code_key: extfanerr
display_message: cooling fan failure
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r3
    h: 36fdb08d72c6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r4
    h: 8c0f6b926ff4
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r5
    h: ae858ba47931
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r2
    h: 584b5f831617
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=29.r4
    h: 4cd041ad8268
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r4
    h: 8c0f6b926ff4
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r3
    h: 36fdb08d72c6
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r4
    h: 8c0f6b926ff4
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r5
    h: ae858ba47931
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r2
    h: 584b5f831617
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=29.r4
    h: 4cd041ad8268
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r4
    h: 8c0f6b926ff4
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r3
    h: b6a4aedbecdc
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r3
    h: 36fdb08d72c6
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  note: Blocked fan, expired fan life or poor fan connector contact
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r4
    h: 8c0f6b926ff4
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r5
    h: a6f5a7f3b418
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r5
    h: ae858ba47931
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r5
    h: de5bc765d628
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  note: Inspect fan blades for foreign objects
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r4
    h: 8c0f6b926ff4
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=33.r1
    h: 88a6b2c8e9ab
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r6
    h: d7a7d9244d6b
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r6
    h: 3c31a0a6c5b8
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r3
    h: 36fdb08d72c6
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  note: Remove foreign objects from fan blades
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=33.r1
    h: 88a6b2c8e9ab
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r6
    h: d7a7d9244d6b
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r3
    h: 1891a9940aaf
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r6
    h: 3c31a0a6c5b8
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r3
    h: b6a4aedbecdc
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r3
    h: 36fdb08d72c6
  review: drafted
  review_note: 'support check: partial - Checking for foreign objects on fan blades is recommended, but
    removal and clearing the blockage are only implied.'
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: First observe for self-clearing; then blade check, reboot, then service
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=33.r1
    h: 88a6b2c8e9ab
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r5
    h: ae858ba47931
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r3
    h: 1891a9940aaf
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r6
    h: 3c31a0a6c5b8
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r3
    h: b6a4aedbecdc
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r3
    h: 36fdb08d72c6
  review: drafted
---
