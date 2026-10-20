---
id: meas:islanding-breaker-open
type: Measurement
name: Islanding breaker open flag
aliases:
- Breaker Closed
- IslandingBreaker.BreakerClosed
---
This signature is a read-only boolean status point that reports the position of the islanding breaker on the site controller. A value of 1 means the islanding breaker is closed and the system is connected to the grid. A value of 0 means the islanding breaker is open and the system is running off-grid, which is the pattern to look for when islanding is reported. Over Modbus, the point is read from register 29025 as a single int16 value. An open breaker can also come from a deliberate command: a user can write the Intentional Island point to open the islanding breaker. Before treating an off-grid reading as unexpected, check the Intentional Island setpoint and its feedback point.

<!-- review notes
- sentence 3: support check: partial - 0 = breaker open, off-grid is stated, but the passages say nothing about it being the pattern to look for when islanding is reported.
- sentence 6: support check: partial - The setpoint and feedback points exist as user triggers to open the breaker, but the passages give no guidance to check them before treating an off-grid reading as unexpected.
-->
