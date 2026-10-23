---
id: meas:high-dc-input-voltage
type: Measurement
name: High DC input voltage
aliases:
- DC input voltage too high
- OV-DC
- High DC Voltage
- DC Voltage High
- Overvoltage at the DC input
signals:
- point: model_103.DCV
  unit: unit:V
  pattern: DC input voltage above the inverter's allowed maximum
---
The inverter detects a DC input voltage above its permitted level and reports it as an event code, for example Fronius code 309, either for the whole input or for one MPPT input. Central inverters log the same condition as a DC Voltage High event or a High DC Voltage fault. Overvoltage at the DC input can destroy the inverter, so treat this signature as urgent. Compare the reading with the inverter's maximum input voltage rating, which is 1000 V on several SMA string inverters and 1500 Vdc on a CPS 125 kW unit. To confirm, switch the DC switch off and measure DC at the inverter test points. If the voltage really is high, check the string configuration. If the field voltage is normal but the display still shows a high value with the DC switch on, the measurement circuit may be faulty (a voltage sensor fault), and the inverter may need replacing. Only use meters rated for a DC input range of 1000 V or higher, because overvoltage can destroy the meter. On Modbus-monitored units, a DC voltage register value of 32768 means the DC contactors are open and there is no voltage reading. Do not read it as an actual voltage.

<!-- review notes
- sentence 3: support check: partial - The passages state that DC overvoltage can destroy the inverter, but 'treat as urgent' is an inference not stated.
- sentence 6: support check: partial - The row says with the DC switch on to check the LCD reading, which may be a bad measurement circuit, and to replace the inverter; the 'voltage sensor fault' label and the condition that field voltage is normal are inferred.
- sentence 8: support check: partial - The register value 32768 meaning open DC contactors with no measurement is stated, but 'on Modbus-monitored units' generally and the instruction not to read it as voltage are only implied.
-->
