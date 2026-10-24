---
id: prod:accuenergy-axm-modules
type: Product
name: Accuenergy AXM expansion modules (AXM-WEB2 / WEB PUSH)
aliases:
- AXM-WEB2
- AXM-WEB
- AXM Series Module
- AXM-DIN
- WEB2 Manual
- WEB-PUSH
- WEB2 & WEB PUSH
- AXM-WEB-PUSH
- AXM-WEB2-FOLC
- AXM-WEB2-D
- AXM-WEB2 series modules
category: Metering
make: accuenergy
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:accuenergy
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-web-push-manual
    loc: sec=front
    h: cf1fed9c651b
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-axm-web2-user-manual
    loc: sec=front
    h: a266fa2db693
  review: drafted
- claim_id: c2
  rel: compatible_with
  target: prod:accuenergy-acuvim-ii
  note: Module plugs into the meter's rear socket by a communication plug.
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-axm-web2-user-manual
    loc: sec=front
    h: a266fa2db693
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-axm-series-module-datasheet
    loc: sec=h4
    h: 4fb17903cfbe
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=h3
    h: a9809bd29613
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=2.2
    h: 9f39746d03b6
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-web2-manual
    loc: sec=h8
    h: 1d58a011fcd7
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:accuenergy-acuvim-l
  note: AXM-WEB2 series; the WEB-PUSH manual names only Acuvim II.
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-axm-web2-user-manual
    loc: sec=front
    h: a266fa2db693
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-axm-series-module-datasheet
    loc: sec=h4
    h: 4fb17903cfbe
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=h3
    h: a9809bd29613
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=2.2
    h: 9f39746d03b6
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:modbus-tcp
  note: Slave only; default port 502, user range 2000-5999.
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=18
    h: 96b3b5e1b3e0
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=h3
    h: a9809bd29613
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.2
    h: f8d5b8cf22b5
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c5
  rel: uses_protocol
  target: proto:iec-61850
  note: Listed for WEB2 and WEB2-FOLC; 1st and 2nd edition.
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=18
    h: 96b3b5e1b3e0
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-axm-series-module-datasheet
    loc: sec=h4
    h: 4fb17903cfbe
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.2
    h: f8d5b8cf22b5
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:bacnet
  note: BACnet-IP on WEB2 series.
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=18
    h: 96b3b5e1b3e0
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-axm-series-module-datasheet
    loc: sec=h4
    h: 4fb17903cfbe
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.2
    h: f8d5b8cf22b5
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:dnp3
  note: DNP 3.0 V2 on WEB2 series.
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-axm-series-module-datasheet
    loc: sec=h4
    h: 4fb17903cfbe
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.2
    h: f8d5b8cf22b5
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:mqtt
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-axm-series-module-datasheet
    loc: sec=h4
    h: 4fb17903cfbe
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.2
    h: f8d5b8cf22b5
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c9
  rel: uses_protocol
  target: proto:snmp
  note: SNMP V2 and V3.
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=18
    h: 96b3b5e1b3e0
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.2
    h: f8d5b8cf22b5
  review: drafted
- claim_id: c10
  rel: uses_protocol
  target: proto:ntp
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.2
    h: f8d5b8cf22b5
  review: drafted
- claim_id: c11
  rel: uses_protocol
  target: proto:ftp
  note: FTP Post and sFTP server.
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=18
    h: 96b3b5e1b3e0
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.2
    h: f8d5b8cf22b5
  review: drafted
- claim_id: c12
  rel: uses_protocol
  target: proto:smtp
  note: Interval or event-triggered emails.
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=18
    h: 96b3b5e1b3e0
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.2
    h: f8d5b8cf22b5
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-web-push-manual
    loc: sec=h66
    h: fb7efc38e295
  review: drafted
- claim_id: c13
  rel: uses_protocol
  target: proto:ethernet-ip
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.2
    h: f8d5b8cf22b5
  review: drafted
- claim_id: c14
  rel: uses_protocol
  target: proto:wifi
  conditions: AXM-WEB2 and AXM-WEB2-FOLC models only
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=18
    h: 96b3b5e1b3e0
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.2
    h: f8d5b8cf22b5
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.1
    h: 95ba6a118b34
  review: drafted
- claim_id: c15
  rel: uses_protocol
  target: proto:ethernet
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-axm-series-module-datasheet
    loc: sec=h4
    h: 4fb17903cfbe
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=h3
    h: a9809bd29613
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.1
    h: 95ba6a118b34
  review: drafted
- claim_id: c16
  rel: uses_protocol
  target: proto:fiber-optic
  conditions: AXM-WEB2-FOLC model only (fiber optic LC port)
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=18
    h: 96b3b5e1b3e0
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=1.1
    h: 95ba6a118b34
  review: drafted
- claim_id: c17
  rel: implements
  target: func:remote-firmware-update
  note: Also manual .aup upload and an auto firmware update feature.
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-web2-manual
    loc: sec=11.1.2
    h: c9adf146bc72
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-axm-web2-user-manual
    loc: sec=9.1
    h: 491cb460d091
  review: drafted
---
The Accuenergy AXM-WEB2 and AXM-WEB-PUSH are add-on communication modules that plug into the back of Acuvim II meters. The AXM-WEB2 series also fits Acuvim-L meters. The WEB2 series comes in three versions: AXM-WEB2 with two Ethernet ports and Wi-Fi, AXM-WEB2-FOLC with one fiber optic LC port, one Ethernet port and Wi-Fi, and AXM-WEB2-D with two Ethernet ports and no Wi-Fi. The WEB2 modules support Modbus TCP, IEC 61850, BACnet-IP, DNP3, MQTT, SNMP, SMTP email, FTP and sFTP, NTP and EtherNet/IP. WEB-PUSH covers a smaller set built around Modbus TCP, a web server, email, SNMP, HTTP push and FTP. Modbus TCP works in slave mode only and uses port 502 by default. Datalogging memory is 8GB on the WEB2 versions and 4GB on WEB-PUSH. You can update firmware remotely, by uploading a .aup file by hand, or with the auto-update feature. The manual's compatibility table lists firmware v6.13 to v6.16 as compatible with bootloader v6.07. Only install or remove the module while the meter is powered off, to avoid injury or damage to the equipment. You can download a diagnostic file and send it to Accuenergy Technical Support to help troubleshoot the module.

<!-- review notes
- sentence 1: review: partial - The passages support AXM-WEB2 as a communication module that plugs into the back of Acuvim II and Acuvim-L meters, but for AXM-WEB-PUSH they give only a manual title, with no statement that it is a communication module that plugs into…
-->
