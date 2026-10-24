---
id: fc:chint-sch-125ktl-aio-fault100
type: FaultCode
name: CPS SCH125KTL-AIO Fault0100
aliases:
- Fault0100
- fault100
- CPS Fault0100
- Grid relay fault
category: Inverters
make: chint
make_name: CPS
model_family: sch-125ktl-aio
family_name: CPS SCH125KTL-AIO/US-600
code: Fault0100
code_key: fault100
display_message: Grid relay fault
vendor_severity: Fault
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch125ktl-aio-us-600-sep-2020
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r3
    h: 7f2c8c1c7701
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r3
    h: 7f2c8c1c7701
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34
    h: 9b7f9bd2e50a
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r5
    h: 0544aa41dad9
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r1
    h: f8b3d290cd84
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r2
    h: 014367901d03
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r2
    h: 014367901d03
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r2
    h: 89baddd3ba9c
  review: drafted
  review_note: 'support check: partial - The passages only say to restart and replace if not cleared;
    they never name relay failure beyond the ''Grid relay…'
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r5
    h: 0544aa41dad9
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r1
    h: f8b3d290cd84
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r2
    h: 014367901d03
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r2
    h: 014367901d03
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r2
    h: 89baddd3ba9c
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r5
    h: 0544aa41dad9
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r1
    h: f8b3d290cd84
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r2
    h: 014367901d03
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r2
    h: 014367901d03
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r2
    h: 89baddd3ba9c
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if a power cycle does not clear the fault.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r5
    h: 0544aa41dad9
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r1
    h: f8b3d290cd84
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r2
    h: 014367901d03
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r2
    h: 014367901d03
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r2
    h: 89baddd3ba9c
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; replace inverter if the fault persists.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r5
    h: 0544aa41dad9
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r1
    h: f8b3d290cd84
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r2
    h: 014367901d03
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r2
    h: 014367901d03
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r2
    h: 89baddd3ba9c
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:chint-sch-125ktl-aio
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r3
    h: 7f2c8c1c7701
  review: drafted
---
