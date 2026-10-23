---
id: symptom:overcurrent
type: Symptom
name: Inverter overcurrent
aliases:
- Inverter Hardware Overcurrent
- Inv HW Overcurr
- Inverter HW overcurrent
- Inverter hardware overcurrent fault
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: CPS inverters show this as Protect0030 (inverter over current), Protect0240 or PFault0080 (inverter
    hardware overcurrent).
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=70.r3
    h: a8a1ed50bb62
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r1
    h: 6acb07e190e3
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r3
    h: 3d6d892ff6c2
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r2
    h: 942a5485e959
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r2
    h: 695c0ef30443
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r2
    h: 695c0ef30443
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=59.r3
    h: eb83a32c1f6c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r3
    h: 9af8329118ff
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=35.r3
    h: eb83a32c1f6c
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r3
    h: eb83a32c1f6c
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r2
    h: bc55e42d9b99
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r1
    h: b667b4ff09bf
  - src: src:chint-cps-sca100k-t-sca50k-t-modbus-map-2026-02-05
    loc: tbl=50.r28
    h: 94d55d06242f
  - src: src:chint-cps-sca100k-t-sca50k-t-modbus-map-2026-02-05
    loc: tbl=48.r16
    h: 8e3ac1ab5893
  - src: src:chint-cps-200-250kw-k-t-modbus-map-2026-01-30
    loc: tbl=42.r29
    h: 85ab36f417a8
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:ac-instantaneous-overcurrent-event
  note: The inverter detects an overcurrent on the AC grid side and disconnects from the grid.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h511
    h: c6e376e4d4de
  review: drafted
  review_note: 'support check: partial - The passage supports the AC-side overcurrent disconnect, but
    the specific signal behaviors (current exceeding trip level then zero, power dropping to zero) are
    not stated.'
---
Inverter overcurrent is a protection event: the inverter detects too much current on its output and stops feeding the grid. On CPS inverters it appears as Protect0030 (inverter over current), or as Protect0240 or PFault0080 (inverter hardware overcurrent). Remote monitoring can read the same event over Modbus as a fault bit in the inverter status registers. For Protect0240, the manual says to watch for about five minutes first, because the alarm may clear by itself. If it stays, turn off both the AC and DC switches, wait one minute for stored energy to discharge, then switch both back on. If the fault comes back after the restart, the manuals point to an internal inverter problem: contact after-sales service or replace the inverter. Do not confuse this alarm with boost or PV input overcurrent codes. Those point to the DC side, so check the PV input current for them first.

<!-- review notes
- sentence 3: support check: partial - Register addresses and bit positions for the overcurrent faults are given, but the passages don't say remote monitoring reads them over Modbus, and u15/u34 are the only ones with a fault level.
- sentence 6: support check: partial - Contact after-sales service or replace the inverter if the fault persists is stated, but the passages don't say this indicates an internal inverter problem.
- sentence 7: support check: partial - Passages show boost/PV overcurrent codes relate to the DC input and PV over current says to check PV input current, but nothing states to not confuse them with this alarm, and the check-PV-first advice applies only to the PV over current code, not boost.
-->
