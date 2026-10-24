---
id: prod:advantech-adam-6000
type: Product
name: Advantech ADAM-6000 Ethernet I/O modules
aliases:
- ADAM-6000
- ADAM-6050
- ADAM-6051
- ADAM-6052
- ADAM-6050-D1
- ADAM-6051-D
- ADAM-6052-D
- ADAM
category: Monitoring and communications
make: advantech
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:io-module
  note: Industrial Ethernet-based I/O modules
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-sa-tmk-05-transformer-dry-contact-monitoring-kit-2020-06
    loc: sec=h9
    h: 652ee8aaaedf
  - src: src:powin-pc-s001-commissioning-procedure-rev5
    loc: tbl=3.r2
    h: aaf9696cca39
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:modbus-tcp
  cite:
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-cutsheet
    loc: sec=h1
    h: 5ad34ee3497e
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-6051-6052-ds-102622-20221027
    loc: sec=h1
    h: 5ad34ee3497e
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-6051-6052-ds-102622-20221027
    loc: sec=h16
    h: 4144c2724580
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-cutsheet
    loc: sec=h16
    h: '289392e87654'
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:tcp-ip
  cite:
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-6051-6052-ds-102622-20221027
    loc: sec=h16
    h: 4144c2724580
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-cutsheet
    loc: sec=h16
    h: '289392e87654'
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:ethernet
  note: One RJ-45 10/100Base-T(X) LAN port
  cite:
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-6051-6052-ds-102622-20221027
    loc: sec=h16
    h: 4144c2724580
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-cutsheet
    loc: sec=h16
    h: '289392e87654'
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:udp
  cite:
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-6051-6052-ds-102622-20221027
    loc: sec=h16
    h: 4144c2724580
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-cutsheet
    loc: sec=h16
    h: '289392e87654'
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:http
  cite:
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-cutsheet
    loc: sec=h16
    h: '289392e87654'
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:restful-api
  cite:
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-6051-6052-ds-102622-20221027
    loc: sec=h16
    h: 4144c2724580
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:dhcp
  cite:
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-cutsheet
    loc: sec=h16
    h: '289392e87654'
  review: drafted
- claim_id: c9
  rel: implements
  target: func:communication-loss-fallback
  note: Digital outputs can go to predefined values when communication breaks
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-sa-tmk-05-transformer-dry-contact-monitoring-kit-2020-06
    loc: sec=h9
    h: 652ee8aaaedf
  review: drafted
- claim_id: c10
  rel: certified_to
  target: std:ce-marking
  cite:
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-6051-6052-ds-102622-20221027
    loc: sec=h16
    h: 4144c2724580
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:fcc-equipment-authorization
  note: Datasheet lists FCC certification
  cite:
  - src: src:eq-equip-a-d-converters-adam-6000-adam-6050-6051-6052-ds-102622-20221027
    loc: sec=h16
    h: 4144c2724580
  review: drafted
---
The ADAM-6000 is a family of Ethernet I/O modules for industrial use. It includes the 18-channel ADAM-6050, the ADAM-6051 with a 2-channel counter, and the source-type ADAM-6052, all of them isolated digital I/O modules. Each module has one RJ-45 10/100 LAN port and plug-in screw terminals for I/O and power. It runs on a 10 to 30 VDC supply and draws about 2 W at 24 VDC. Using peer-to-peer and Graphic Condition Logic, a module can run on its own for measurement and control, with no separate controller or programming. You can also define your own Modbus addresses. Both a system watchdog and a programmable communication watchdog are built in. If communication is lost, the digital outputs can go to predefined safe values. The datasheet lists FCC, CE and UL certification and a Class I, Division 2 hazardous locations rating.

<!-- review notes
- sentence 1: support check: partial - Names and channel counts are supported, but ADAM-6050 is listed as 18-ch and ADAM-6051 as 14-ch with counter, ADAM-6052 16-ch; 'all isolated digital I/O' holds, though statement's wording is loose and fine; main issue is nothing contradicts, yet 'family' framing is inferred.
-->
