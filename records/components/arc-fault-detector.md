---
id: comp:arc-fault-detector
type: Component
name: Arc fault detection board
aliases:
- Arcing check board
- arc board
- arc-fault circuit interrupter
- AFCI
- arc fault sensor
- arc detection tool
---
The arc fault detection board is a part inside the inverter that watches the DC lines for arcing and sends a protection signal to the processor on the control board. It works by picking up the electrical noise that usually comes with a DC series arc, and the inverter shuts down when an arc is found. Arcs can occur in the PV modules and in the module wiring of the connected strings. When the circuit interrupter detects one, it stops the inverter and halts the current flow so the arc is broken. An arc fault shown on the display can only be cleared by hand, for example from the ARCFaultClear menu. A separate menu option turns the arc function on or off. If the board itself fails, the display shows an arc board error and the inverter stays off the grid until the board is working again. First check that the logic connector to the board is secure, then run the arc fault test. If the alarm comes back, contact service to replace the board or the wiring box. Arc fault trips are considered reliable signs of a real fault in the PV circuit and should be investigated right away. Repeated arcing can damage nearby conductors and may cause fires. Inverter arc fault detection is certified to UL 1699B, as required by NEC 690.11 for PV systems. Installing an arc detection tool is recommended as a mitigation where modules have cracked backsheets or defective or detached junction boxes.

<!-- review notes
- sentence 1: support check: partial - Passages say the arc check board detects arcing in the line and sends a protection signal to the control board DSP, but do not say it is inside the inverter or that it watches the DC lines specifically.
-->
