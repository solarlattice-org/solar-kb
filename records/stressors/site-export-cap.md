---
id: stressor:site-export-cap
type: Stressor
name: Site export cap
aliases:
- site-level export cap
- export limit
---
A site export cap limits how much power a plant may send to the grid, even when the array could produce more. It is one cause of grid curtailment yield losses, along with grid operator dispatch, interconnection constraints, plant controller commands and responses to negative pricing. The cap does not physically damage modules or inverters. It leaves available solar resource unused, and equipment health and availability can stay normal. In monitoring data it shows up as a flat or controlled output level below what the irradiance supports, while inverters and trackers look available, so it is easily mistaken for underperformance. A low performance ratio during capped hours may reflect grid limits rather than a fault in the modules, inverters or trackers. To confirm it, rebuild the available power from irradiance, temperature, inverter status and clipping state. Then compare that with meter output and controller limits, and tag each constrained interval by cause, including export limit. On sites with storage, some capped energy can be recovered by charging the battery, but only if the battery has capacity, power headroom, control permission and an operating goal that values the charge. Track curtailment separately from equipment losses and use performance metrics that account for curtailment, so crews do not chase equipment problems that are not there.

<!-- review notes
- sentence 3: support check: partial - Unused resource and normal availability/health are stated, but the passages never say the cap does not physically damage modules or inverters.
-->
