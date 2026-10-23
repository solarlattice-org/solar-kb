---
id: meas:ac-terminal-voltage-low
type: Measurement
name: Low AC terminal voltage
aliases:
- VAC-Low
- InvVtgLo
- AC Voltage Low
- Very Low AC Voltage
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC phase voltage on the affected line conductor sags below normal when the event is logged
---
The voltage measured at the inverter's AC1 connection on a line conductor reads lower than it should. In stand-alone grids with battery inverters, the manuals blame AC sources elsewhere in the system for the drop. It can show up on the master unit's line conductor or on the slave units' line conductors. To check, disconnect all AC sources and loads, restart the inverter, and then reconnect sources and loads one at a time while measuring to find the cause of the undervoltage. If the low output voltage error also appears when the unit starts, possible causes are a permanent short circuit in the stand-alone grid or loads that need more power than the inverter can supply. Central inverters log AC Voltage Low as an event and have a separate Very Low AC Voltage fault. After that fault, the inverter waits for slaves to recover and for phase lock before it restarts. Monitoring registers may report low AC voltage as a status bit in the inverter event word. When the inverter reports undervoltage, measure the AC at the inverter test points and compare it with the display reading, because a faulty internal measurement circuit can also cause a low reading.

<!-- review notes
- sentence 5: support check: partial - Passages list AC Voltage Low event, Very Low AC Voltage fault, and waiting states, but do not say these are central inverters or that the inverter restarts after waiting; the sequence is implied only by fault names.
-->
