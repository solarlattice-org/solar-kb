---
id: mit:latched-fault-reset
type: Mitigation
name: Manual reset of latched operation inhibition
aliases:
- Reset operation inhibition
- Resetting the operation inhibition
- Reset errors
- manual restart after arc detection
- Reset error
- confirm ArcContinuousFault
- Memory function reset error
- Manual reset of latched fault (operation inhibition)
- Resetting operation inhibition
---
Some SMA inverters can latch an operation inhibition. While it is latched, the inverter will not feed into the grid until someone resets it by hand. The usual trigger is an arc fault. When the arc-fault circuit interrupter is on and detects an arc, the inverter stops feeding in and inhibits operation. Whether an arc latches the unit depends on the manual restart setting. With On, every arc stops the inverter. With Off, the inverter pauses briefly and then resumes by itself. With the third option, it stops only after more than five arcs within 24 hours. To reset by parameter, go to Device > Operation, set Reset operating data to Reset operation inhibition, then start the system again. On some models, manual restart is turned on or off with the Manual restart activated parameter, and the arc behaviour is set with the Manual restart after arc detection parameter.

<!-- review notes
- sentence 2: support check: partial - The arc-detection behavior is stated, but the passages do not say an arc fault is the 'usual' trigger of operation inhibition.
-->
