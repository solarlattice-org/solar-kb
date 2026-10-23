---
id: fc:chint-sca-50-100k-t-protect30
type: FaultCode
name: CPS SCA50-100K-T Protect0030
aliases:
- Protect0030
- protect30
- CPS Protect0030
- Bus Soft start time out
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0030
code_key: protect30
display_message: Bus Soft start time out
vendor_severity: Protection
page: 130
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48.r4
    h: f8d129f841c8
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48.r4
    h: f8d129f841c8
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:overcurrent
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r2
    h: 695c0ef30443
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r3
    h: 3d6d892ff6c2
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r1
    h: b667b4ff09bf
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r3
    h: 9af8329118ff
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r2
    h: 695c0ef30443
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r2
    h: 695c0ef30443
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r3
    h: 3d6d892ff6c2
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r1
    h: b667b4ff09bf
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r3
    h: 9af8329118ff
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r2
    h: 695c0ef30443
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Power cycle needed to clear implies inverter stopped
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r2
    h: 695c0ef30443
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r3
    h: 3d6d892ff6c2
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r1
    h: b667b4ff09bf
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r3
    h: 9af8329118ff
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r2
    h: 695c0ef30443
  review: drafted
  review_note: 'support check: partial - Power cycle and replacement are recommended, but a stop of production
    is not stated; it is only implied.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: AC and DC power cycle; replace inverter if fault persists
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r2
    h: 695c0ef30443
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r3
    h: 3d6d892ff6c2
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r1
    h: b667b4ff09bf
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r3
    h: 9af8329118ff
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r2
    h: 695c0ef30443
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r2
    h: 695c0ef30443
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r3
    h: 3d6d892ff6c2
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r1
    h: b667b4ff09bf
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r3
    h: 9af8329118ff
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r2
    h: 695c0ef30443
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if restart does not clear the fault
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r2
    h: 695c0ef30443
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r3
    h: 3d6d892ff6c2
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r1
    h: b667b4ff09bf
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r3
    h: 9af8329118ff
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r2
    h: 695c0ef30443
  review: drafted
---
