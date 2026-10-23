---
id: comp:grid-protection-device
type: Component
name: External grid protection device
aliases:
- grid plant protection
- external grid and system protection
- Grid and system protection
---
An external grid protection device is a separate protection unit that watches grid parameters and makes the inverter shut down when the values leave the set limits. On KACO blueplanet TL3 inverters, the protection device's COM and NC contacts connect to the inverter's INV OFF+ and INV OFF- terminals. Additional inverters are chained together wire A to wire A and wire B to wire B. These inverters also provide an ERR connection where an external grid protection component can be wired in as a fault signal relay. When the device trips, the KACO inverter reports an external grid protection shutdown. Check that the protection unit has power and that its grid parameters and cabling are correct. If no external protection is needed, check that the function has not been turned on in the menu. On Fronius inverters, the built-in AC relays can serve as section switches for a central grid and system protection unit under VDE-AR-N 4105:2018:11. The trigger switch is wired into the wired shutdown chain. Regional rules may require external grid and system protection for systems above 30 kVA. On Fronius systems it can be left out when a Fronius Smart Meter IP measures the voltage remotely and the other listed conditions are met. On SMA inverters, you turn on grid and system protection with an inverter parameter. This requires a mounted SMA I/O Module and a minimum firmware version.

<!-- review notes
- sentence 1: support check: partial - Passage says shutdown was triggered by grid plant protection when grid values are outside limits, but doesn't describe it as a separate unit or explicitly that it makes the inverter shut down in general terms (mostly implied).
- sentence 4: support check: partial - The passage says to check the menu to see if the grid plant protection has been (text cut off), so 'turned on' is not stated; the rest matches.
- sentence 4: review: partial - The 'External grid protection shutdown' message and the power, grid-parameter and cabling checks are stated, but the menu check is cut off in the row, so 'has not been turned on' is not in the passage.
-->
