---
id: fc:chint-sch-100-125ktl-pvovercurrent
type: FaultCode
name: CPS SCH100-125KTL PV Over current
aliases:
- PV Over current
- pvovercurrent
- CPS PV Over current
- PV over current
category: Inverters
make: chint
make_name: CPS
model_family: sch-100-125ktl
family_name: CPS SCH100/125KTL-DO/US-600
code: PV Over current
code_key: pvovercurrent
display_message: PV over current
vendor_severity: Protection
page: 77
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r2
    h: c41641d3f34c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r2
    h: c41641d3f34c
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37
    h: b3d48b50b5c7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r2
    h: c41641d3f34c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r3
    h: 1661d3fd4a84
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:pv-current-measurement
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r2
    h: c41641d3f34c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r3
    h: 1661d3fd4a84
  review: drafted
  review_note: 'support check: partial - Passages say to check PV input current but do not state it is
    detected by PV current measurement.'
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Check PV current and power cycle; replace the inverter if the fault cannot be cleared
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r2
    h: c41641d3f34c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r3
    h: 1661d3fd4a84
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r2
    h: c41641d3f34c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r3
    h: 1661d3fd4a84
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r2
    h: c41641d3f34c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r3
    h: 1661d3fd4a84
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:chint-sch-100-125ktl
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r2
    h: c41641d3f34c
  review: drafted
---
