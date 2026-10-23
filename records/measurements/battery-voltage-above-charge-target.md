---
id: meas:battery-voltage-above-charge-target
type: Measurement
name: Battery voltage above charge target
aliases:
- BatVtgHi
- VBATMAX
- BatVtgHiWarn
- Battery overvoltage
---
On Sunny Island battery inverters, event F 208 BatVtgHi means the measured battery voltage is higher than the target charge voltage. The device at L2 reports it. To confirm it, compare the battery voltage value BatVtg with the charging voltage target value BatChrgVtg on the device display or in the parameter list. Related messages report that the battery voltage at the master or at a slave is above the permissible measurement range. For those messages, the manual says to check whether parameter 120.02 BatVtg reads above 65.0 V. If it does, review the DC source settings and make sure the battery capacity is large enough. For F 208, check that all DC sources are configured correctly and that all SMA inverters use the country data set for stand-alone grid operation. Two warning variants exist. One flags high battery voltage that the device itself did not generate. The other flags a voltage that is only temporarily too high.

<!-- review notes
- sentence 2: support check: partial - Passages list BatVtg and BatChrgVtg as display values, but nothing states comparing them to confirm F 208 or mentions the parameter list.
- sentence 4: support check: partial - Check of 120.02 BatVtg above 65.0 V and DC source settings is stated for F 201 and W 202, but not W 203, which has a different measure.
-->
