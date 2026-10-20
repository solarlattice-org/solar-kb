---
id: symptom:dc-overvoltage
type: Symptom
name: DC overvoltage
aliases:
- PVx Over Volt
- PV2VoltOver
- OV-DC
- DC voltage is too high
---
The inverter reports that the voltage at its DC input is higher than it is rated for, and this can permanently damage or destroy the inverter. SMA inverters also flash their LEDs rapidly for this message, and the instruction is to disconnect the PV array. On CPS SCA36KTL and SCA50/60KTL units the alarm is PVx Over Volt, and the open-circuit PV voltage must stay below 1000V. Start by switching the DC off, measuring the voltage at the DC terminals or test points with a meter, and comparing it with the inverter display. If the display does not agree with the meter within 2%, the inverter's measuring circuit is likely faulty and the inverter should be replaced. If the meter confirms the high voltage, the string is too long: check the string configuration and reduce the number of modules. Before connecting new strings, check their polarity, open-circuit voltage and length to prevent this alarm.

<!-- review notes
- sentence 1: support check: partial - Passages say overvoltage at the DC input can destroy the inverter and exceeding max DC voltage may cause permanent damage, but 'higher than it is rated for' is only implied and not stated for the alarm itself.
- sentence 2: support check: partial - Rapid LED flashing and 'Disconnect PV array' are stated, but the passages do not name the manufacturer as SMA (nor 'also').
- sentence 3: support check: partial - PVx Over Volt and the 1000V open-circuit limit are stated, and max DC input of 1000V for SCA36/50/60KTL, but the passages tie the alarm name to a generic row not explicitly to both models.
- sentence 5: support check: partial - Replacing the inverter when display is off by more than 2% is stated, and u38 mentions a possibly bad measurement circuit, but the 2% threshold and the 'likely faulty circuit' are from different rows and not directly linked.
- sentence 6: support check: partial - Passages say check string configuration or adjust number of panels in the string if the reading is accurate, but do not explicitly say 'reduce' modules or that the string is too long.
- sentence 7: support check: partial - u26 says to check polarity, open-circuit voltage, and string length before connecting DC cables to avoid overvoltage damage, but it does not mention this specific alarm.
-->
