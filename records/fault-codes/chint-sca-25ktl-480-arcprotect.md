---
id: fc:chint-sca-25ktl-480-arcprotect
type: FaultCode
name: CPS SCA25KTL-480 ARC Protect
aliases:
- ARC Protect
- arcprotect
- CPS ARC Protect
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-480
family_name: CPS SCA25KTL-DO-R/US-480
code: ARC Protect
code_key: arcprotect
page: 110
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-25kw-user-manual-rev-2-1
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r3
    h: 70adb9ea2a38
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r2
    h: bdd8e4eb27f4
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r3
    h: 70adb9ea2a38
  review: drafted
  review_note: 'support check: partial - ARC Protect with arc board checks suggests arc fault, but the
    passages do not explicitly say it indicates an arc fault.'
- claim_id: c3
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r2
    h: bdd8e4eb27f4
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r3
    h: 70adb9ea2a38
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:arc-fault-self-test
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r2
    h: bdd8e4eb27f4
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r3
    h: 70adb9ea2a38
  review: drafted
  review_note: 'support check: partial - Arc Fault Test is a diagnostic step, but the passages don''t
    say the alarm is detected by it.'
- claim_id: c5
  rel: mitigated_by
  target: mit:arc-board-connector-check
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r2
    h: bdd8e4eb27f4
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r3
    h: 70adb9ea2a38
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:arc-board-replacement
  note: Only if the alarm recurs after the connector check and self-test.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r2
    h: bdd8e4eb27f4
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r3
    h: 70adb9ea2a38
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Operator checks connector and runs the test first; service replacement only if the alarm recurs.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r2
    h: bdd8e4eb27f4
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r3
    h: 70adb9ea2a38
  review: drafted
  review_note: 'support check: partial - Operator steps and conditional replacement stated, but no explicit
    manual reset clearing mechanism.'
- claim_id: c8
  rel: applies_to
  target: prod:chint-sca-25ktl-480
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r3
    h: 70adb9ea2a38
  review: drafted
---
