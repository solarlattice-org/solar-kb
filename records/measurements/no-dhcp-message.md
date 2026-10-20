---
id: meas:no-dhcp-message
type: Measurement
name: No DHCP error message
aliases:
- DHCP Failed
- Invalid DHCP Config
---
The inverter shows a No DHCP error message on its communication status screen, which points to a problem with the IP settings. On the gateway, the same condition is reported as DHCP Failed or Invalid DHCP Config. It means the inverter got no valid IP address from the DHCP server, or the gateway's DHCP or static IP settings do not match the router's. A related message asks the user to configure a static IP or set the device to DHCP, and it also points to an IP settings issue. This is a network configuration problem. It is different from a disconnected LAN cable, which the guide lists as a physical connection fault. To troubleshoot, check the router and the gateway or inverter configuration, and consult your network IT. On other inverters, a change in communication status to the DHCP server or router may come with an additional error message.

<!-- review notes
- sentence 2: support check: partial - The gateway message and its description are stated. The passages never say it is 'the same condition' as the inverter's No DHCP message, so that equivalence is inferred.
-->
