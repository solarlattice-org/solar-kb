---
id: meas:transient-grid-overvoltage
type: Measurement
name: Transient grid overvoltage event
aliases:
- Grid transient overvoltage
---
Some inverters log a dedicated fault when the momentary grid voltage rises above the standard value, for example Sungrow fault code 003, Grid transient overvoltage. This is separate from the ordinary grid overvoltage fault, which is raised when the grid voltage sits above the set protection value. The inverter normally reconnects by itself once the grid is back to normal, and the manufacturer should be contacted if the fault keeps coming back. AC overvoltage can come from high grid resistance compared with the local PV peak capacity, or from too much resistance in the wiring between the inverter and the grid connection point. In monitoring data it can show up as a repeating cycle: the inverter disconnects, voltage falls, the inverter reconnects after its set delay, and voltage climbs again until the next trip, seconds to minutes later. Other inverters judge grid voltage on a ten-minute average rather than a short transient, then disconnect when the average leaves the permitted range because grid voltage or impedance is too high. Surge protection devices conduct current only briefly when a transient surge reaches them, and they draw very little current otherwise.

<!-- review notes
- sentence 7: support check: partial - The passage says this only about the TPS4 SPD unit, not surge protection devices in general.
-->
