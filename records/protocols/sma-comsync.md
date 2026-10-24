---
id: proto:sma-comsync
type: Protocol
name: SMA ComSync bus
aliases:
- ComSync
- SYNC communication bus
category: Communication
protocol_kind: transport
---
ComSync is the communication bus on SMA Sunny Island battery inverters. It is wired through the ComSync In and ComSync Out sockets and links the units of a cluster to each other. In a cluster the units are daisy-chained. Slave 1 takes the master's bus on ComSync In and passes it on to slave 2 from ComSync Out. Slave 2, at the end of the chain, keeps its terminator plugged in. Both ends of the bus must be terminated. From the factory, ComSync Out holds an RJ45 plug with 100 Ohm resistors across CAN-H/CAN-L and Sync-H/Sync-L. Plugs with 120 Ohm resistors are also acceptable under the CAN specifications. A lithium-ion battery's data cable connects to ComSync In. If no data cable is used, the terminator goes into ComSync In. For clusters, use CAT5e cable for the ComSync wiring, ideally the cables SMA supplies. The total ComSync wiring length must not exceed 30 meters. Sunny Island event 6123 or F703 (internal timing error) can come from a broken or poor-quality communication cable or a missing terminator. A single unit also needs the ComSync terminator, because two processors inside the device talk to each other over it.
