---
id: meas:network-status-half
type: Measurement
name: Network status Half
aliases:
- duplex mode
- data transfer mode
---
This signature is an inverter event message saying that the duplex mode (data transfer mode) of the network interface has switched from Full to Half. On SMA inverters the change is logged as event number 10254 in the event list. The Half status can come from a defective plug or a defective cable. It can also appear when the network connector is pulled or plugged in. On an Ethernet connection, check that the network cable and connector are undamaged and that the connectors are plugged in correctly. Also check that the DHCP server (router) and any network switches show correct operation. A separate event, 10255, reports that network load has returned to normal after a busy period. It points to a network overload, not a duplex change.

<!-- review notes
- sentence 1: support check: partial - Passages say the duplex mode goes to [Full / Half] has changed, but don't state the specific Full-to-Half direction; the event covers a change to either value.
- sentence 6: support check: partial - Event 10255 and its meaning are stated, but the passages do not say it points to overload rather than a duplex change; that is an inference.
-->
