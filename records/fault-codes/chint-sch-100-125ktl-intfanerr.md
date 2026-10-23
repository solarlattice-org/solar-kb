---
id: fc:chint-sch-100-125ktl-intfanerr
type: FaultCode
name: CPS SCH100-125KTL IntFanErr
aliases:
- IntFanErr
- intfanerr
- CPS IntFanErr
category: Inverters
make: chint
make_name: CPS
model_family: sch-100-125ktl
family_name: CPS SCH100/125KTL-DO/US-600
code: IntFanErr
code_key: intfanerr
vendor_severity: Alarm
page: 75
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=33.r2
    h: bd2ced4d1215
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=33.r2
    h: bd2ced4d1215
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32
    h: c7489de96c62
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r4
    h: 6c80e7b1e31d
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=33.r2
    h: bd2ced4d1215
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r3
    h: b6a4aedbecdc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r7
    h: 49943c6ea785
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r4
    h: c9dab768e540
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r3
    h: b6a4aedbecdc
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r4
    h: c9dab768e540
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r4
    h: 6c80e7b1e31d
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=33.r2
    h: bd2ced4d1215
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r3
    h: b6a4aedbecdc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r7
    h: 49943c6ea785
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r4
    h: c9dab768e540
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r4
    h: 6c80e7b1e31d
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=33.r2
    h: bd2ced4d1215
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r3
    h: b6a4aedbecdc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r7
    h: 49943c6ea785
  review: drafted
  review_note: 'support check: partial - Checking for foreign objects on the fan blades is stated, but
    ''ventilation blockage'' is a looser concept than the fan-blade check.'
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r4
    h: 6c80e7b1e31d
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=33.r2
    h: bd2ced4d1215
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r3
    h: b6a4aedbecdc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r7
    h: 49943c6ea785
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r4
    h: 6c80e7b1e31d
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=33.r2
    h: bd2ced4d1215
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r3
    h: b6a4aedbecdc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r7
    h: 49943c6ea785
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:auto-reset
  note: May clear within five minutes; otherwise clear fan debris, reboot, then contact service.
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r4
    h: 6c80e7b1e31d
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=33.r2
    h: bd2ced4d1215
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r3
    h: b6a4aedbecdc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r7
    h: 49943c6ea785
  review: drafted
---
