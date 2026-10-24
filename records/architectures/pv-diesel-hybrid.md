---
id: arch:pv-diesel-hybrid
type: Architecture
name: PV-generator hybrid system
aliases:
- PV-diesel hybrid
- generator-coupled system
- genset hybrid
- hybrid system
- PV hybrid systems
category: Storage
---
A PV-generator hybrid system pairs a PV array with an electric generator, usually a genset with a combustion engine. Because it draws on more than one energy source, it is called a hybrid. The generator backs up the PV array when the array cannot produce enough energy on its own to serve the loads or charge the batteries. It also covers periods when the weather is poor for renewable generation. Diesel generators are commonly paired with PV and energy storage in isolated microgrids. A generator can also reduce the PV array and battery size needed, shifting capital cost toward ongoing fuel cost. Many battery-based inverters can start the generator through a relay or dry contact when the battery reaches a low voltage or minimum SOC. They stop it again once the battery reaches the target charge set in the inverter. On some hybrid inverters, the generator is used only while the system is running off-grid. In those cases the generator and an AC-coupled PV inverter may not be connectable at the same time. A grid-tied PV system without batteries needs a separate generator transfer switch, because most generators cannot connect directly to the grid without extra synchronizing and protective equipment. In larger plants, a programmable controller such as the SMA Hybrid Controller manages the energy flows between the PV, genset and battery sources. It can talk to genset controllers over CANopen. When hybrid inverters run in parallel on one generator, a transfer switch is recommended. The generator should be rated at or slightly above the combined rated AC power of the inverters.

<!-- review notes
- sentence 3: support check: partial - u26 says a diesel generator can be paired in isolated micro-grids and can reduce PV/storage sizing shifting cost to fuel, but 'commonly' is stronger than 'in certain settings, particularly'.
- sentence 4: support check: partial - Start at low voltage/min SOC and stop at target SOC are stated, but u25 says relay circuits and u35 dry contact for Solis; 'many' inverters is roughly supported, though stopping at target is only in Solis and 'relay or dry contact' is covered across passages; generally core supported with minor generalization.
- sentence 7: support check: partial - The passages say the SMA Hybrid Controller manages energy flows among PV, genset and battery and uses CANopen to genset controllers (optional), but 'in larger plants' is not stated.
-->
