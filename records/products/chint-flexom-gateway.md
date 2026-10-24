---
id: prod:chint-flexom-gateway
type: Product
name: CPS FlexOM Gateway
aliases:
- FlexOM Gateway
- CPS Flex Gateway
- FlexOM gateway card
category: Monitoring and communications
make: chint
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:chint
  note: Manual names Chint Power Systems America Co. (CPS).
  cite:
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: sec=h10
    h: b2396ffb8ea2
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:monitoring-gateway
  note: Described as an IoT cloud-based gateway.
  cite:
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: sec=2.1
    h: 66f3d9afdae8
  review: drafted
- claim_id: c3
  rel: implements
  target: func:remote-firmware-update
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: sec=h39
    h: 2d17325e6c4c
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=38.r13
    h: a836860653de
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=31.r6
    h: a836860653de
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: sec=2.1
    h: 66f3d9afdae8
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:rs485
  note: Multiple CPS inverters and other devices on one RS485 daisy chain; RS485 pass-through for a third-party
    client.
  cite:
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: sec=2.1
    h: 66f3d9afdae8
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:modbus-tcp
  note: Modbus TCP pass-through lets third-party controllers read/write CPS inverters.
  cite:
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: sec=2.1
    h: 66f3d9afdae8
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:bluetooth
  note: Built-in BLE for configuration via the CPS Connect Pro app.
  cite:
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: sec=2.1
    h: 66f3d9afdae8
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:ethernet
  cite:
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: tbl=1.r15
    h: c2b49463aa44
  review: drafted
  review_note: 'support check: partial - Only a table-of-contents entry ''Ethernet (FlexOM Gateway)''
    appears, implying an Ethernet interface but not stating usage.'
- claim_id: c8
  rel: uses_protocol
  target: proto:cellular
  conditions: FlexOM-4G version only; LTE-FDD/LTE-TDD, WCDMA
  cite:
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: tbl=3.r8
    h: 0721161e1a7b
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: tbl=3.r9
    h: e7661fbd1dbc
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:fcc-part-15
  note: FCC SDoC Part 15B and FCC ID Part 15C.
  cite:
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: tbl=4
    h: 83e34a5fe105
  review: drafted
- claim_id: c10
  rel: certified_to
  target: std:en-62368-1
  note: Listed under CE-LVD and CE-RED.
  cite:
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: tbl=4
    h: 83e34a5fe105
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:en-55032
  note: Listed under CE-EMC.
  cite:
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: tbl=4
    h: 83e34a5fe105
  review: drafted
- claim_id: c12
  rel: certified_to
  target: std:en-55035
  note: Listed under CE-EMC.
  cite:
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: tbl=4
    h: 83e34a5fe105
  review: drafted
---
The CPS FlexOM Gateway is a cloud-connected IoT gateway from Chint Power Systems. It connects CPS inverters to the CPS FlexOM monitoring portal. Several CPS inverters and other devices can share one RS485 daisy chain, and the portal can help diagnose RS485 wiring problems. RS485 and Modbus TCP pass-through let a third-party controller read and write inverter data alongside the gateway. You set it up over its built-in Bluetooth Low Energy link using the CPS Connect Pro app. It also has an Ethernet port, and the FlexOM-4G version adds an LTE/WCDMA cellular interface. It allows remote diagnostics and remote firmware upgrades for the inverters, which cuts down on site visits. It runs on 9 to 25 VDC through a terminal block and draws 2.5 W, up to a maximum of 5 W. The app's Recovery option restores factory settings, while Reboot restarts the gateway and keeps its current settings. Listed certifications are CE (EMC, RED, LVD) and FCC Part 15.

<!-- review notes
- sentence 4: support check: partial - BLE setup and FlexOM-4G cellular are supported, but Ethernet port is only a table-of-contents entry.
-->
