---
id: symptom:grid-overvoltage
type: Symptom
name: Grid overvoltage
aliases:
- AC overvoltage
- Over Grid Voltage
- OV-G-V
- 10-minute grid overvoltage
- Grid transient overvoltage
- Grid Uncompliant
claims:
- claim_id: c1
  rel: observed_as
  target: meas:grid-voltage-reading-out-of-limit
  note: The inverter or storage unit sees AC grid voltage above its protection setpoint and disconnects.
    It usually reconnects once the grid returns to normal.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38
    h: f6a2dafbc999
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46
    h: be632716260f
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49
    h: e99876b86296
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r3
    h: 52c3fd63f040
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=88.r13
    h: 559b8ecfd60c
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=95.r13
    h: 559b8ecfd60c
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=79.r6
    h: 559b8ecfd60c
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=262.r3
    h: 0dc455d95f7f
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=176.r1
    h: 14b129a5c9bc
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
  review_note: 'support check: partial - Passages show grid overvoltage faults where voltage exceeds the
    set protection value and the inverter reconnects after normalization, but the specific signal behaviors
    (power falling to zero while disconnected, voltage rising before the trip) are not stated.'
- claim_id: c2
  rel: observed_as
  target: meas:ten-minute-average-overvoltage
  note: The ten-minute average of grid voltage stays above the permitted range, which points to grid voltage
    or grid impedance at the connection point being too high.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49
    h: e99876b86296
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r2
    h: b3913e1065ce
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h156
    h: 8aae27dfe35e
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:overvoltage-trip-reconnect-cycle
  note: The inverter disconnects, voltage falls, it reconnects after the reconnection delay, and voltage
    climbs again. The next trip can follow after seconds, minutes or longer as the wires heat up again.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.10
    h: 2d30f5e4ccd0
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:transient-grid-overvoltage
  note: A short voltage spike above the standard value, reported under a separate fault code from sustained
    overvoltage.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r2
    h: 8a8b6ec00b3f
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46
    h: be632716260f
  review: drafted
- claim_id: c5
  rel: observed_as
  target: meas:overvoltage-power-derating
  note: With volt-watt derating set up, active power is reduced as grid voltage rises between a start
    voltage and an end voltage. These voltages are configurable settings.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=17
    h: 187f43ed0b7e
  review: drafted
  review_note: 'support check: partial - The derating table gives the V1 start and V2 end voltage settings,
    which are configurable, but it does not explicitly state that power is reduced between them (only
    start/end power points) or describe the monitoring signals.'
---
Grid overvoltage means the inverter measures AC voltage above its protection setpoint and disconnects from the grid. It normally reconnects once the grid is back to normal. In monitoring data it often repeats as a cycle: the inverter trips, voltage drops, the inverter reconnects after the set delay, and voltage climbs until the next trip, which may come seconds or minutes later. Some inverters report a separate fault when the ten-minute average voltage stays too high, and another for short transient overvoltage spikes. The cause can be a weak grid, where high distribution-grid resistance meets a lot of local PV capacity. It can also be local, from AC cables between the inverter and the grid connection that are too small or too resistive. Check first: with the DC switch off, measure AC voltage at the inverter. If it is already high, the grid is the cause and the utility should be contacted. If voltage is only high at full power, compare the inverter display with your test-point readings and review the cable ampacity, voltage-drop calculation and cable cross-section. Also confirm that the overvoltage protection parameters are set correctly. Change them only with the utility operator's consent.

<!-- review notes
- sentence 1: support check: partial - Passages say the inverter reconnects after the grid returns to normal and the voltage exceeds the set protection value, but disconnection is only implied by reconnection and the 10-minute fault says to wait for normal.
- sentence 2: support check: partial - The cycle is described, but the passage doesn't say it appears in monitoring data or that it often repeats, and it states the cycle only as a possibility.
- sentence 5: support check: partial - Passage says to switch DC off, check AC at the inverter, and adjust the upper limit with utility permission if it is high; it doesn't state that the grid is the cause, though it says to contact the utility.
-->
