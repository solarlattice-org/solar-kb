---
id: comp:current-sensor
type: Component
name: Current sensor
aliases:
- AC current sensor
- Arc detector current sensor
---
A current sensor measures electrical current inside an inverter. Inverters include AC current sensors and current sensors that feed the arc detector. In module-level monitoring systems, a current sensor such as the ACS712 is fitted to each module together with a voltage sensor. The measured power is then compared with a predicted value to flag faults. When the arc detector current sensor is defective, Fronius inverters show status code 247 and disconnect from the grid. If the code keeps coming back, call a Fronius-trained service technician. Fronius Symo inverters report an AC current sensor fault as status code 315. If current sensor calibration times out (code 314), grid feed-in stops briefly and the inverter goes back to its startup phase. A faulty RCMU sensor (code 474) stops the inverter from feeding current into the grid. If the code keeps coming back, contact the system installer. The AC current sensor can be replaced in the field. Yaskawa instructions say it is held by two nuts and removed with a 7 mm socket. Solis lists the AC current sensor among the parts for which alternate materials were added to its certification report.

<!-- review notes
- sentence 1: support check: partial - Passages show AC current sensor and arc detector current sensor faults, but do not define a current sensor as measuring electrical current inside an inverter or state that inverters include them.
- sentence 4: support check: partial - Code 315 is AC current sensor fault, but the passage does not mention Symo models specifically.
- sentence 7: support check: partial - Evidence mentions two nuts and a 7mm socket for AC current sensor replacement, but doesn't name Yaskawa or explicitly state field replaceability.
- sentence 8: support check: partial - Report update adds alternate materials including AC current sensor, but the passage doesn't mention Solis by name.
- sentence 1: review: partial - The status codes confirm that inverters have AC and arc-detector current sensors, but the definition that a current sensor measures current inside an inverter is not stated.
-->
