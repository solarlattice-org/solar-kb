---
id: proto:ocpp
type: Protocol
name: OCPP
aliases:
- Open Charge Point Protocol
- OCPP 1.6
- OCPP-J
- OCPP 1.6 JSON
- OCPP-J 1.6
category: Communication
protocol_kind: application
---
OCPP is the application-level protocol an EV charging station uses to talk to its backend system. The SMA eCharger 22 lists OCPP 1.6 JSON as its backend communication protocol. To commission the SMA EV Charger Business, connect to its Bender controller through the Micro-USB port and open the charger's web interface at 192.168.123.123. Under Network, turn on the LAN connection. Then on the Backend tab, choose Ethernet as the connection type, enter a ChargePoint ID, set the OCPP mode to OCPP-J 1.6 and enter the backend WebSocket address. To authorize RFID cards through the backend, switch on Enable OCPP Whitelist under Authorization, then save and restart the charger. The Power Electronics PowerSupervisor software shows OCPP connector status and error codes for each charging post on its charging stations, including the CHAdeMO, CCS and GBT connectors.

<!-- review notes
- sentence 1: support check: partial - Passages show chargers use OCPP 1.6 JSON/OCPP-J to a backend, but none state that OCPP is an application-level protocol for station-to-backend communication in general terms.
- sentence 5: support check: partial - The steps (Enable OCPP Whitelist On under Authorization, Save and Restart) are stated, but the purpose of authorizing RFID cards through the backend is only implied by the 'RFID Whitelist' heading.
- sentence 6: support check: partial - PowerSupervisor shows OCPP status and error codes for CHAdeMO, CCS and GBT connectors, but the evidence says connector status is OCPP and error codes are listed (only labeled OCPP in the summary view), and does not explicitly say 'for each charging post on its charging stations' beyond post-level views; mostly supported.
-->
