---
id: fc:chint-sch-350ktl-commerr
type: FaultCode
name: CPS SCH350KTL CommErr
aliases:
- CommErr
- commerr
- CPS CommErr
- communication error
category: Inverters
make: chint
make_name: CPS
model_family: sch-350ktl
family_name: CPS SCH350KTL-DO/US-800
code: CommErr
code_key: commerr
display_message: communication error
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r2
    h: cf577b21cc53
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r1
    h: 1d25ec1c879a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=29.r1
    h: cdea98d0f253
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r1
    h: 1d25ec1c879a
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r3
    h: a402e3a3a132
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=54.r1
    h: 58820161a345
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r1
    h: 77985fbffbd6
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:auto-reset
  note: Usually clears by itself; then reboot, then service if persisting
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r3
    h: ff2cdce4cb07
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r4
    h: 89e8a85f2e95
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r1
    h: a37a7c047fe8
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=29.r3
    h: 8ba6a7859a01
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r1
    h: 77985fbffbd6
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r3
    h: ff2cdce4cb07
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r2
    h: cf577b21cc53
  review: drafted
  review_note: 'support check: partial - Observing for automatic elimination is the first step, but ''usually
    clears by itself'' is not stated; reboot and service steps…'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  note: Second step if the alarm does not clear automatically
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r3
    h: ff2cdce4cb07
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r4
    h: 89e8a85f2e95
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r1
    h: a37a7c047fe8
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=29.r3
    h: 8ba6a7859a01
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r1
    h: 77985fbffbd6
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r3
    h: ff2cdce4cb07
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r2
    h: cf577b21cc53
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Final escalation after reboot fails
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r3
    h: ff2cdce4cb07
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r4
    h: 89e8a85f2e95
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r1
    h: a37a7c047fe8
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r1
    h: 77985fbffbd6
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r3
    h: ff2cdce4cb07
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r2
    h: cf577b21cc53
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:chint-sch-350ktl
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r2
    h: cf577b21cc53
  review: drafted
---
