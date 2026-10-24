---
id: fc:chint-sca-25ktl-480-pvvoltover
type: FaultCode
name: CPS SCA25KTL-480 PVVoltOver
aliases:
- PVVoltOver
- pvvoltover
- CPS PVVoltOver
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-480
family_name: CPS SCA25KTL-DO-R/US-480
code: PVVoltOver
code_key: pvvoltover
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-25kw-user-manual-rev-2-1
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r6
    h: 10cec3ceac86
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r6
    h: 10cec3ceac86
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r3
    h: 2f24040c3ea0
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r4
    h: 0a808d074f25
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=28.r1
    h: 2f24040c3ea0
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r7
    h: 0fccc4e3d5db
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r1
    h: 5476c5da00e0
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r3
    h: 2f24040c3ea0
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=28.r1
    h: 2f24040c3ea0
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r7
    h: 0fccc4e3d5db
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r6
    h: 10cec3ceac86
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r3
    h: 2f24040c3ea0
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r4
    h: 0a808d074f25
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=28.r1
    h: 2f24040c3ea0
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r7
    h: 0fccc4e3d5db
  review: drafted
  review_note: 'support check: partial - The passages say to measure the DC voltage as a diagnostic step,
    but they don''t say the fault is detected…'
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Applies when the display reading agrees with the meter within 2%.
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=60.r1
    h: 5476c5da00e0
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r3
    h: 2f24040c3ea0
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r4
    h: 0a808d074f25
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=28.r1
    h: 2f24040c3ea0
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r7
    h: 0fccc4e3d5db
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Applies when the display reading deviates from the meter by more than 2%.
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r6
    h: 10cec3ceac86
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r3
    h: 2f24040c3ea0
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r4
    h: 0a808d074f25
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=28.r1
    h: 2f24040c3ea0
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r7
    h: 0fccc4e3d5db
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-25ktl-480
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r6
    h: 10cec3ceac86
  review: drafted
---
