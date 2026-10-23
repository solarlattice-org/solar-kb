---
id: symptom:grid-phase-angle-abnormal
type: Symptom
name: Abnormal grid phase angle
aliases:
- PHASE FAULT
- Abnormal phase of the grid
- Grid phase abnormal
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Solis shows the PHASE FAULT message in its fault message table.
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r8
    h: f73d799fd7e4
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r8
    h: f73d799fd7e4
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16
    h: 4d8c48c35a55
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15
    h: c4c034a83bc3
  review: drafted
---
Some inverters raise an alarm when the phase of the grid at their AC terminals looks abnormal. Solis calls it PHASE FAULT. Check the installation first and confirm the grid wiring to the inverter is connected correctly, because a wiring error can cause this alarm. Then measure the grid to confirm the phases are 120 degrees apart. If the wiring and the grid phase angles are both correct, restart the inverter. If the fault comes back, the inverter itself is the likely cause and should be replaced. On microgrid controllers, a phase difference reading in degrees shows the angle between the grid-side and microgrid-side voltages during reconnection.

<!-- review notes
- sentence 2: support check: partial - The passages say to inspect the installation and check that the grid wiring is connected properly, but they don't say a wiring error causes the alarm, and the cause is only given as 'abnormal phase of the grid'.
- sentence 4: support check: partial - The solution list gives the steps in order (check wiring, check phase angle, restart, replace), but it doesn't say to replace the inverter only if the fault returns after a restart, and it doesn't call the inverter the likely cause.
-->
