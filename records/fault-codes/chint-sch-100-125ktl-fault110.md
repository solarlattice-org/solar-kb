---
id: fc:chint-sch-100-125ktl-fault110
type: FaultCode
name: CPS SCH100-125KTL Fault0110
aliases:
- Fault0110
- fault110
- CPS Fault0110
- bus imbalance
category: Inverters
make: chint
make_name: CPS
model_family: sch-100-125ktl
family_name: CPS SCH100/125KTL-DO/US-600
code: Fault0110
code_key: fault110
display_message: bus imbalance
vendor_severity: Fault
page: 78
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=39.r1
    h: df66a452b082
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=39.r1
    h: df66a452b082
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38
    h: 1bcb7a5b5e5d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:neutral-point-voltage-imbalance
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r1
    h: 4a6b01017499
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=61.r2
    h: 5b3c27fda620
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=39.r1
    h: df66a452b082
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r2
    h: 9f90ca4fa5ea
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r6
    h: df66a452b082
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r6
    h: 57ffb0fe11e4
  review: drafted
  review_note: 'support check: partial - Fault0110 is ''Bus imbalance'' with grid phase imbalance mentioned,
    but neutral point voltage imbalance isn''t explicitly stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Raise the DC injection limit to tolerate grid phase imbalance.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r1
    h: 4a6b01017499
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=61.r2
    h: 5b3c27fda620
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=39.r1
    h: df66a452b082
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r2
    h: 9f90ca4fa5ea
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r6
    h: df66a452b082
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r6
    h: 57ffb0fe11e4
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if the fault persists after the parameter adjustment.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r1
    h: 4a6b01017499
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=61.r2
    h: 5b3c27fda620
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=39.r1
    h: df66a452b082
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r2
    h: 9f90ca4fa5ea
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r6
    h: df66a452b082
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r6
    h: 57ffb0fe11e4
  review: drafted
---
