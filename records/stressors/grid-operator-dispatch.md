---
id: stressor:grid-operator-dispatch
type: Stressor
name: Grid operator dispatch
aliases:
- grid dispatch
---
Grid operator dispatch is an instruction from the grid operator that caps how much power a PV plant may export, even when the plant could produce more. It is one of several causes of grid curtailment yield losses. The others are interconnection constraints, plant controller commands, responses to negative pricing and site-level export caps. Dispatch does not physically damage modules or inverters. It lowers the energy the plant delivers and makes performance metrics harder to read, while availability and equipment health stay normal. In the data it shows up as flat or held-down output below the power the irradiance could support. Because inverters and trackers look available, it is easy to mistake for underperformance unless setpoints and dispatch signals are checked. To confirm it, rebuild the available power from irradiance, temperature, inverter status and clipping state. Compare that with meter output, plant setpoints, inverter active power limits and the operator's dispatch records, then label each constrained interval by its cause. To limit the impact, track curtailment separately from equipment losses, improve available-power estimates, tune battery charging where storage exists and use performance metrics that account for curtailment. Grid-relevant inverter parameters may only be changed with the grid operator's approval. Settings reserved for grid operators should be left alone unless the operator specifically asks for a change.

<!-- review notes
- sentence 1: support check: partial - Passage lists grid operator dispatch as a limitation source and defines curtailment as output capped below capability, but doesn't define dispatch as an operator instruction explicitly.
- sentence 3: support check: partial - Passages say curtailment reduces energy, complicates metrics, and availability/equipment health stay normal, but don't state that it doesn't physically damage modules or inverters.
-->
