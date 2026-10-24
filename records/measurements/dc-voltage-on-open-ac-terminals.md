---
id: meas:dc-voltage-on-open-ac-terminals
type: Measurement
name: DC voltage on open AC terminals
aliases:
- DC measurements on the AC side
- DC voltage on AC output terminals
---
A multimeter shows a DC voltage on the inverter AC output terminals, measured from a line terminal to Neutral or to Protective Earth. It appears when the PV strings are still connected to the inverter but the AC connection to the grid is switched off or disconnected. The cause is the inverter's internal voltage sampling circuit, which monitors grid voltage through high-impedance measuring resistors tied to the AC terminals and stays connected while the AC breaker is open. With the PV array connected, DC voltage sits on the internal DC bus and can be read through this sampling circuit on the AC side. The manufacturer says this reading does not mean the inverter is faulty and can be normal under these conditions. The voltage goes away once the grid is connected, because the grid provides a very low DC impedance path. Before any maintenance, isolate both the AC and the DC supplies, wait for the capacitors to discharge, and check that the AC and DC terminals read zero.
