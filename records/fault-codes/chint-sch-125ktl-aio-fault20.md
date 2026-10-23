---
id: fc:chint-sch-125ktl-aio-fault20
type: FaultCode
name: CPS SCH125KTL-AIO Fault0020
aliases:
- Fault0020
- fault20
- CPS Fault0020
- Bus over volt Hardware
category: Inverters
make: chint
make_name: CPS
model_family: sch-125ktl-aio
family_name: CPS SCH125KTL-AIO/US-600
code: Fault0020
code_key: fault20
display_message: Bus over volt Hardware
vendor_severity: Fault
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch125ktl-aio-us-600-sep-2020
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r2
    h: 112fb58796fc
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r2
    h: 112fb58796fc
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34
    h: 9b7f9bd2e50a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r1
    h: 46538e2c878f
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r4
    h: 2325da3dff9a
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r5
    h: 27755f3e72d0
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r2
    h: 112fb58796fc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r4
    h: 27755f3e72d0
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r4
    h: d2bf39f802ad
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r1
    h: 46538e2c878f
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r4
    h: 2325da3dff9a
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r5
    h: 27755f3e72d0
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r2
    h: 112fb58796fc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r4
    h: 27755f3e72d0
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r4
    h: d2bf39f802ad
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r1
    h: 46538e2c878f
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r4
    h: 2325da3dff9a
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r5
    h: 27755f3e72d0
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r2
    h: 112fb58796fc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r4
    h: 27755f3e72d0
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r4
    h: d2bf39f802ad
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if a power cycle does not clear the fault.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r1
    h: 46538e2c878f
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r4
    h: 2325da3dff9a
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r5
    h: 27755f3e72d0
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r2
    h: 112fb58796fc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r4
    h: 27755f3e72d0
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r4
    h: d2bf39f802ad
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; replace inverter if the fault persists.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r1
    h: 46538e2c878f
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r4
    h: 2325da3dff9a
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r5
    h: 27755f3e72d0
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r2
    h: 112fb58796fc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r4
    h: 27755f3e72d0
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r4
    h: d2bf39f802ad
  review: drafted
  review_note: 'support check: partial - Power cycle then replace is stated; manual-reset classification
    only implied.'
---
