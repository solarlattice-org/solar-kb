---
id: meas:estop-relay-lights-off
type: Measurement
name: Emergency stop relay lights off
aliases:
- emergency switch relay
---
On Sunny Central cabinets, the emergency stop relay has indicator lights at the control unit. Depending on cabinet design and production version, it is mounted either there or elsewhere. In normal operation, both signal lights of the emergency stop relay should be lit. If they are off, the relay has dropped out. When an emergency stop switch is pressed, the relay lights switch to off. Sunny Central Control then shows error 206, which must be acknowledged manually after the switch is unlocked. The relay lights also stay off while any door contact switch is open. In Stop mode, Sunny Central Control shows no message for this. To check this signature, put the inverter in Stop with control voltage applied and tape the door contact switches on. Then operate each emergency stop switch: on the cabinet, in the stations and any external ones. Where several Sunny Central inverters run in a Team configuration, the emergency stop relay must switch in every cabinet. On other central inverters, pressing the emergency stop opens the DC load break switches and AC circuit breakers. The inverter then disconnects from the grid.

<!-- review notes
- sentence 1: support check: partial - Passage says that, depending on design and version, the relay is installed with the indicator lights at the control unit, but doesn't state the alternative of being mounted elsewhere.
- sentence 2: support check: partial - Passages say both lights must be lit in normal operation, but don't say that being off means the relay has dropped out.
-->
