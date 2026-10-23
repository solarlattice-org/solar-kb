---
id: meas:bad-packet-counter-increment
type: Measurement
name: Bad packet counter increment
aliases:
- Bad Packet Format
- Package error rate
---
On a meter's Modbus interface, a query with a format error is answered with an Illegal Data Value error code, and the Bad Packet Format communication counter goes up by one. A query whose data region has the wrong number of bytes also raises the Bad Packet Format counter, along with the Illegal Write counter. Do not confuse this with the ordinary packet count field, which rises by one for every packet in normal operation. On inverters, the same kind of problem shows up as an interface event saying the package error rate has changed to ok or high. A high package error rate means the network is overloaded, or the link to the network switch or DHCP server (router) is impaired or disturbed. To fix it, check that the Ethernet cable and connectors are undamaged and plugged in correctly. If needed, lengthen the data query intervals or reduce the number of devices on the network.

<!-- review notes
- sentence 3: support check: partial - PktCount is said to increment once per packet, but the passage doesn't say it differs from the counter or about 'normal operation'; the contrast is implied only.
- sentence 4: support check: partial - The interface event 'package error rate [ok / high]' is stated, but the passages don't link it to the same kind of problem as Modbus format errors.
-->
