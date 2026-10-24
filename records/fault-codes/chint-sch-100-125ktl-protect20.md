---
id: fc:chint-sch-100-125ktl-protect20
type: FaultCode
name: CPS SCH100-125KTL Protect0020
aliases:
- Protect0020
- protect20
- CPS Protect0020
- grid relay error
category: Inverters
make: chint
make_name: CPS
model_family: sch-100-125ktl
family_name: CPS SCH100/125KTL-DO/US-600
code: Protect0020
code_key: protect20
display_message: grid relay error
vendor_severity: Protection
page: 75
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r3
    h: f95108ce31c7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r3
    h: f95108ce31c7
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35
    h: 2441b6237235
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r3
    h: f95108ce31c7
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r6
    h: 68c1dff1947b
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r4
    h: c502d58b28db
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r6
    h: '017498296276'
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r3
    h: f95108ce31c7
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r3
    h: cee358a50948
  review: drafted
  review_note: 'support check: partial - The code is labelled grid relay error, but relay failure as a
    failure mode is only implied by the label.'
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r3
    h: f95108ce31c7
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r6
    h: 68c1dff1947b
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r4
    h: c502d58b28db
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r6
    h: '017498296276'
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r3
    h: f95108ce31c7
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r3
    h: cee358a50948
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Power cycle needed to clear implies inverter stopped
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r3
    h: f95108ce31c7
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r6
    h: 68c1dff1947b
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r4
    h: c502d58b28db
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r6
    h: '017498296276'
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r3
    h: f95108ce31c7
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r3
    h: cee358a50948
  review: drafted
  review_note: 'support check: partial - Power cycle and replacement instructions imply stoppage, but
    a trip is not stated.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: AC and DC power cycle; replace inverter if fault persists
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r3
    h: f95108ce31c7
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r6
    h: 68c1dff1947b
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r4
    h: c502d58b28db
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r6
    h: '017498296276'
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r3
    h: f95108ce31c7
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r3
    h: cee358a50948
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r3
    h: f95108ce31c7
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r6
    h: 68c1dff1947b
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r4
    h: c502d58b28db
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r6
    h: '017498296276'
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r3
    h: f95108ce31c7
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r3
    h: cee358a50948
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if restart does not clear the fault
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r3
    h: f95108ce31c7
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r6
    h: 68c1dff1947b
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r4
    h: c502d58b28db
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r6
    h: '017498296276'
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r3
    h: f95108ce31c7
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r3
    h: cee358a50948
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:chint-sch-100-125ktl
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r3
    h: f95108ce31c7
  review: drafted
---
