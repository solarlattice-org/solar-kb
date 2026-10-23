---
id: symptom:pv-input-overload
type: Symptom
name: PV input overload
aliases:
- PV overload condition
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On the Conext CL125 this condition is reported as event/alarm code 076 (hex 0x004C), described
    as a PV overload condition.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r3
    h: 44cf211d1a75
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=34.r1
    h: 5f40bd979e1d
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=34
    h: dd5787f9b578
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
PV input overload is an inverter alarm. It means the PV array connected to the inverter inputs is delivering more than the inverter is designed to accept. On the Schneider Conext CL125 it shows up as event or alarm code 076, also read over Modbus as hex 0x004C, with the description PV overload condition. The manufacturer's fix is to review the PV system design and change how the PV strings are connected to the inverter inputs. Check the array sizing and how strings are spread across the PV inputs first, because the alarm points to a design or connection issue rather than a failed part. Do not confuse this alarm with the CL125 PV power event warning, code 078. That one points to loose PV input terminals that need re-torquing.

<!-- review notes
- sentence 1: support check: partial - The alarm and PV overload description are stated, but the definition that the array delivers more than the inverter accepts comes only from a different (MV grid-connected) inverter's overload text, not the CL125 alarm.
- sentence 2: support check: partial - Code 076, hex 0x004C and description are stated, but the passages do not mention Modbus reading of the hex value.
- sentence 4: support check: partial - The solution supports checking design and input connections, but the claim that it is not a failed part, and the 'array sizing/string spread' priority, are inferred, not stated.
- sentence 4: review: partial - The passages say to check the PV system design and adjust the PV input connections, but the focus on array sizing and string spread, the 'first' ordering, and the 'rather than a failed part' reasoning are inferred, not stated.
-->
