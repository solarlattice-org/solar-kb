---
id: fc:chint-sca-50-100k-t-protect100
type: FaultCode
name: CPS SCA50-100K-T Protect0100
aliases:
- Protect0100
- protect100
- CPS Protect0100
- Grid Freq High
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0100
code_key: protect100
display_message: Grid Freq High
vendor_severity: Protection
page: 132
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=50.r1
    h: c4b0511bb5e7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=50.r1
    h: c4b0511bb5e7
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
---
