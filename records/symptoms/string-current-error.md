---
id: symptom:string-current-error
type: Symptom
name: String current measurement error
aliases:
- String Err.
---
On FIMER inverters with monitored string fuses, this condition is reported as warning W017 "String Err." and the yellow LED flashes. It means the inverter recorded an error while measuring the string currents. The manual's main cause is one or more damaged string protection fuses. Check the fuses on the fuse boards with a multimeter first. Replace any open fuse. Then confirm the string input current stays within the fuse rating, especially where strings have been paralleled outside the inverter. If no fuse is damaged and the warning stays, check the webserver settings that declare which input strings are present or absent. A wrong setting points to a configuration error, not a hardware fault. In monitoring data, look for one string or input whose current falls well short of the mean of comparable inputs. Under stable irradiance, identical strings should typically be within 5 % of the average string current. If a string shows normal voltage but low or no current, the cause can be a module problem, an open or damaged connection, low irradiance or a faulty measuring device. To tell a string fault from an inverter input fault, move the suspect string to another MPPT input. If the low current moves with the string, the problem is in the string, and an IV curve trace should follow.

<!-- review notes
- sentence 4: support check: partial - The passage says to check the webserver settings (presence or absence of input strings) if no fuse is damaged, but it never says a wrong setting is a configuration error rather than a hardware fault.
- sentence 5: support check: partial - The passages support comparing string currents to the mean, and the 5% figure for identical strings under stable irradiance, but the 5% comes from commissioning test guidance rather than a monitoring-data criterion. The 'well short' framing is also not stated.
-->
