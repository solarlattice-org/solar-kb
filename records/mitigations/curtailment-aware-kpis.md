---
id: mit:curtailment-aware-kpis
type: Mitigation
name: Curtailment-aware performance metrics
aliases:
- curtailment-aware KPIs
- non-curtailed PR
---
Curtailment-aware performance metrics are KPIs built for plants whose export is often limited below the power they could produce. They are one of the listed mitigations for grid curtailment yield losses. They are needed because heavy curtailment distorts standard metrics. A low performance ratio during curtailed hours can reflect grid instructions more than the health of modules, inverters or trackers. Curtailment shows up as flat or controlled output below irradiance-supported available power while availability looks normal, so it is easy to mistake for underperformance. Use these metrics when a plant is constrained often. Otherwise teams may chase equipment problems that do not exist and miss real gains in dispatch, controls or storage use. A common method is to exclude the curtailed periods and calculate a non-curtailed performance ratio. Under IEC 61724-1, every data exclusion must be recorded. This exclusion approach usually gives valid results. Analyse carefully when curtailment covers more than half of the time. Combine this with tracking curtailment separately from equipment loss and with better estimates of available power.

<!-- review notes
- sentence 7: support check: partial - The mitigation list includes tracking curtailment separately and improving available-power estimation, but the passages do not say to combine them with the exclusion method.
-->
