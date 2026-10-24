---
id: fc:chint-sch-100-125ktl-fault80
type: FaultCode
name: CPS SCH100-125KTL Fault0080
aliases:
- Fault0080
- fault80
- CPS Fault0080
- bus hardware over current fault
category: Inverters
make: chint
make_name: CPS
model_family: sch-100-125ktl
family_name: CPS SCH100/125KTL-DO/US-600
code: Fault0080
code_key: fault80
display_message: bus hardware over current fault
vendor_severity: Fault
page: 77
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r3
    h: 67b952fa596d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r3
    h: 67b952fa596d
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38
    h: 1bcb7a5b5e5d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-overcurrent-overvoltage
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r3
    h: 7cbaae6497da
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r3
    h: 67b952fa596d
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r5
    h: b655afdf273b
  review: drafted
  review_note: 'support check: partial - Fault0080 is a bus hardware over current fault; overvoltage isn''t
    mentioned, though the label covers overcurrent.'
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r3
    h: 7cbaae6497da
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r3
    h: 67b952fa596d
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r5
    h: b655afdf273b
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r3
    h: 7cbaae6497da
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r3
    h: 67b952fa596d
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r5
    h: b655afdf273b
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if a power cycle does not clear the fault.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r3
    h: 7cbaae6497da
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r3
    h: 67b952fa596d
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r5
    h: b655afdf273b
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; replace inverter if the fault persists.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r3
    h: 7cbaae6497da
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r3
    h: 67b952fa596d
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r5
    h: b655afdf273b
  review: drafted
  review_note: 'support check: partial - Power cycle then replace is stated; manual-reset classification
    only implied.'
- claim_id: c8
  rel: applies_to
  target: prod:chint-sch-100-125ktl
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r3
    h: 67b952fa596d
  review: drafted
---
