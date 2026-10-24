---
id: comp:monitoring-gateway
type: Component
name: Monitoring data logger
aliases:
- data logger
- communication gateway
- Datamanager
- Envoy
- system gateway
- Monitoring gateway
- datalogger
- Gateway or data logger
- communications gateway
- control and communication gateway
- Fronius Datamanager
- Envoy-S
- SolrenView Data Logger
- Data Acquisition System
- DAS
---
A monitoring data logger gathers data from inverters, weather sensors, energy meters, string combiners and status signals, registering each device separately. It also raises basic alarms, keeps a temporary copy of the data while the internet link is down, and helps technicians check inverter feed-in during commissioning. Communication gateways pass the monitoring data to the manufacturer's portal. They can link inverters from the same or other brands, environmental sensors, revenue meters, third-party loggers and power reduction controls. Typical interfaces include Ethernet, RS485, RS232, ZigBee, Wi-Fi and a mini-USB port for software upgrades. Under best practice the logger keeps at least one month of data locally, three months is preferred, with a full cloud backup. The logger itself should be watched remotely so the operations room is alerted to failures and communication loss. A watchdog device or automatic reboot can hard-reset a logger that has stopped responding. A UPS should protect the whole monitoring installation, and IEC 61724-1 covers PV monitoring. Loggers should not be reachable directly from the internet, or should at least sit behind a firewall. Commands should go through a secure VPN connection. If a site gateway or router blocks outgoing traffic, add an outgoing rule so the data acquisition system can reach the monitoring servers.

<!-- review notes
- sentence 3: support check: partial - The SolarEdge gateway passage supports linking SolarEdge/non-SolarEdge inverters, sensors, meters, third-party loggers, power reduction devices and transferring data to the manufacturer's server, but it is a specific product, not communication gateways generally.
- sentence 4: support check: partial - The listed interfaces (Ethernet, RS485, RS232, ZigBee, Wi-Fi, mini-USB for software upgrade) are stated, but for the SolarEdge gateway specifically, with ZigBee/Wi-Fi sold separately/optional, not as typical interfaces generally.
- sentence 5: support check: partial - Passage says minimum one month (requirement) and best practice three months local plus cloud backup, and remote monitoring with alerts; but it does not say one month is best practice, and 'three months is preferred' is a mild rewording.
-->
