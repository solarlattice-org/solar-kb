---
id: fc:chint-sca-25ktl-208-fault80
type: FaultCode
name: CPS SCA25KTL-208 Fault0080
aliases:
- Fault0080
- fault80
- CPS Fault0080
- Bus Hardware over current fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: Fault0080
code_key: fault80
display_message: Bus Hardware over current fault
vendor_severity: Fault
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r3
    h: 7cbaae6497da
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r3
    h: 7cbaae6497da
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
---
