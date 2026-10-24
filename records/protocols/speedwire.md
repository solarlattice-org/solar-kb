---
id: proto:speedwire
type: Protocol
name: SMA Speedwire
aliases:
- Speedwire
- Speedwire Encrypted Communication
- SEC
- SMA Speedwire Encrypted Communication
- Speedwire encryption
category: Communication
protocol_kind: application
---
SMA Speedwire is SMA's own system communication between Speedwire devices. It runs on the Ethernet standard and is built for 100 Mbps data transfer. Inverters without a built-in Speedwire interface may need the Speedwire/Webconnect data module SWDM-10. You can configure Speedwire PV inverters with Sunny Explorer or an SMA Cluster Controller. The Cluster Controller sets up the Speedwire network and monitors and controls SMA devices that have Speedwire/Webconnect interfaces. Use Class 1 wiring methods for field wiring to the communication interface terminals. If an Energy Meter's Speedwire LED is off or the meter does not appear, check the network cable, and make sure the meter is on the same router or switch as the SMA communication product. Speedwire Encrypted Communication (SEC) encrypts traffic between Data Managers and inverters. All Speedwire devices in the system except the energy meter must support it. Inverters connected through an SMA Com Gateway do not support it. To replace or add a device in a system that uses SEC, first turn off the system encryption with Sunny Explorer. Then include the new device and turn encryption back on with a new password. If an SMA Data Manager is present, you can start a Speedwire diagnostic from its user interface, and the product's red LED will show whether communication is working.

<!-- review notes
- sentence 4: support check: partial - Class 1 wiring and the Energy Meter LED/network cable/same router advice are present, but the 'check the network cable' is roughly supported; the passage gives 'meter does not appear' cause as not on same network, which is covered, so only minor wording differs, though the 'Class 1' and troubleshooting are joined fine—core supported but cable 'check' is implied.
-->
