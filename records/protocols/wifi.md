---
id: proto:wifi
type: Protocol
name: Wi-Fi
aliases:
- WLAN
- IEEE 802.11
- WiFi
category: Communication
protocol_kind: transport
---
Wi-Fi is the IEEE 802.11 wireless network link. Inverters and data loggers use it to join a local network or to connect directly to a phone or tablet. The Delta DC1 controller supports IEEE 802.11 b/g/n, with 802.11b running at 1 to 11 Mbps and 802.11g at 6 to 54 Mbps. On SMA inverters that have a Wi-Fi interface, it is on by default when shipped. It can be switched off, and the direct connection and the local-network connection can be turned on or off separately. SMA products with Wi-Fi also have a WPS function, which connects the device to a router automatically or sets up a direct link to a smart device. The Enphase IQ Gateway broadcasts its own Wi-Fi network (AP mode) so installers and homeowners can do limited tasks. It can be reconnected to home Wi-Fi through the Enphase App, and the Enphase Installer App can also configure Wi-Fi. If an IQ Gateway shows offline behind a Wi-Fi extender, check that the extender is within range of the gateway and that the gateway is joined to the extender's network, whose name usually includes _EXT. The FIMER PVS-166/175-TL-US can receive firmware updates and parameter upgrades over Ethernet or WLAN, with the parameter upgrades following the SunSpec Modbus protocol. SolarEdge inverters are set up for Wi-Fi with the SetApp app.

<!-- review notes
- sentence 1: support check: partial - Passages give IEEE 802.11 Wi-Fi and joining a local network or direct connection to a smart device, but nothing on data loggers or phone/tablet specifically.
- sentence 2: support check: partial - Standards and data rates are stated, but nothing in the passages ties them to the Delta DC1 controller by name.
- sentence 5: support check: partial - AP mode broadcast for limited tasks and reconnect via Enphase App are stated, but the Installer App configuring Wi-Fi is only in a feature note about improved configuration, which loosely supports it; AP mode label is implied by the title.
- sentence 7: support check: partial - FIMER firmware and parameter upgrade claims are supported, but the passage for SolarEdge only has a title about Wi-Fi configuration using SetApp, which weakly supports it.
-->
