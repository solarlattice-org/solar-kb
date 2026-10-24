---
id: arch:ac-coupled-storage
type: Architecture
name: AC-coupled storage
aliases:
- AC coupling
- AC-coupled battery
- AC-coupled third-party PV
- AC-coupled system
- 'PV+BESS: AC-coupled'
- AC-coupled backup power system
- AC-Coupling at Grid Port
category: Storage
---
In AC-coupled storage the battery and the PV array connect to each other only on the AC bus. The storage inverter is a separate unit from the PV string or central inverters. PV power can feed loads directly through one conversion. To charge the battery, though, PV power has to pass back through a bidirectional inverter to become DC again, which costs some efficiency. This layout is common in residential systems. It is also the usual way to add batteries to an existing PV system, because it avoids rewiring and avoids possible conflicts with ownership agreements. The Solis S6 three-phase hybrid can be AC-coupled with both Solis and third-party three-phase grid-tied inverters. Update the hybrid to the latest firmware before commissioning any AC-coupled mode. SMA builds this topology from a Sunny Boy Storage, which is a single-phase AC-coupled battery inverter for grid-parallel operation, together with SMA PV inverters, a battery and an SMA Energy Meter or Sunny Home Manager. The Enphase IQ Battery is sold as an all-in-one AC-coupled storage product that works alongside the solar system. For monitoring, AC-coupled battery systems use a storage meter on the AC side of the battery.

<!-- review notes
- sentence 3: support check: partial - The passages say AC coupling is common in residential markets and that retrofitted batteries are typically coupled on the AC side to avoid wiring replacements and ownership-agreement violations. They don't say it is the usual way to add batteries to an existing PV system in general, and the ownership-agreement risk is 'potential'.
- sentence 5: support check: partial - u13 describes the Sunny Boy Storage as a single-phase AC-coupled battery inverter for parallel grid operation, with SMA PV inverters, an Energy Meter (optionally a Sunny Home Manager) and a battery. It does not say SMA builds 'this topology' from them, and the 'AC-coupled' link to this topology is only implied.
-->
