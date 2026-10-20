---
id: symptom:grid-voltage-out-of-range
type: Symptom
name: Grid voltage out of range
aliases:
- GridV.OutLim
- Grid incident
- Grid abnormal
- Grid Uncompliant
claims:
- claim_id: c1
  rel: observed_as
  target: meas:grid-voltage-reading-out-of-limit
  note: The measured grid voltage at the inverter is above or below the configured protection thresholds.
    On CPS units the thresholds are set as a percentage of rated voltage, at several levels, for each
    grid standard.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=35.r4
    h: ae10c12f715d
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=39.r4
    h: 18041faed7c2
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r1
    h: c4550b8a0ebe
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=38.r2
    h: 74f93b8997f3
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49
    h: e99876b86296
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h156
    h: 8aae27dfe35e
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=15.r7
    h: 7a21d1bf773a
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=88.r13
    h: 559b8ecfd60c
  review: drafted
  review_note: 'support check: partial - Passages state grid voltage out of range/limits for protection,
    but the specific signal patterns (phase voltage vs. settings, power drop to zero then return) and
    CPS percentage thresholds at several levels are only partly stated.'
- claim_id: c2
  rel: observed_as
  target: meas:ac-power-step-drop
  note: The inverter disconnects from the grid when voltage is out of range. It usually reconnects after
    the grid returns to normal.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h156
    h: 8aae27dfe35e
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h239
    h: 8aae27dfe35e
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h235
    h: 797da27ddf22
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49
    h: e99876b86296
  review: drafted
  review_note: 'support check: partial - Passages say the inverter disconnects from the grid and usually
    reconnects when the grid is normal, but do not state power falls abruptly to zero at the moment of
    the excursion.'
- claim_id: c3
  rel: observed_as
  target: meas:ten-minute-average-overvoltage
  note: The ten-minute average of the grid voltage goes above the permitted range. This can be caused
    by high grid impedance at the connection point.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h156
    h: 8aae27dfe35e
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h239
    h: 8aae27dfe35e
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49
    h: e99876b86296
  review: drafted
---
The inverter reports that the grid voltage at its AC terminals is outside the allowed protection range, and it disconnects from the grid. In monitoring data, AC output stops while the measured grid voltage is above or below the set limits. Some inverters also trip on the ten-minute average voltage. Usually the inverter reconnects by itself once the grid is normal again, so first watch it for about ten minutes to see whether the alarm clears. If the alarm keeps coming back, measure the actual grid voltage at the inverter. If it really is out of range, or the phases differ a lot, contact the utility. If the grid voltage measures normal, check the AC connections and cable between the inverter and the grid. Make sure the cable is firmly in place and its cross-section is large enough, because high impedance at the connection point can push the voltage up. Also check that the voltage protection settings are right for the grid standard that applies. Change them only with the grid operator's consent. On CPS inverters, restart the inverter after the cause is fixed. If the fault persists, contact the manufacturer's service.

<!-- review notes
- sentence 5: support check: partial - Passages say to check AC connections, cable firmness and cross-section, and that grid impedance is too high, but they do not tie these to the case where voltage measures normal.
- sentence 6: support check: partial - Passages say to check protection parameters and modify overvoltage values only with operator consent, but the grid-standard match and consent for all settings (including undervoltage) are not fully stated.
- sentence 7: support check: partial - u1 says restart the inverter, but 'restart after the cause is fixed' and 'contact the manufacturer's service' for CPS are not stated for CPS; the contact-service text is from Sungrow.
-->
