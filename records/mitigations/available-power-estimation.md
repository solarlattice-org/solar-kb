---
id: mit:available-power-estimation
type: Mitigation
name: Improved available-power estimation
---
This action makes the estimate of how much power the plant could have produced more accurate. It is one of the listed mitigations for grid curtailment yield losses. It applies when curtailment keeps export below the power the plant could deliver. Curtailment cuts the energy actually delivered and makes performance metrics hard to read, even when availability and equipment health are normal. At sites with storage, record whether curtailed PV energy was charged, clipped or abandoned. A battery can only recover curtailed energy if it has capacity, power headroom, control permission and an operating goal that values the charge. Use the estimate together with separate curtailment tracking and curtailment-aware metrics. A low performance ratio during curtailed hours may reflect grid instructions rather than a module, inverter or tracker problem. Without this separation, teams may chase false equipment faults and miss real gains in dispatch, controls or storage use. The sources give no figures for how effective the action is.

<!-- review notes
- sentence 1: support check: partial - Improving available-power estimation is a listed mitigation, but the passages don't say it makes the estimate more accurate in those words, which is close to a restatement of the action name.
- sentence 5: support check: partial - The passage supports chasing false equipment problems and missing opportunities in dispatch, controls or storage, but it ties this to not using curtailment-aware KPIs. The claim that the sources give no effectiveness figures is an absence the passages can't confirm, though none appear.
-->
