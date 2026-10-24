---
id: state:start-up
type: OperatingState
name: Start-up
aliases:
- soft start
- SOFT RUN
- starting
- ramp-up
- Soft start-up
- Power rampup
- Device start
- Startup status
category: Inverters
---
Start-up is the normal phase after an inverter is switched on or reconnects, when it raises its real power gradually instead of jumping straight to full output. The gradual ramp protects the grid from a sudden jump in feed-in power, which matters most after a grid-protection trip, when many plants could otherwise come back at the same moment. On some inverters you can choose when the soft start applies: at every switch-on, only at the first start of the day, or only after a grid-protection disconnection. The ramp works as a rising power ceiling. Actual output can move freely below it as the available power changes, but it never goes above it. Soft start only limits the ramp up, never the ramp down. If a normal ramp rate is also enabled, the inverter uses whichever of the two is lower. Solis inverters have a Ramp-up Slew Rate parameter that sets how fast power rises during start-up; the default is 100%. Start-up is a normal state and needs no action. On CPS inverters, a soft start that does not finish is reported as an inverter soft start timeout protection, with the fault LED blinking fast.

<!-- review notes
- sentence 6: support check: partial - Parameter, description and 100% default are stated, but passages don't name Solis explicitly and ranges vary (0-100 vs 1-100).
- sentence 7: support check: partial - The CPS-style soft start timeout protection with fast-blinking fault LED is in the row, but the claim that start-up is a normal state needing no action is not stated there.
-->
