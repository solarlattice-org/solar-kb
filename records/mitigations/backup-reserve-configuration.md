---
id: mit:backup-reserve-configuration
type: Mitigation
name: Battery backup reserve configuration
aliases:
- Backup Reserve
- backup power range
- deep discharge protection range
- minimum state of energy
- Reserve SOC
- Reserved SOC
- Min Reserve SoC
- Backup power area
- BuRes
- Deep discharge protection area
- Battery Reserve Switch
---
Backup reserve configuration sets the share of battery capacity that is held back for supplying loads during a utility outage instead of being used for daily self-consumption. Once the state of charge falls to the reserve setpoint in self-supply operation, the battery stops discharging to local loads so that the reserve stays available for a grid failure. The setting is a trade-off: a lower reserve frees more capacity for self-consumption, while a higher reserve gives more backup energy; Generac ships it at 30% by default. When sizing the reserve, think about when an outage is likely, such as a weather event or a utility shutoff, and how much power the backed-up loads draw; one example gives about 1.2 hours of runtime from a 20% reserve on a roughly 10 kWh battery. On Solis systems the reserved SOC can be set from 10% to 100% when the reserve switch is enabled, and grid charging can be allowed so the reserve is kept topped up. SMA systems divide the battery into a backup power range, a deep discharge protection range and a deep discharge range, with defaults that depend on battery type; if the configured ranges add up to less than 100%, the backup range is enlarged automatically. On SMA systems the deep discharge protection range is only reached during a grid failure; the Sunny Island then goes into energy-saving mode and tries to recharge from PV every two hours, and it recharges from the grid once the grid returns. Make these settings in the energy management interface or the commissioning wizard, and in SMA multicluster backup systems set the same state-of-charge ranges on every cluster.

<!-- review notes
- sentence 3: support check: partial - The trade-off and 30% default are stated, but the passage doesn't name Generac, so attributing the default to Generac isn't supported.
- sentence 4: support check: partial - The considerations and the 2000 Wh / 1660 W = 1.2 hours example are given, but the passage doesn't say to consider how much power the backed-up loads draw, though the 1660 W figure implies it.
- sentence 5: support check: partial - The 10–100% range with the reserve switch and the grid-charging option are stated, but the passages never name Solis.
-->
