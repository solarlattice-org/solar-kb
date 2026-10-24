---
id: proto:bacnet
type: Protocol
name: BACnet
category: Communication
protocol_kind: application
---
BACnet is a networking protocol for building automation and control, developed by ASHRAE for uses such as HVAC, lighting, access control and fire detection. BACnet works at the application layer. On Ethernet, the BACnet packet sits inside UDP, which sits inside IP, which sits inside the Ethernet frame. BACnet comes in flavors. BACnet IP runs over the IP protocol and links controllers to each other, controllers to HMIs, and some field devices. BACnet MS/TP runs over RS-485 serial wiring. A device called native BACnet supports the protocol directly, with no added gateway or module. The Accuvim II power meter offers BACnet IP and BACnet MS/TP as an option. The Eaton SPD publishes a BACnet map of analog, binary and device objects. On the Elkor WattsOn-Mark II M2 models, a BACnet MS/TP port takes the place of the Modbus/RTU port. You set the MS/TP network parameters from the on-board display, or from a Windows PC on the second RS-485 port, called the Expansion Bus. To configure the WattsOn over the Expansion Bus, wire a Modbus/RTU master to the X. Bus terminal and set the serial port to 115200,N,8,1. Write the MS/TP baud rate register, then write the Commit register to reset the network and apply the new settings. Tools such as BACnet Explorer can discover, browse, monitor and document BACnet networks.

<!-- review notes
- sentence 2: support check: partial - Nesting of BACnet in UDP, IP, Ethernet is stated, but 'works at the application layer' is only loosely implied (contents passed to the bacnet application).
- sentence 3: support check: partial - IP flavor applications are stated, but MS/TP running over RS-485 is only implied by headings (MSTP, RS485), not explicitly stated.
- sentence 5: support check: partial - BACnet IP/MS/TP optional is stated, but the passage doesn't name Accuvim II, and the BACnet map isn't attributed to Eaton SPD.
- sentence 7: support check: partial - Wiring, serial settings, and register descriptions are present, but the passages do not state the sequence of writing baud rate then Commit.
- sentence 8: support check: partial - Passage says BACnet Explorer does these things, but doesn't generalize to 'tools such as' it.
-->
