---
id: comp:grounding-resistor
type: Component
name: Grounding resistor
aliases:
- grounding resistance
---
The grounding resistor is found inside inverters fitted with a grounding kit. It connects one pole of the PV generator to ground. When the inverter's Amorphous mode is enabled, it monitors the voltage across the resistor's terminals. Too much voltage across the resistor raises the E037 Riso Low alarm, which points to low insulation resistance in the array. On an E037 alarm, first check that the resistor is present and that both of its terminals make good contact inside the inverter. Next, short the array's positive terminal to its negative pole and measure the insulation resistance to ground with a megohmmeter. Do this in the same environmental conditions as when the error occurred. If the reading is below 1 megaohm, the PV generator needs checking for an insulation fault, which counts as a loss of electrical insulation. If the reading is above 1 megaohm and the alarm continues, contact customer assistance. Some module technologies, such as thin-film or back-contact modules, may require one pole of the array to be grounded. Always follow the module manufacturer's requirements and local regulations.

<!-- review notes
- sentence 3: support check: partial - The check of resistor presence and terminal contact is the first listed solution step, but the passages do not say it must be done 'first' as an explicit ordering (only bullet order implies it).
- sentence 5: support check: partial - The thresholds and actions are stated, but the passages do not say an insulation fault is classed as a loss of electrical insulation (this is an added gloss, and they describe checking the generator generally).
-->
