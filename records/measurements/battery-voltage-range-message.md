---
id: meas:battery-voltage-range-message
type: Measurement
name: Battery voltage range message
aliases:
- VBATMAX
- VBATMIN
- VBATMAXSL1
- VBATMAXSL2
- VBATMINSL2
- F201
- F716
- Battery error
- Battery fault
---
The Sunny Island battery inverter shows this message when the battery voltage it measures falls outside its allowed measurement range, either above or below it. The message tells you which device saw the problem: the master at L1, or slave 1 at L2 or slave 2 at L3. If the voltage is below the range, the usable battery capacity may be too small, for example because the battery has aged, or a high-power load may have connected. For a low reading, disconnect the DC loads, charge the battery and check that every battery cell works. If the voltage is above the range, check whether the battery voltage parameter BatVtg reads above 65.0 V. If it does, check the DC source settings and make sure the battery capacity is large enough. A related message, BatVtgHi, means the battery voltage is above the target charge voltage. When you see it, check that all DC sources are connected and configured correctly.

<!-- review notes
- sentence 6: support check: partial - u9 supports BatVtgHi as voltage above target charge voltage and checking DC sources are correctly configured, but 'connected and configured correctly' comes from VBATMAXSL2 row, not BatVtgHi (whose text is truncated).
-->
