---
id: stressor:negative-pricing
type: Stressor
name: Negative power pricing
---
Negative power pricing is one reason a plant may limit export below what it could produce. The sources list a negative pricing response alongside dispatch, interconnection limits, controller commands and export caps. It drives grid curtailment yield losses: solar resource that is available but not exported becomes unused energy. It does not physically damage modules, inverters or trackers. Energy is lost even though availability and equipment health stay normal. In monitoring data it shows up as a flat or controlled output level below the power that irradiance could support, while inverter and tracker availability look normal. A low performance ratio during curtailed hours can be mistaken for underperformance. Review plant setpoints, active power limits, dispatch signals and curtailment flags before chasing equipment faults. To limit the impact, track curtailment separately from equipment loss, improve available-power estimates and use performance metrics that account for curtailment. At plants with batteries, some curtailed energy can be recovered by charging the battery. This only works if the battery has spare capacity and power headroom, is permitted by the controls, and has an operating objective that values the charge.

<!-- review notes
- sentence 2: support check: partial - Passages say curtailment turns available resource into unused energy, but they do not tie that loss specifically to negative pricing as the driver.
- sentence 3: support check: partial - Passages say availability and equipment health remain normal while energy is lost, but they never state that curtailment does not physically damage equipment.
-->
