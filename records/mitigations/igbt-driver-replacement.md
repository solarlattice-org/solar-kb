---
id: mit:igbt-driver-replacement
type: Mitigation
name: IGBT driver board replacement
---
On Sungrow central inverters, a major Module Fault is raised when the drive board is faulty or a hardware overcurrent occurs. This is the power stage fault that replacing the driver board addresses. Before replacing the board, check whether the AC or DC side of the IGBT module is short-circuited, confirm the grid is normal, and look over the IGBT modules inside the inverter unit for visible damage. The sources do not give a step-by-step procedure for the driver board alone. Yaskawa's XGI 1500 service instructions cover replacing the complete IGBT assembly instead. In that procedure, the ribbon cable is plugged into the Gate Adaptor board on the IGBT assembly. Check the connector orientation and make sure the latches close around the mating connector. Two technicians are needed: one holds the assembly against the drop-in panel while the other fastens it from the front, with every screw torqued to the specified value.

<!-- review notes
- sentence 1: support check: partial - Passage gives the Module Fault explanation and Major severity, but doesn't mention replacing the driver board as the remedy, so that claim isn't stated.
- sentence 2: support check: partial - The three checks are listed as measures, but the passage doesn't frame them as steps before board replacement, and 'visible damage' paraphrases 'appearances are normal'.
- sentence 5: support check: partial - Two technicians (one holds, one secures from the front) is stated, but only some screws have torque values given and one snubber screw is explicitly not torqued, so 'every screw torqued' is overstated.
- sentence 1: review: partial - The Module Fault row supports the first sentence (Major severity, drive board faulty or hardware overcurrent), but it never says that replacing the driver board addresses this fault.
-->
