---
id: fc:chint-sch-100-125ktl-protect90
type: FaultCode
name: CPS SCH100-125KTL Protect0090
aliases:
- Protect0090
- protect90
- CPS Protect0090
- bus over voltage
category: Inverters
make: chint
make_name: CPS
model_family: sch-100-125ktl
family_name: CPS SCH100/125KTL-DO/US-600
code: Protect0090
code_key: protect90
display_message: bus over voltage
vendor_severity: Protection
page: 75
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r1
    h: 2dc0825dfb68
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r1
    h: 2dc0825dfb68
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35
    h: 2441b6237235
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r1
    h: 2dc0825dfb68
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r1
    h: 00dd96fd4be8
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r6
    h: 8c706f517d8a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r1
    h: f8db38612c36
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r1
    h: 2dc0825dfb68
  review: drafted
  review_note: 'support check: partial - Protect0090 is labelled bus over voltage, but whether it is DC
    bus is not stated.'
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r1
    h: 2dc0825dfb68
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r1
    h: 00dd96fd4be8
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r6
    h: 8c706f517d8a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r1
    h: f8db38612c36
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r1
    h: 2dc0825dfb68
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Power cycle needed to clear implies inverter stopped
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r1
    h: 2dc0825dfb68
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r1
    h: 00dd96fd4be8
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r6
    h: 8c706f517d8a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r1
    h: f8db38612c36
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r1
    h: 2dc0825dfb68
  review: drafted
  review_note: 'support check: partial - Power cycle and replacement are recommended, but a stop of production
    is not stated; it is only implied.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: AC and DC power cycle; replace inverter if fault persists
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r1
    h: 2dc0825dfb68
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r1
    h: 00dd96fd4be8
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r6
    h: 8c706f517d8a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r1
    h: f8db38612c36
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r1
    h: 2dc0825dfb68
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r1
    h: 2dc0825dfb68
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r1
    h: 00dd96fd4be8
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r6
    h: 8c706f517d8a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r1
    h: f8db38612c36
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r1
    h: 2dc0825dfb68
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if restart does not clear the fault
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r1
    h: 2dc0825dfb68
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r1
    h: 00dd96fd4be8
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r6
    h: 8c706f517d8a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r1
    h: f8db38612c36
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r1
    h: 2dc0825dfb68
  review: drafted
---
