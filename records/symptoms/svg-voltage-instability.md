---
id: symptom:svg-voltage-instability
type: Symptom
name: Reactive compensation voltage instability
aliases:
- SVG voltage stability alarm
- Fault7020
---
Monitoring systems can read it from Modbus register 0x841B, bit 2, where it is listed at the Trip Fault 7 level. Do not confuse it with Fault7010, which is a separate alarm for PID voltage stability. First, watch the inverter for 5 minutes to see if the alarm clears by itself. If the alarm stays or comes back, contact the manufacturer's after-sales service. In Q(U) mode the inverter changes its reactive compensation as the grid voltage changes, so check the reactive power settings and the grid voltage.

<!-- review notes
- sentence 1: support check: partial - Register 0x841B, Bit2, Trip Fault 7 level are stated, but 'Monitoring systems can read it' is an inference and fine; the passage lists the level as 'Trip Fault 7' which matches, so only the SVG alarm identity is implied.
- sentence 5: support check: partial - Passages state that in Q(U) mode reactive compensation changes with grid voltage, but nothing says to check reactive power settings and grid voltage as a troubleshooting step for this alarm.
-->
