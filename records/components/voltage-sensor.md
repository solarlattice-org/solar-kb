---
id: comp:voltage-sensor
type: Component
name: Voltage sensor
aliases:
- measurement circuit
---
A voltage sensor measures voltage so that a monitoring system or an inverter can check it against expected or allowed values. In one research monitoring system, each PV module had its own voltage sensor, built as a voltage divider, alongside a current sensor. Readings from these sensors, plus irradiance and temperature, were compared with a neural network prediction, and a module was flagged for maintenance when predicted and actual power differed by more than 10%. In Canadian Solar three-phase inverters, an under grid voltage alarm (UN-G-V) may come from a bad voltage measurement circuit rather than a truly low grid voltage. This is the voltage measurement sensor fault. To check, switch the DC off, measure AC at the inverter test points and compare it with the voltage shown on the LCD. A low reading on the display with a normal measured value points to the measurement circuit. If the alarm stays after the grid standard has been checked with the DC switch on, the manual says to replace the inverter. These inverters carry protective circuits and controls so that they meet the relevant codes and standards.

<!-- review notes
- sentence 1: support check: partial - The passages show voltage sensors used in monitoring and an inverter checking grid voltage, but they don't state the general purpose of checking against expected or allowed values; that is only implied.
- sentence 4: support check: partial - The passage says to check the LCD reading because it may be a bad measurement circuit, but it doesn't name a 'voltage measurement sensor fault' and doesn't tie the alarm to Canadian Solar three-phase inverters in this passage.
- sentence 5: support check: partial - The passage lists switching the DC off, checking AC at the test points and checking the LCD reading, with a possible bad measurement circuit; it doesn't state the comparison logic of a low display against a normal measured value.
- sentence 6: support check: partial - The steps under DC switch ON are to check the grid standard and replace the inverter, but the passage doesn't say the alarm persisting after the grid check is the condition for replacement.
- sentence 4: review: partial - The rows support that UN-G-V may come from a bad measurement circuit, but the passage text does not name Canadian Solar or three-phase inverters, and it does not use the label 'voltage measurement sensor fault'.
-->
