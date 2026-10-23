---
id: fc:chint-sch-275ktl-fault100
type: FaultCode
name: CPS SCH275KTL Fault0100
aliases:
- Fault0100
- fault100
- CPS Fault0100
- grid relay fault
category: Inverters
make: chint
make_name: CPS
model_family: sch-275ktl
family_name: CPS SCH275KTL-DO/US-800
code: Fault0100
code_key: fault100
display_message: grid relay fault
vendor_severity: Fault
page: 73
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r2
    h: 014367901d03
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r2
    h: 014367901d03
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29
    h: 759e8a49f299
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
---
