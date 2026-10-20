---
id: symptom:grid-undervoltage
type: Symptom
name: Grid undervoltage
aliases:
- Undervoltage
- grid under-voltage
claims:
- claim_id: c1
  rel: observed_as
  target: meas:grid-voltage-reading-out-of-limit
  note: Inverter fault codes report that the measured grid voltage is below the set protection value.
    Battery-system status points flag undervoltage that falls outside the hardware trip thresholds.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r2
    h: 74f93b8997f3
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=95.r13
    h: 559b8ecfd60c
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=88.r13
    h: 559b8ecfd60c
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=79.r6
    h: 559b8ecfd60c
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=176.r1
    h: 14b129a5c9bc
  review: drafted
  review_note: 'support check: partial - Passages say undervoltage means grid voltage below the set protection
    value and Megapack flags voltage outside trip thresholds, but nothing mentions AC power dropping to
    zero during the trip.'
---
A grid undervoltage fault means the inverter measured an AC grid voltage below its set protection value and disconnected from the grid. Inverters and storage systems report it as a fault code or a status flag when the measured voltage falls outside the protection trip thresholds. Usually the inverter reconnects by itself once the grid voltage is normal again, so a single event needs no action. If the fault keeps coming back, first measure the actual grid voltage. If it really is below the setpoint, the cause is on the utility side and the local power company should be contacted. If the grid voltage is normal, check in the app or on the LCD that the undervoltage protection parameters are set correctly for the local grid code. Next, check that the AC cable is firmly seated in its terminals. If none of these checks finds the cause, contact the inverter manufacturer's service.

<!-- review notes
- sentence 1: support check: partial - Voltage below the set protection value is stated and reconnection after recovery implies disconnection, but disconnection is not explicitly stated.
- sentence 4: support check: partial - Measuring grid voltage and contacting the utility if it is below the set value is stated, but the 'cause is on the utility side' conclusion is not explicit.
- sentence 5: support check: partial - Checking protection parameters via app or LCD is stated, but the 'for the local grid code' qualifier is only loosely implied by the parameter ranges.
-->
