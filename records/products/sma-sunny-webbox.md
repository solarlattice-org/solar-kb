---
id: prod:sma-sunny-webbox
type: Product
name: Sunny WebBox
aliases:
- WebBox
- Sunny WebBox-20
- Sunny WebBox Bluetooth
category: Monitoring and communications
make: sma
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:monitoring-gateway
  note: Central communication interface that collects and documents data from connected devices.
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: sec=2
    h: 326d4f4a98f0
  review: drafted
- claim_id: c2
  rel: implements
  target: func:remote-firmware-update
  note: Firmware can be updated over the Internet, from an SD card, or through the user interface; settings
    and data are kept.
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: sec=11.1.1
    h: 323d8080eec5
  - src: src:sma-doc-swebbox-ba-en-36
    loc: sec=h190
    h: 21db8d7d612e
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:modbus
  note: Optional Modbus server, port 502 by default. When it is enabled, users without a password can
    read instantaneous values and change the system time.
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: sec=10.4.1
    h: 5a0ce2804d8e
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  rel: uses_protocol
  target: proto:rs485
  note: Connects to the RS485 communication bus.
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=2.r11
    h: 36febe2b99f3
  - src: src:sma-doc-swebbox-ba-en-36
    loc: sec=13.1
    h: 417634b2848e
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:ethernet
  note: Ethernet connection to a computer or local network.
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: sec=13.1
    h: 417634b2848e
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:bluetooth
  note: Only the Sunny WebBox with BLUETOOTH Wireless Technology variant.
  cite:
  - src: src:sma-doc-246498
    loc: tbl=11.r4
    h: c99079c3b7df
  - src: src:sma-kb-sunny-webbox-bluetooth-perform-a-firmware-update
    loc: sec=h1
    h: d3b1f044ec20
  review: drafted
  review_note: 'support check: partial - A Bluetooth variant exists by designation, but passages do not
    explicitly state Bluetooth communication use; implied only.'
- claim_id: c7
  rel: compatible_with
  target: prod:sma-sunny-sensorbox
  note: The SensorBox records environmental data for performance monitoring through the WebBox.
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: sec=2
    h: 326d4f4a98f0
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The Sunny WebBox is the SMA data logger and central communication interface between a PV plant and its operator. It collects and stores data from the connected devices and makes it available over the Internet. You can view the plant data locally with Flashview or online through Sunny Portal. For Sunny Portal access, the router must forward Sunny Portal data requests to the WebBox. The WebBox talks to the inverters over the RS485 bus and reaches a computer or local network over Ethernet. It can also use a modem connection, and one variant adds Bluetooth wireless technology. A Modbus server can be switched on, using port 502 by default. Once it is on, anyone without a password can read live values and change the system time. Firmware can be updated over the Internet, from an SD card, or through the user interface, and settings and data are kept. Do not disconnect the power during an update. A Sunny SensorBox can be added to record irradiation and temperature data, and with a Power Reducer Box connected, the WebBox passes grid operator requirements on to the inverters. If the user interface cannot be reached, check the network settings, cabling, firewall, Internet access and IPv6 support of the proxy server. If an SD card is not detected, use an SD card supplied by SMA.

<!-- review notes
- sentence 1: support check: partial - Central communication interface collecting data and providing it over the Internet is stated, but calling it an 'SMA data logger' and 'stores' is only loosely supported ('documents', 'recorded data').
- sentence 3: support check: partial - RS485, Ethernet, modem and a Bluetooth variant are mentioned, but RS485 being to inverters is only implied (connect to inverter) and Bluetooth is only a variant designation.
-->
