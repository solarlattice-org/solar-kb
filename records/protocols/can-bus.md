---
id: proto:can-bus
type: Protocol
name: CAN bus
aliases:
- CAN
- Controller Area Network
- CANbus
- Control Area Network
category: Communication
protocol_kind: transport
---
CAN bus is a sturdy serial bus for exchanging data between devices. Powin storage manuals spell it out as Control Area Network. The Solis RHI-1P HVES-5G hybrid inverters list CAN and RS485 as their communication interfaces. The SMA Sunny Island family uses the CAN bus to exchange information with batteries or their battery management system, and specific configuration settings are required for this. When Solis S6 hybrids run in parallel, the fault CAN BUS LOSE (106B) points to a loose parallel cable or a cable other than the supplied accessory. It can also mean missing cores in the 8-core wire, unshielded cable, damaged CAN hardware, a power supply problem or heavy interference. On SMA Home Storage, a multimaster error means CAN bus communication is disturbed, and the battery module's red LED flashes slowly. The fix is to commission each battery module on its own, note its serial number, then contact Service. The Generac PWRmanager has a CANbus terminal that is reserved for future functionality.

<!-- review notes
- sentence 1: review: partial - The Powin manuals do expand CAN as Control Area Network and call it a robust bus for communication, but they do not call it a 'serial' bus or say 'between devices'.
-->
