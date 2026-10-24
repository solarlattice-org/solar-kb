---
id: proto:zigbee
type: Protocol
name: Zigbee
aliases:
- IEEE 802.15.4
category: Communication
protocol_kind: transport
---
Zigbee is a wireless protocol for moving data between devices. It uses the same frequency band as Wi-Fi and Bluetooth and builds a mesh, so devices can pass messages for each other when they have no line of sight. Every network has one coordinator, which creates the network and gives it a PAN ID. Routers and end devices join the network. Routers stay awake and can repeat traffic, while end devices sleep and cannot repeat. On Solar FlexRack tracker sites, the NCU gateway is the coordinator and the TCUs and RSUs are routers. Set the correct PAN ID in the TCUs so they join the right gateway. This matters most with double-gateway NCUs or sites with several NCUs. In SolarEdge systems, ZigBee cards or plug-ins inside the inverters connect wirelessly to a SolarEdge ZigBee gateway and on to an internet router. The protocol can be set to master, slave, point-to-point, multipoint master or multipoint slave. On SolarEdge HD-Wave inverters, the Smart Energy ZigBee option needs a ZigBee plug-in and an external antenna. The SolarEdge ZigBee status screen shows the PAN ID, the channel, the signal strength (low, medium, high or none) and the transceiver ID. If no ZigBee module is connected, the screen shows No ZigBee. SolarEdge lists the maximum ZigBee range as 400 m outdoors with line of sight and 50 m indoors, and an optional repeater can extend it. Enphase also offers Zigbee range extenders. The FTC Voyager zone controller has one Zigbee Pro 2007 interface, and its antenna cable screws onto a dedicated port. On Game Change Genius trackers, the Zigbee channel is set in Modbus register 40111.

<!-- review notes
- sentence 3: support check: partial - NCU coordinator, TCU/RSU routers and PAN ID configuration for double gateway/multiple NCUs are stated, but the passages never mention Solar FlexRack tracker sites.
- sentence 5: support check: partial - Smart Energy ZigBee needing a plug-in and external antenna is stated, but the passage does not mention HD-Wave inverters.
- sentence 6: support check: partial - PAN, channel, RSSI and ID are described, and No ZigBee appears when not connected, but the 'transceiver ID' and 'no ZigBee shows' are partly tied to field conditions, and the statement's single screen merges two different screen variants.
- sentence 8: support check: partial - One Zigbee interface (Pro 2007) and screw-on antenna port are stated, and register 40111 is the Zigbee channel, but the passages do not link the register to Game Change Genius trackers or name the FTC Voyager.
-->
