---
id: arch:hybrid-inverter-system
type: Architecture
name: Hybrid inverter system
aliases:
- hybrid inverter
- PV + battery inverter
- hybrid power system
category: Storage
---
A hybrid inverter system uses one inverter that does the jobs of both a PV inverter and a battery inverter. It can send PV DC power into the battery or turn it into grid-compliant AC, and it can also turn battery DC into AC. The main parts are the hybrid inverter, the battery and an external energy meter. The meter uses current transformers to measure the power the site draws from the grid and consumes. These systems are mainly used in homes to raise self-consumption and supply backup power. Some models can run both on-grid and off-grid. Depending on the model, the inverter works with low-voltage 48-52V lithium-ion or lead-acid batteries, or with high-voltage batteries. The system can run without a battery, with the hybrid unit acting like a normal PV inverter. A battery can be added later. A hybrid inverter with a battery can be AC-coupled to an existing microinverter or string inverter system, so it charges the battery from that system's AC output. If no meter is installed, the battery only charges and discharges on time-of-use schedules. Export limiting is built in: the inverter reads its own meter and cuts back PV output to stay under the set limit. This works with or without a battery. A separate Solis Export Power Manager is not compatible with hybrid inverters because they already control export through their own meter and CTs.

<!-- review notes
- sentence 2: support check: partial - The passages give the inverter, battery and external energy meter with CTs measuring consumed/imported power (Solis), but the meter's CT use comes from Solis text while the SMA system lists only an Energy Meter; 'battery' as a main part is only loosely stated since the system works without one.
- sentence 3: support check: partial - Residential use, self-consumption and backup power, and on-grid/off-grid operation are stated, but 'some models' is not clearly stated (the passages say the series can operate in both) and 'mainly used in homes' is only 'designed for residential'.
- sentence 5: support check: partial - Operation without a battery as a normal PV inverter is stated, but adding a battery later is not explicitly stated.
-->
