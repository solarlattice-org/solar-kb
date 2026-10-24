---
id: arch:partial-home-backup
type: Architecture
name: Partial-home backup
aliases:
- protected loads panel
- backup loads panel
- partial backup
- dedicated loads backup
- protected loads subpanel
category: Storage
---
In partial-home backup, only selected key loads such as the fridge, lights and some outlets get power during a grid outage, not the whole house. The breakers for the backed-up loads are first identified in the main service panel, then moved into a new subpanel connected to the inverter's backup side. In the Generac PWRcell version, a PWRcell ATS sits between the main panel and the protected loads subpanel. When the grid fails, the inverter's internal relays isolate it from the grid, the transfer switch moves the subpanel to the inverter, and PV and battery power supply the loads. Choose the moved loads carefully, because too much load can exceed the system's maximum output rating and will shorten backup time. The installer has to size the protected loads panel so the system is not overloaded. Never connect the protected loads terminals to the grid, a generator or another inverter, and never parallel the protected loads outputs of several inverters. For Generac, this setup does not support three-phase 120/208 V installations, transfer switches from other manufacturers, or parallel operation with other storage systems. Bond neutral to ground only in the main service panel, never at the backup subpanel. A bond anywhere else can put current on the ground conductor, enclosures and piping. For SolarEdge, the Main Lug Only Backup Interface variant is described as ideal for partial home backup, but it is not suitable for a service side connection.
