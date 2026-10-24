---
id: arch:off-grid-system
type: Architecture
name: Off-grid system
aliases:
- stand-alone system
- off-grid
- island system
- stand-alone grid system
- stand-alone grid
category: Storage
---
An off-grid system makes and supplies electricity on its own, with no connection to any outside supply such as the utility grid. In SMA designs a Sunny Island battery inverter acts as the voltage source for the stand-alone grid. It balances the energy coming in against the energy being used, and it manages the battery, generators and loads. PV inverters connected on the AC side feed the loads, and the Sunny Island uses their output to recharge the battery. A generator can be added to make the system more available and to allow a smaller battery. In single and single-cluster systems it connects to the AC2 terminal of the Sunny Island; in multicluster systems it connects directly to the Multicluster-Box. The firmware needed to commission an SMA off-grid system depends on how the system is built and on which outside energy source it uses. The table lists version 3.20.09.R or later for these setups. Typical uses are remote power for off-grid homes and villages, telecommunications, water pumping, lighting and navigation aids. With a few exceptions these systems store energy in batteries, and they are not designed to run in parallel with the utility grid or other sources. Grid-following string inverters such as the Solectria PVI 25TL-480-R are not intended for off-grid or microgrid use.

<!-- review notes
- sentence 3: support check: partial - u4 says AC sources (e.g., PV inverters) supply loads and are used to recharge the battery, but it does not say they connect on the AC side, though that is implied.
-->
