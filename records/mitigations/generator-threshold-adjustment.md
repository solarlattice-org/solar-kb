---
id: mit:generator-threshold-adjustment
type: Mitigation
name: Generator voltage and frequency threshold adjustment
aliases:
- adjust GnVtgMin/GnVtgMax
- adjust GnFrqMin/GnFrqMax
- set the thresholds for generator voltage
- GnVtgMin
- GnVtgMax
- GnFrqMin
- GnFrqMax
- Thresholds for Generator Connection
---
This action sets the battery inverter's voltage and frequency monitoring limits for the backup generator so that they match what the generator actually delivers. Use it when the generator keeps getting disconnected because its voltage or frequency is out of tolerance, for example when the minimum frequency limit is set too high. For voltage, open Generator > Generator > Voltage monitoring and set the lower minimum threshold to the generator's lowest voltage and the upper maximum threshold to its highest voltage. For frequency, set the generator nominal frequency to the generator's rated frequency, then under Frequency monitoring set the lower and upper thresholds to the generator's lowest and highest frequency. To choose suitable values, watch the measured voltage and frequency at the external connection while the system runs, and if needed adjust the generator's own voltage or frequency instead. Slightly narrower limits apply when the generator connects than when it is disconnected, and some of these parameters are only available in expert mode to a qualified person. After the change, clear the generator error by setting Acknowledge generator errors to Execute under Generator > Generator > Operation.

<!-- review notes
- sentence 2: support check: partial - Disconnection when outside limits and min frequency set too high are stated, but 'keeps getting disconnected' as the trigger is implied rather than explicit.
- sentence 6: support check: partial - Narrower limits for connection and expert mode for GnFrqMin are stated, but 'qualified person' requirement for expert mode isn't explicit and the narrower-vs-disconnected comparison is only loosely stated.
-->
