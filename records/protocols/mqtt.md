---
id: proto:mqtt
type: Protocol
name: MQTT
category: Communication
protocol_kind: application
---
MQTT is an application-level publish/subscribe messaging protocol in which clients exchange data through a central broker. The broker is the server that every MQTT client connects to; it keeps track of message topics and forwards new messages to the clients subscribed to each topic. The Accuenergy AXM-WEB2 communication module lets an Acuvim II or Acuvim-L meter publish its device data to subscribers through an MQTT broker, and MQTT is listed on the Acuvim II and AXM-series datasheets. On the meter, MQTT is set up on the MQTT page under the Communications tab: enable the protocol, then enter the broker address, broker port, a unique client ID, the keep-alive interval in seconds and the clean session choice. With clean session set to Yes, session data and offline data are discarded; with No, queued messages are delivered after reconnection. Click Save MQTT to store the settings and Test MQTT to check the broker connection. On the FTC Solar Voyager tracker zone controller, a Mosquitto MQTT broker runs on TCP/IP port 1883 and carries communication between the controller's own application processes.

<!-- review notes
- sentence 1: support check: partial - Central broker and topic-subscription exchange are stated, but 'application-level' protocol is not stated in the passages.
- sentence 3: support check: partial - Publishing via broker for Acuvim II/Acuvim-L is stated; MQTT appearing on datasheets is only hinted by bare 'MQTT' entries (u5, u10) with no datasheet context.
- sentence 1: review: partial - The passages support publish/subscribe exchange through a central broker, but they never say MQTT is 'application-level'.
-->
