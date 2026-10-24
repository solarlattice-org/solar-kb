---
id: prod:solis-dls-datalogger
type: Product
name: Solis DLS data logging stick
aliases:
- DLS-W
- DLS-L
- DLS-G
- Solis WIFI Stick
- Solis WIFI Dongle
- LAN Stick
- GPRS Datalogger
category: Monitoring and communications
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:kb-solis-44002437876-dls-w-solis-wifi-stick-troubleshooting-old-version
    loc: sec=h1
    h: 35677fcdf303
  - src: src:kb-solis-44002092757-solis-dls-l-lan-stick-troubleshooting
    loc: sec=h1
    h: af59d9287f01
  - src: src:kb-solis-44002005581-solis-dls-g-gprs-datalogger-setup-and-troubleshooting
    loc: sec=h1
    h: 19eb19f89e02
  review: drafted
  review_note: 'support check: partial - Passages call them ''Solis'' WIFI/LAN/GPRS sticks and mention
    Solis Service Center, but never explicitly state the manufacturer relation.'
- claim_id: c2
  rel: instance_of
  target: comp:monitoring-gateway
  cite:
  - src: src:kb-solis-44002437876-dls-w-solis-wifi-stick-troubleshooting-old-version
    loc: sec=h1
    h: 35677fcdf303
  - src: src:kb-solis-44002005581-solis-dls-g-gprs-datalogger-setup-and-troubleshooting
    loc: sec=h1
    h: 19eb19f89e02
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:wifi
  note: DLS-W variant; only 2.4 GHz networks are supported, a 5 GHz signal will not work.
  quote: Solis DLS-W only supports 2.4 ghz signals
  cite:
  - src: src:kb-solis-44002437876-dls-w-solis-wifi-stick-troubleshooting-old-version
    loc: sec=h1
    h: 35677fcdf303
  - src: src:kb-solis-44002219342-solis-wifi-dongle-setup-instructions-dls-w
    loc: sec=h1
    h: '662744655385'
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:ethernet
  note: DLS-L LAN stick connects by Ethernet cable to the router or, for setup, directly to a computer.
  cite:
  - src: src:kb-solis-44002092757-solis-dls-l-lan-stick-troubleshooting
    loc: sec=h1
    h: af59d9287f01
  review: drafted
  review_note: 'support check: partial - The LAN stick uses an ethernet cable connected directly to a
    computer for setup, but connection to a router is only implied via router-assigned IP and firewall.'
- claim_id: c5
  rel: uses_protocol
  target: proto:cellular
  note: DLS-G GPRS stick uses an inserted SIM card; APN is configured by SMS command.
  cite:
  - src: src:kb-solis-44002005581-solis-dls-g-gprs-datalogger-setup-and-troubleshooting
    loc: sec=h1
    h: 19eb19f89e02
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:rs485
  note: The data logger stick plugs into the inverter's 4-pin RS485 COM2 port.
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: sec=4.6.4
    h: 867507d10f98
  review: drafted
  review_note: 'support check: partial - COM2 is a 4-pin RS485 port used to connect a Solis data logger
    stick, but the ''DLS'' naming and the per-product protocol are not stated.'
---
The Solis DLS family is a set of plug-in data logging sticks for Solis inverters: DLS-W for Wi-Fi, DLS-L for wired LAN and DLS-G for GPRS cellular. The stick plugs into the communication port on the bottom of the inverter, which on the RHI-1P HV models is the 4-pin RS485 COM2 port, and the inverter address must be set to 1. The DLS-W works only on 2.4 GHz Wi-Fi. Its most common problems are a 5 GHz network, a wrong router password, weak signal, a firewall blocking data and outdated logger firmware. To configure DLS-W or DLS-L, open the stick's admin page at 10.10.100.254. For the LAN stick, first give the computer a manual IP address in the 10.10.100.x range. To reset the Wi-Fi or LAN stick, open the case, power it from a running inverter and hold the reset button for 5 seconds. If the portal shows no data, check that the remote server can be pinged and that the Wi-Fi RSSI is higher than 15 percent. Also check that the router firewall allows the Solis server ports, for example port 10000. When troubleshooting the Wi-Fi stick's link to the inverter, a technician can check for 5 VDC on pins 1 and 2 and for 1.5 to 1.7 VDC on pins 3 and 4. To set up the DLS-G, send an APN SMS command to its SIM card and then link the logger by serial number on the Solis platform. Its setup is different from the S3-GPRS-ST logger.

<!-- review notes
- sentence 2: support check: partial - Sticks plug into the bottom of the inverter and address must be 1/01, and COM2 is the 4-pin RS485 port, but the RHI-1P HV model scope is not stated.
- sentence 5: support check: partial - Both pages describe opening the case, powering from the inverter and pressing/holding the button for 5 seconds, but 'running inverter' is stated only for LAN.
-->
