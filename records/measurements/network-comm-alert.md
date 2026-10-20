---
id: meas:network-comm-alert
type: Measurement
name: Network communication alert
aliases:
- communication disrupted
- Communication failure
- Network Fault
- LAN cable disconnected
- Gateway not responding
- network overloaded
- Network Communication
---
On SMA inverters this alert appears as an interface event saying communication is disrupted, which means the network line carries no valid signal. A related SMA event reports that the link status to the network switch or DHCP router has changed to OK, Warning, Error or Not connected, sometimes with an extra error message. A network overloaded event means the devices are no longer exchanging any data. Monitoring platforms can run a network communication rule that flags local network failures on devices linked over TCP and RS-485. On SolarEdge inverters, a LAN cable disconnected message points to a physical connection fault, so check the cable pin-out and connection. A gateway not responding message means a ping to the router failed, so check the cable and the link LED on the switch or router. On Yaskawa Solectria inverters, a Network Fault means a network connection has failed. Make sure the Ethernet plugs are firmly seated and the Wi-Fi antennas are mounted vertically. When a Tesla controller loses contact with a meter, it freezes the meter readings and may cut battery output to zero. Inspect the physical network connection. If an SMA inverter reports a general communication failure, the Service team must find the cause.

<!-- review notes
- sentence 7: support check: partial - Freezing readings and curtailing output to zero is stated, but only if the meter is required for the control function in use, and the statement omits that condition (says 'may', which roughly covers it); inspecting the physical network connection is stated.
-->
