---
id: symptom:neutral-point-voltage-imbalance
type: Symptom
name: Neutral point voltage imbalance
aliases:
- Bus imbalance
- Voltage imbalance at neutral point
- Neutral point shift
- Bus high voltage differential fault
- BUS voltage difference fault
- Bus different high fault
- symptom:dc-bus-imbalance
- DC bus voltage imbalance
claims:
- claim_id: c1
  rel: observed_as
  target: meas:dc-bus-voltage-differential
  note: 'Fault bits for a difference between the two DC bus halves: Fault4010 and PFault0020 in CPS Modbus
    maps.'
  cite:
  - src: src:chint-cps-sca100k-t-sca50k-t-modbus-map-2026-02-05
    loc: tbl=56.r19
    h: 6646bca4fe2f
  - src: src:chint-cps-200-250kw-k-t-modbus-map-2026-01-30
    loc: tbl=44.r17
    h: 001b939f84a4
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r2
    h: a03501754bb9
  - src: src:chint-cps-sca100k-t-sca50k-t-modbus-map-2026-02-05
    loc: tbl=51.r6
    h: 4c895cc64663
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c2
  rel: observed_as
  target: meas:unequal-phase-voltages
  note: CPS manuals tie bus imbalance to impedance and voltage imbalance between grid phases. Sungrow
    tells the technician to measure grid voltage for imbalance.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r2
    h: 14073738a6a6
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r1
    h: 4a6b01017499
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r6
    h: df66a452b082
  - src: src:sungrow-sungrow-sg3150ud-mv-us-sg4400ud-mv-us-user-manual-ver23
    loc: tbl=45.r6
    h: a2a9e1a666ea
  review: drafted
  review_note: 'support check: partial - Passages tie bus imbalance to impedance/voltage imbalance between
    grid phases and Sungrow says measure grid voltage, but nothing says phase voltages differ while the
    alarm is active as an observation.; review: partial - The note''s wording is supported: CPS ties bus
    imbalance to impedance and voltage imbalance between grid phases, and Sungrow says to measure grid
    voltage. No passage says unequal phase voltages are actually seen as the sign of neutral point imbalance,…'
---
The inverter reports that the voltage on the two halves of its DC bus, measured around the neutral point, has drifted apart. CPS and Yaskawa string inverters show this as Fault0110 or Protect0070 bus imbalance. CPS manuals link it to unequal impedance and voltage between the grid phases during transients. Measure the phase voltages first and check for grid imbalance. Sungrow also says to check whether the DC side is short-circuited, whether the DC input voltage is outside its allowed range, and whether the grid voltage is abnormal. Look in the fault history for DC overvoltage, DC undervoltage, module faults or AC overcurrent at the same time, and troubleshoot those first. On CPS units, raise the IDCmax or DCI limit as the manual describes. If the alarm keeps coming back after that, the inverter itself is likely faulty and should be replaced or sent to service.

<!-- review notes
- sentence 1: support check: partial - Fault0110/Protect0070 bus imbalance and 'voltage imbalance at neutral point' appear, but nothing attributes it to Yaskawa or states the DC bus halves drifting apart explicitly.
- sentence 4: support check: partial - Passage says check history for those concurrent faults and refer to their troubleshooting, but 'troubleshoot those first' ordering is only implied.
- sentence 5: support check: partial - Raising IDCmax/DCI limit and replacing the inverter if alarm persists are stated, but 'sent to service' and 'likely faulty' are not stated for this fault (service contact is for Fault4010 only).
- sentence 1: review: partial - The CPS and Yaskawa sources do show Fault0110/Protect0070 bus imbalance, but none of the passages describes the two DC bus halves drifting apart around the neutral point.
-->
