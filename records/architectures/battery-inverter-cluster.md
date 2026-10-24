---
id: arch:battery-inverter-cluster
type: Architecture
name: Battery inverter cluster
aliases:
- multicluster
- Sunny Island cluster
- single-cluster system
- multicluster system
category: Storage
---
A battery inverter cluster groups Sunny Island battery inverters on one battery. In a three-phase cluster there is one inverter per line conductor, three in total: one master and two slaves. The master is the control center. It switches and monitors the slaves, regulates frequency and voltage, manages battery charging and state of charge, requests the diesel generator and passes firmware updates on to the slaves. Only the master measures battery temperature, so the battery temperature sensor goes on the master only. All Sunny Island inverters in a cluster must be the same device type. The SI 4548-US-10 and 6048-US-10 can be mixed freely, including with older SI 5048U units. For more power, several clusters can be connected in parallel through a Multicluster-Box, which forms a multicluster system with one main cluster and several extension clusters. If an extension cluster master stops, only that cluster shuts down and the system keeps running at reduced power. If the main cluster master stops, the whole system shuts down. Multicluster systems with a battery-backup grid use the Multicluster-Box 12 (MC-Box-12.3-20) together with an NA-Box or Grid-Connect-Box. The battery state-of-charge ranges must be set to the same values for every cluster. Do not build multicluster systems on sites that fall under grid codes such as VDE-AR-N 4105, EN 50549-1, G98, G99 or CEI 0-21. Heavy energy transfer between clusters can come from very different battery capacities, different nominal voltage or frequency settings on the masters, or failed battery cells. To prevent it, spread battery capacity evenly across the clusters and give every master the same settings.

<!-- review notes
- sentence 4: support check: partial - Same device type requirement is stated and the SI 4548-US-10/6048-US-10 arbitrary combination incl. SI 5048U is stated, but these conflict in the passages (u20 is in a multicluster context) and the statement's 'mixed freely within a cluster' is not clearly reconciled.
- sentence 8: support check: partial - Causes (differing capacities, nominal voltage/frequency, failed cells) and remedies of even capacity and same master settings are stated, but for failed cells the remedy is disconnecting defective cells and setting new rated values, not merely prevention; also temporary SOC differences exist.
- sentence 4: review: partial - Both halves are quoted, but the 'arbitrarily combined' note sits under multicluster technology, not within a cluster, so presenting free mixing next to the same-device-type rule merges two scopes and leaves the apparent conflict unresolved.
-->
