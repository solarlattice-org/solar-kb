---
id: proto:ethernet
type: Protocol
name: Ethernet
aliases:
- IEEE 802.3
- LAN
category: Communication
protocol_kind: transport
---
Ethernet is a network technology that covers the physical and data link layers, as defined by IEEE 802.2 and IEEE 802.3. Canadian Solar CSI-125KTL-GS-E and CSI-125K-T600GL02-U inverters list Ethernet among their communication connections, alongside RS485. FIMER PVS-166/175-TL-US inverters can receive firmware updates, locally or remotely, and parameter upgrades over Ethernet or WLAN, with parameter upgrades following the SunSpec Modbus protocol. Inverters can be wired as a daisy chain or in a star around an Ethernet switch. A ring is also possible: FIMER recommends connecting the first and last inverters to the switch so the chain stays connected if one link fails, and SMA allows a ring only when spanning tree is used. The LAN port is usually set to DHCP, where the router assigns an address automatically, or to Static, where you enter a fixed IP address and the related network fields by hand. If a SolarEdge inverter shows the message to configure static IP or set DHCP, check the IP settings on both the router and the inverter and consult the site's network IT staff.

<!-- review notes
- sentence 4: support check: partial - The passages support daisy chain, star, the FIMER ring recommendation, and a ring only with spanning tree, but they don't attribute the spanning-tree condition to SMA.
- sentence 5: support check: partial - DHCP and Static are supported with the router assigning the address and manual entry, but the passages don't say these are the 'usual' settings, and they mention DHCP as the default and the mandatory fields except the secondary DNS server, not a list of 'related network fields'.
-->
