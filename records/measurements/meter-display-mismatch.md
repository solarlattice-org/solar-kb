---
id: meas:meter-display-mismatch
type: Measurement
name: Meter vs display mismatch
---
This signature compares two readings. One is the PV input voltage you measure with a meter at the DC terminals in the wiring box. The other is the voltage the inverter shows in its measurement data menu. Manuals tell you to make this check when the inverter raises a PV overvoltage protection code, such as PVVoltOver or PV2VoltOver. A mismatch means the display reading falls outside a 2% band around the meter reading. In that case the manuals treat the inverter's own measurement as untrustworthy and say to replace the inverter. If the display agrees with the meter within that band, the overvoltage is real. The fix is then to change the number of modules in the string or source circuit. The open-circuit PV voltage limit you check against depends on the model. Several manuals give 1000V, and one 1500V-class central inverter manual gives 1500V.

<!-- review notes
- sentence 3: support check: partial - Passages say to replace the inverter if the display is not within 2% of the meter, but they don't say the inverter's measurement is untrustworthy.
- sentence 4: support check: partial - Passages say to adjust the number of modules/panels when the display is within 2%, but they don't state explicitly that the overvoltage is real.
- sentence 5: support check: partial - Passages give 1000V in several manuals and 1500V in one, but nothing says the limit depends on the model or that the 1500V manual is for a central inverter.
-->
