---
id: method:grid-voltage-measurement
type: DetectionMethod
name: Grid voltage measurement
claims:
- claim_id: c1
  rel: produces
  target: meas:grid-voltage-reading-out-of-limit
  note: A low reading at the test points confirms an under-voltage alarm. A high reading confirms an over-voltage
    alarm. If the reading is high only at full power, the AC cables to the interconnect may be undersized.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r3
    h: 52c3fd63f040
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r3
    h: 8ede75869601
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:zero-ac-grid-voltage
  note: For a NO-GRID alarm, AC is checked line-to-line and line-to-ground at the inverter test points.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r2
    h: 3fc18463c15a
  review: drafted
  review_note: 'support check: partial - NO-GRID says inverter doesn''t detect grid and to check AC L-L
    and L-GND, but doesn''t explicitly say measurement shows zero voltage.'
- claim_id: c3
  rel: produces
  target: meas:unequal-phase-voltages
  note: Used to confirm a grid voltage unbalance fault. If the spread is within the utility's limits,
    the imbalance parameter can be adjusted instead.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  review: drafted
---
Grid voltage measurement means checking the actual AC voltage at the inverter test points with a meter to confirm a grid voltage alarm. First measure with the DC switch off, line-to-line and line-to-ground, to see whether grid voltage is present and whether it is too high or too low. If the measured voltage really is out of range, contact the utility or power company. Only change the protection limits with the utility's permission. If the AC voltage measures high with the DC switch on and the inverter at full power, the cables between the inverter and the interconnect may be too small. Check the cable size and the voltage drop calculations. Compare the meter reading with the voltage shown on the LCD. If they disagree, the inverter's measurement circuit may be faulty and the inverter may need to be replaced. On three-phase systems, measure each phase. If the phase voltages differ greatly, the cause is grid imbalance and the power company should be contacted. For grid instability alarms, measure the AC voltage and test the AC line for harmonic distortion (THD), both with the DC switch off and with it on.

<!-- review notes
- sentence 3: support check: partial - Adjusting limits with utility permission and contacting the power company when voltage is high are stated, but contacting the utility for under-voltage is not, and 'only' is stronger.
- sentence 5: support check: partial - Passages say compare with LCD and that the measurement circuit may be bad, with replace inverter listed, but don't explicitly tie disagreement to replacement.
- sentence 6: support check: partial - Fault 017 says contact the power company if phase voltages differ greatly, but doesn't state to measure each phase or conclude the cause is grid imbalance definitively.
- sentence 7: support check: partial - AC voltage measurement is only with DC off and THD test is with DC both off and on; the statement says both measurements in both states.
-->
