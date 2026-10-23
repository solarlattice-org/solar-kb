---
id: meas:package-error-rate-high
type: Measurement
name: High package error rate status
aliases:
- package error rate [ok / high]
- '10250'
---
The inverter logs an interface event when its package error rate changes, and the status shows either ok or high. Some SMA event tables list this message as event number 10250. A high package error rate means the network is overloaded, or the link to the network switch or the DHCP server (router) is impaired or disturbed. On an Ethernet connection, check the network cable and connectors for damage and make sure the connectors are plugged in correctly. If the rate stays high, increase the data query intervals or reduce the number of devices on the network.

<!-- review notes
- sentence 5: support check: partial - Measures say 'if necessary' increase query intervals or reduce devices when rate is high; the 'stays high' persistence condition isn't stated.
-->
