---
id: meas:low-ground-fault-resistance
type: Measurement
name: Low ground fault resistance
aliases:
- Insulation resistance low
- IsolationErr
- Isolation Resistance Low
- low insulation fault
---
The signature is a resistance between the DC conductors and ground that falls below the allowable limit, so the inverter reports a ground fault or low isolation resistance. Inverters and storage systems usually check this with built-in insulation test circuits, often by measuring insulation resistance before they start operating. The fault often shows up after rain or early in the morning when dew covers the modules. The inverter may flag it or shut off when the resistance drops below its limit. Typical causes are damaged conductor insulation, cracked backsheets, defective connectors and module insulation failure, which cannot be seen by eye. If a voltage check does not clearly show a ground fault, measure the insulation resistance. It gives a more exact result, and module defects are best confirmed under humid or wet conditions. To find the faulty string, isolate all strings, then reconnect them one at a time and restart the inverter until the alarm comes back. Then trace that string for leakage to earth. While a ground fault is active, do not touch the array, racking or inverter. Have a qualified person locate and repair it.

<!-- review notes
- sentence 4: support check: partial - Passages support damaged conductor insulation, cracked backsheets, connector defects (ground faults) and module insulation failure not visible by eye, but 'cannot be seen by eye' applies only to module insulation failure, not all causes.
-->
