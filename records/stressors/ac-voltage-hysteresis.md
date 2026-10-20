---
id: stressor:ac-voltage-hysteresis
type: Stressor
name: AC voltage hysteresis
---
AC voltage hysteresis is a grid-side voltage behavior that can change the effective operating window of an inverter. It is a contributing cause of inverter voltage floor losses. In that failure, the array maximum power point voltage drops below the inverter's minimum DC input voltage, so the inverter has to run above the maximum power point and leaves energy unharvested. The problem is most likely in hot weather, because module voltage falls as cells heat up. High reactive power demand can make it worse. From production data alone, the loss can look like clipping or general underperformance. Check AC voltage and reactive power dispatch at the same timestamps as DC voltage and IV-derived Vmp. To reduce exposure, verify inverter settings and AC voltage behavior, and coordinate any transformer tap or voltage setpoint changes. Also confirm the reactive power requirements and retest MPPT recovery during hot operation. On the grid side, high AC voltage can also go past the inverter's overvoltage settings. The inverter then disconnects and reconnects repeatedly.

<!-- review notes
- sentence 2: support check: partial - Passages say Vmp falling below the inverter minimum forces operation above MPP, but AC voltage hysteresis is only said to change the operating window and be a possible root-cause factor, not explicitly a contributing cause of voltage floor.
-->
