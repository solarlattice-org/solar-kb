---
id: stressor:module-inverter-current-mismatch
type: Stressor
name: Module current above inverter input rating
aliases:
- high-current modules
- maximum continuous DC input current
- module Imp above inverter input
- M10 wafer modules 13-14 A
- panel incompatible with microinverter
- higher-current modules
- higher current PV modules
---
Newer PV modules use larger cells, which raises their wattage and the current they deliver at the maximum power point. M10 wafer-based modules are now the most common type, and their DC output current at STC is in the range of 13 A to 14 A. Each microinverter has a maximum continuous DC input current: 12 A for the IQ8 Series models listed, 14 A for IQ8MC, IQ8AC and IQ8HC, and 16 A for IQ9N. Before installing, check that the module's voltage and current specifications match the microinverter, and that the module short-circuit current is no higher than the microinverter's maximum input short-circuit current rating. The inverter's maximum input current has to be respected at both the lowest and the highest operating temperatures, and the manufacturer's module compatibility calculator can be used to check a pairing. On string inverters, the combined short-circuit current of all strings on one MPPT input must stay within that input's maximum short-circuit rating. To reduce exposure, pair high-current modules with microinverters rated for higher input current, choosing from the manufacturer's pairing tables based on DC/AC ratio and irradiance.

<!-- review notes
- sentence 3: support check: partial - 14 A for IQ8MC/AC/HC, 12 A (one table) and 16 A for IQ9N are stated, but the 12 A table isn't tied to specific IQ8 Series models listed, and u23 says IQ8 Series support up to 14 A.
- sentence 7: support check: partial - Passages support pairing higher-current modules with higher-input-current microinverters and tables based on DC/AC ratio and irradiance, but 'to reduce exposure' as a stated rationale isn't given.
-->
