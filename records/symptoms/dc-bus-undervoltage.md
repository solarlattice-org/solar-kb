---
id: symptom:dc-bus-undervoltage
type: Symptom
name: DC bus undervoltage
aliases:
- UN-BUS
---
The inverter raises a DC bus undervoltage alarm when it detects that the voltage on its internal DC bus is too low. Bus voltage is the voltage between the positive and negative poles on the inverter's DC side, and some inverters show it as a parameter. The manufacturer lists two likely causes: damage inside the inverter, or an internal wire that came loose during shipping. First, measure the DC and AC voltages at the inverter and compare them with the values on the LCD. If your measurements look normal but the display reports a low bus voltage, suspect internal damage; in that case the guidance is to replace the inverter. The matching DC bus overvoltage alarm has the same listed causes and checks, so handle both alarms the same way.

<!-- review notes
- sentence 2: support check: partial - The passages define Bus Voltage as the voltage between the positive and negative poles on the DC side, but they don't say that only some inverters show it as a parameter.
- sentence 5: support check: partial - The passage lists 'Replace Inverter' and 'Internal damage', but it doesn't tie replacement to measurements that look normal while the display shows a low bus voltage, or say to suspect internal damage in that case.
- sentence 6: support check: partial - The OV-BUS row has the same causes and solution steps as the undervoltage row. The passages don't say to handle both alarms the same way, and the detection condition differs (high vs low).
-->
