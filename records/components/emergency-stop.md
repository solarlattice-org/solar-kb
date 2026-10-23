---
id: comp:emergency-stop
type: Component
name: Emergency stop circuit
aliases:
- emergency stop button
- emergency stop relay
- emergency switch relay
- fast stop
- Emergency stop external switch
- EmergencyStp
---
The emergency stop circuit lets an operator shut down the inverter at once by pressing an emergency stop button. Pressing the button opens the DC load break switches and the AC circuit breakers, which disconnects the inverter units from the grid. The button stays locked once pressed and has to be released with a key. To restart, release the button, switch the DC load break switches back on and follow the normal start-up procedure. Some inverters also have EPO+ and EPO- terminals for an external emergency stop switch, rated for wire sizes from 22 to 16 AWG. In central inverters, an emergency stop relay with indicator lights monitors the circuit. In Team configurations the relay has to switch in every cabinet. Emergency stop circuit defect is the main failure mode. One SMA inverter reports it as a defective fast stop, and the fix is to check the fast stop cabling. A tripped fast stop or a pressed emergency stop button also stops the inverter and raises an error. Remove the cause and switch the stop back on, or acknowledge the error manually.

<!-- review notes
- sentence 4: support check: partial - EPO+ and EPO- external emergency stop ports with 22-16 AWG are stated, but 'some inverters' is not stated and 'rated for' is slightly off.
- sentence 6: support check: partial - Error 9019 Defective fast stop with check fast stop cabling is stated, but the claim that it is the main failure mode is not in the passages.
-->
