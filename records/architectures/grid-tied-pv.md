---
id: arch:grid-tied-pv
type: Architecture
name: Grid-tied PV without storage
aliases:
- grid-tied
- grid-connected PV
- Grid-tied PV only system
- PV-only grid-tied
- grid-tied PV power system
- Grid-Tied PV System
category: System topology
---
A grid-tied PV system turns sunlight into DC power in the PV modules. Inverters convert that DC to AC that matches the grid's frequency and phase. A typical system has PV strings, grid-tied string inverters, DC and AC distribution equipment, and often an isolation or step-up transformer before the grid connection. The AC output feeds on-site loads first. Any surplus is exported to the utility grid. Manufacturers list this topology for commercial rooftops, large power stations and commercial or utility-scale plants. In its simplest form only the PV and grid ports are used. While the grid is present, the inverter produces as much PV power as it can, without measuring or limiting what goes to the grid. If the grid fails, the inverter shuts down and stops producing power, so this layout gives no backup. Export power control and monitoring can be added. With grid-tied-only inverters this needs an extra meter and CTs bought and installed separately, while Solis hybrid inverters ship with them. When a Solis hybrid inverter runs as a PV-only grid-tied unit, Solis sets no limit on how many can be paralleled in one system, and a battery can be added later.

<!-- review notes
- sentence 3: support check: partial - Passages say power can supply local loads and surplus goes to the grid, but do not state that loads are served first, though this is implied.
- sentence 6: support check: partial - The passage says the inverter shuts down on grid failure, but it also says it is capable of backup with only PV, so 'gives no backup' is not stated.
- sentence 8: support check: partial - The passage says there is no Solis limit on parallel inverters and a battery can be added later, but it does not say hybrid inverters specifically; 'this inverter' is unspecified.
-->
