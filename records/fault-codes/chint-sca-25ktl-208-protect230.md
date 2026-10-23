---
id: fc:chint-sca-25ktl-208-protect230
type: FaultCode
name: CPS SCA25KTL-208 Protect0230
aliases:
- Protect0230
- protect230
- CPS Protect0230
- Inverter open-loop self-test fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: Protect0230
code_key: protect230
display_message: Inverter open-loop self-test fault
vendor_severity: Protection
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r1
    h: 5cddbc08f1cb
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r1
    h: 5cddbc08f1cb
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r1
    h: a985333dbde9
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r2
    h: 8adbbd6a5fea
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r5
    h: 30dd11eda55c
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r7
    h: '535012272447'
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r9
    h: a080e286e0b7
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52
    h: a81a2643c1b9
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r2
    h: 8adbbd6a5fea
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r5
    h: 30dd11eda55c
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r7
    h: '535012272447'
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r9
    h: a080e286e0b7
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r2
    h: 8adbbd6a5fea
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r5
    h: 30dd11eda55c
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r7
    h: '535012272447'
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r9
    h: a080e286e0b7
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52
    h: a81a2643c1b9
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r2
    h: 8adbbd6a5fea
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r5
    h: 30dd11eda55c
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r7
    h: '535012272447'
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r9
    h: a080e286e0b7
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52
    h: a81a2643c1b9
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle clears normal case; replace inverter if fault persists.
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r2
    h: 8adbbd6a5fea
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r5
    h: 30dd11eda55c
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r7
    h: '535012272447'
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r9
    h: a080e286e0b7
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52
    h: a81a2643c1b9
  review: drafted
  review_note: 'support check: partial - Operator power cycle and replacement if persisting are stated,
    but nothing says it clears only by manual reset; plausibly implied…'
---
