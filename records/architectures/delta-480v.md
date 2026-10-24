---
id: arch:delta-480v
type: Architecture
name: 480 V three-phase delta service
aliases:
- 480 V delta
- ungrounded delta
- 480 V 3∅, 3 wire
category: Grid service
---
A 480 V delta service is a three-phase, three-wire supply that is usually ungrounded and offers only the line-to-line voltage, with no phase-to-neutral voltage. Delta circuits serve balanced loads such as three-phase motors well and are cheap to build with only three conductors, but unbalanced load currents lead to unbalanced voltages. Because the system is ungrounded, ground-fault protection is more complicated and ground faults take longer to clear than on a comparable grounded system. Inverter support varies by model: the SMA STP 30000TL-US-10 lists 480 V Delta as a compatible grid and needs no neutral connection, while the STP 15000TL-US-10 does not support it. Where co-located loads cause recurring line-to-ground faults that in effect make the service a corner-grounded delta, SMA requires the PV system to be isolated from the fault source to protect the inverters from excessive line-to-ground voltage. SolarEdge commercial inverters set their ground reference through the inverter, so they should not be connected to ungrounded or corner-grounded delta grids; delta applications need a separate isolation transformer. The Fronius Symo 480 versions list their output as 480 V Delta plus a neutral connection, so check each inverter datasheet for its delta and neutral requirements before connecting.

<!-- review notes
- sentence 7: support check: partial - u10 shows Symo 480 output as 480 V Delta +N, but nothing in the passages says to check each datasheet for requirements (the ** footnote isn't given).
- sentence 7: review: partial - The datasheet row shows Symo 480 output as 480 V Delta +N, but nothing in the passage supports the advice to check each datasheet before connecting.
-->
