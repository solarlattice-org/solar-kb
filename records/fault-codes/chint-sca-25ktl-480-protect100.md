---
id: fc:chint-sca-25ktl-480-protect100
type: FaultCode
name: CPS SCA25KTL-480 Protect0100
aliases:
- Protect0100
- protect100
- CPS Protect0100
- The sensor fault of leakage current
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-480
family_name: CPS SCA25KTL-DO-R/US-480
code: Protect0100
code_key: protect100
display_message: The sensor fault of leakage current
vendor_severity: Protection
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-25kw-user-manual-rev-2-1
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r4
    h: 8160d8a2403f
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r4
    h: 8160d8a2403f
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:ground-fault-detector-failure
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r5
    h: fe0ca2913a14
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r4
    h: 8160d8a2403f
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r1
    h: 62a7b29ff982
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r6
    h: a24a0da56dc8
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ground-fault-detector
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r5
    h: fe0ca2913a14
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r1
    h: 62a7b29ff982
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r6
    h: a24a0da56dc8
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:filter-board
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r5
    h: fe0ca2913a14
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r4
    h: 8160d8a2403f
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r1
    h: 62a7b29ff982
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r5
    h: fe0ca2913a14
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r4
    h: 8160d8a2403f
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r1
    h: 62a7b29ff982
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r6
    h: a24a0da56dc8
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Filter board replacement is an alternative in some manuals.
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r5
    h: fe0ca2913a14
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r4
    h: 8160d8a2403f
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r1
    h: 62a7b29ff982
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r6
    h: a24a0da56dc8
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r6
    h: a24a0da56dc8
  review: drafted
  review_note: 'support check: partial - The passages give no explicit stop or trip behaviour for Protect0100.'
- claim_id: c9
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle clears normal case; otherwise service replaces board or inverter.
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r5
    h: fe0ca2913a14
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r4
    h: 8160d8a2403f
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r1
    h: 62a7b29ff982
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r6
    h: a24a0da56dc8
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:chint-sca-25ktl-480
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r4
    h: 8160d8a2403f
  review: drafted
---
