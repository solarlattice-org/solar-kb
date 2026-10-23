---
id: comp:residual-current-monitor
type: Component
name: Residual current monitoring unit
aliases:
- RCMU
---
The residual current monitoring unit is a protective circuit built into the inverter. It watches for residual current flowing between the PV modules and the inverter's grid connection. If it detects an improper residual current, it disconnects the inverter from the grid. SMA describes its version as all-pole sensitive. It monitors both AC and DC residual currents and disconnects from the grid redundantly when the residual current jumps suddenly. If the monitoring unit itself malfunctions, the inverter immediately disconnects all poles from the grid. SMA builds the unit to IEC/EN 62109-2 and VDE 0126-1-1. Fronius builds its unit to the Austrian standard ÖVE/ÖNORM E 8001-4-712. Some installations or utilities require an external residual current device as well. In that case, use a type B device with a high enough rated current, because a lower rating can cause false trips. Datasheets list the unit as standard on many string inverters, including SMA, Huawei and Solis models.

<!-- review notes
- sentence 7: support check: partial - Datasheet rows show the RCMU as available or supported, including Huawei SUN2000 models, but the passages don't name Solis or clearly identify SMA, and don't say 'standard on many'.
-->
