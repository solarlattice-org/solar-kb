---
id: state:island-operation
type: OperatingState
name: Island operation
aliases:
- off-grid operation
- stand-alone grid operation
- island mode
- stand-alone grid
- Off-Grid mode
- intentional island
category: Storage
---
In island operation, a battery inverter such as the Sunny Island supplies a stand-alone grid that is not connected to the utility grid. This is the opposite of grid operation, where the two grids are linked and share the same voltage and frequency. In a battery-backup system, the Sunny Island detects a utility power outage by itself and moves the connected Sunny Boy PV inverters into Off-Grid mode. For this switchover to work, the Sunny Island and the Sunny Boy inverters must share an RS485 data cable, and the Sunny Boy parameters must be set as SMA specifies. When the utility grid comes back, the Sunny Island returns to grid-tied operation under UL 1741. On Tesla battery systems, the user can set a voltage target and a frequency target for the battery system during off-grid operation. While running a stand-alone grid, the Sunny Island can report events at its AC1 connection, such as overvoltage, overfrequency, underfrequency or an unexpected voltage. These events point to a condition that needs checking and are not part of normal island operation. Battery-backup and off-grid setups need more battery modules than self-consumption setups. Check SMA's minimum module counts for the inverter model and phase setup before commissioning.

<!-- review notes
- sentence 1: support check: partial - Grid operation (connected, identical voltage/frequency) is stated, but the passages never describe island operation as the Sunny Island supplying a stand-alone grid not connected to the utility, nor state it as the opposite; only an off-grid term definition is given.
- sentence 3: support check: partial - Passage requires a data cable and parameters set per the document; RS485 is mentioned as necessary for communication with the utility grid as external source, but 'RS485 data cable' sharing is roughly implied, not exact.
- sentence 6: support check: partial - Passages state the overvoltage, overfrequency, underfrequency and undesired voltage events at AC1 in the stand-alone grid, but not that they need checking or are not part of normal operation.
- sentence 1: review: partial - The grid-operation half (grids connected, same voltage and frequency) is stated, but the passages never define island operation as the Sunny Island supplying an unconnected stand-alone grid, and never call it the opposite of grid operation.
-->
