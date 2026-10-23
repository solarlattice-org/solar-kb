---
id: fc:chint-sca-25ktl-208-arcboarderr
type: FaultCode
name: CPS SCA25KTL-208 Arcboard Err
aliases:
- Arcboard Err
- arcboarderr
- CPS Arcboard Err
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: Arcboard Err
code_key: arcboarderr
vendor_severity: Protection
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r3
    h: 99d70367a788
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r3
    h: 99d70367a788
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-detector-failure
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r3
    h: 99d70367a788
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r4
    h: 38c2919b6b74
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r7
    h: 29641da34bb0
  review: drafted
  review_note: 'support check: partial - Arc board error with board checks/replacement implies arc board
    failure, but not explicitly stated as indicating failure.'
- claim_id: c4
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r3
    h: 99d70367a788
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r4
    h: 38c2919b6b74
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r7
    h: 29641da34bb0
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:arc-fault-self-test
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r3
    h: 99d70367a788
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r4
    h: 38c2919b6b74
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r7
    h: 29641da34bb0
  review: drafted
  review_note: 'support check: partial - Arc fault test is a remedy step, not stated as the detection
    method.'
- claim_id: c6
  rel: mitigated_by
  target: mit:arc-board-connector-check
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r3
    h: 99d70367a788
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r4
    h: 38c2919b6b74
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r7
    h: 29641da34bb0
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:arc-board-replacement
  note: Only if the alarm recurs after the connector check and self-test.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r3
    h: 99d70367a788
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r4
    h: 38c2919b6b74
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r7
    h: 29641da34bb0
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Operator checks connector and runs the test first; replacement only if the alarm recurs.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r3
    h: 99d70367a788
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r4
    h: 38c2919b6b74
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r7
    h: 29641da34bb0
  review: drafted
  review_note: 'support check: partial - Steps stated but manual reset classification not explicit.'
---
