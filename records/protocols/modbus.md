---
id: proto:modbus
type: Protocol
name: Modbus
aliases:
- Modbus protocol
category: Communication
protocol_kind: application
---
Modbus is an application-layer messaging protocol at level 7 of the OSI model. It provides client/server communication between devices connected on buses or networks. The protocol defines a simple protocol data unit that does not depend on the communication layers underneath. When Modbus is carried on a specific bus or network, extra fields are added to form the application data unit, and a function code tells the server what action to take. Modbus started as the common language of Modicon controllers. It sets the message structure, how a device recognizes its own address and messages sent to it, and how errors are detected and reported. On a serial line the master acts as the client and the slave nodes act as servers. Two-wire RS485 is the most common wiring, and RS232 can be used for short point-to-point links. On a serial bus only the slaves have addresses, and each address must be unique on that bus. Address 0 is reserved for broadcast. Inverter Modbus maps from CPS and Yaskawa Solectria contain read/write registers for remote dispatch enable and for the reactive power control mode. Tesla controls manuals list Modbus registers for the maximum active power limit, closed-loop control enable and power factor enable. Every SunSpec information model carried over Modbus begins with an ID register and a length register. This lets a client scan through the models and skip any it does not recognize.

<!-- review notes
- sentence 3: support check: partial - Passage supports common language of Modicon controllers, message structure, addressing/recognition and error detection/reporting, but does not say Modbus 'started as' that language (origin claim is slightly beyond it).
- sentence 6: support check: partial - Evidence shows CPS and Solectria RW registers for remote dispatch enable and reactive mode, and Tesla-style registers for max active power limit, closed-loop enable and PF enable; but Yaskawa Solectria's remote dispatch enable register (RemoteDispatchEn) is only shown for CPS-labelled entry, and Tesla attribution isn't explicit in the passages.
-->
