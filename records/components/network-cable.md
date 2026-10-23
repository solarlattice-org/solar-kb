---
id: comp:network-cable
type: Component
name: Network cable
aliases:
- Ethernet cable
- Communication cable
- Data Cable
---
A network cable is the Ethernet link between a device such as an inverter or energy meter and a router or network switch. It carries monitoring and communication data. One inverter manual calls for a shielded CAT6 Ethernet cable, with no more than 100 m between the inverter and the router. If the cable cannot handle 100 MBit/s, a home energy manager may fail to find some or all of the devices connected over Speedwire. A damaged cable or plug, or a connector being pulled out and plugged back in, can drop the link speed to 10 Mbit or switch the duplex mode to Half. The inverter reports these changes as events. Events for no valid signal on the network line, or for a high package error rate, call for checking that the cable and connectors are undamaged and plugged in correctly. The checks also cover the router and switches. If the cable is not connected correctly to the network terminal, the Speedwire LED may stay dark and the energy meter may not show up in the communication product. A network cable tester is listed among the recommended tools for operation and maintenance work.

<!-- review notes
- sentence 1: support check: partial - Passages show a network cable connecting an Energy Meter/inverter to a router/switch, but don't explicitly define it as an Ethernet link or say it carries monitoring and communication data.
-->
