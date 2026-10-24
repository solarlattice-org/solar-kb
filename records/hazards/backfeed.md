---
id: hazard:backfeed
type: Hazard
name: Backfeed from another source
aliases:
- unexpected energization
- backfeed
- multiple sources
- back-fed
category: Electrical
---
Backfeed is the danger that a circuit you think is dead gets energized from another connected source. In PV systems that source can be a generator, a wind turbine, a fuel cell, storage or the utility grid. Interactive PV systems run in parallel with the utility grid and are synchronized to it. When PV output is greater than the site load, they push the surplus power back onto the grid. For safety, interactive systems must disconnect from the grid during utility outages or disturbances. Only special battery-based interactive inverters can keep powering critical loads on their own while the grid is down. A circuit between a PV system and an energy storage device has a supply source at both ends, so power can flow either way. Storage devices can deliver large short-circuit currents, so these circuits need overcurrent protection. When equipment is fed by more than one source, such as switchgear fed by both a utility transformer and a generator, a fault draws current from every source until each one is cleared. That has to be included when calculating arc flash incident energy. Fused disconnects and circuit breakers not marked line and load are treated as suitable for backfeed. Breakers marked line and load count as suitable only if they are specifically rated for backfeed or reverse current. Some microinverter and string inverter datasheets list the maximum backfeed current from the inverter to the array or input source as 0 A.

<!-- review notes
- sentence 1: support check: partial - Passages list generators, wind turbines, fuel cells, and the grid as other sources coupled with PV (and storage), but never define backfeed as the danger of a dead-seeming circuit being energized.
- sentence 6: support check: partial - The passage says fused disconnects are suitable unless otherwise marked, a condition the statement omits, and the statement's 'only if' for line/load breakers is stronger than the passage.
-->
