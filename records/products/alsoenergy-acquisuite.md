---
id: prod:alsoenergy-acquisuite
type: Product
name: AcquiSuite A8810 data acquisition server
aliases:
- AcquiSuite
- A8810
- AcquiSuite EMB
- AcquiSuite EMB A8810
category: Monitoring and communications
make: alsoenergy
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:monitoring-gateway
  note: Described as a data acquisition server collecting energy data from meters and environmental sensors.
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-datasheet-a8810-emb-1
    loc: sec=h2
    h: afabb39a2525
  - src: src:eq-equip-das-alsoenergy-locus-locus-energy-commercial-pv-monitoring
    loc: tbl=7.r1
    h: 251ac1ed3d66
  review: drafted
- claim_id: c2
  rel: manufactured_by
  target: org:obvius
  note: The datasheet calls it Obvius' AcquiSuite.
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-datasheet-a8810-emb-1
    loc: sec=h2
    h: afabb39a2525
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:modbus-rtu
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-datasheet-a8810-emb-1
    loc: tbl=1.r13
    h: dd7008dc80bf
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-a8810-manual-2
    loc: sec=h11
    h: a8a3fa679929
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:modbus-tcp
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-datasheet-a8810-emb-1
    loc: tbl=1.r13
    h: dd7008dc80bf
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:tcp-ip
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-datasheet-a8810-emb-1
    loc: tbl=1.r13
    h: dd7008dc80bf
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:ppp
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-datasheet-a8810-emb-1
    loc: tbl=1.r13
    h: dd7008dc80bf
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:http
  note: Listed as HTTP/HTML.
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-datasheet-a8810-emb-1
    loc: tbl=1.r13
    h: dd7008dc80bf
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:ftp
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-datasheet-a8810-emb-1
    loc: tbl=1.r13
    h: dd7008dc80bf
  review: drafted
- claim_id: c9
  rel: uses_protocol
  target: proto:ntp
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-datasheet-a8810-emb-1
    loc: tbl=1.r13
    h: dd7008dc80bf
  review: drafted
- claim_id: c10
  rel: uses_protocol
  target: proto:snmp
  note: Listed as SNMP-Trap.
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-datasheet-a8810-emb-1
    loc: tbl=1.r13
    h: dd7008dc80bf
  review: drafted
- claim_id: c11
  rel: uses_protocol
  target: proto:rs485
  note: Modbus/RS485 connection over shielded twisted pair; 120 ohm termination resistor for runs over
    200 ft.
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-a8810-manual-2
    loc: sec=h11
    h: a8a3fa679929
  review: drafted
- claim_id: c12
  rel: requires
  target: proto:ethernet
  note: Ethernet 10/100Mbit connection and Cat 5 cable listed as required hardware.
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-acquisuite-a8810-manual-2
    loc: sec=h11
    h: a8a3fa679929
  review: drafted
---
The AcquiSuite A8810 (AcquiSuite EMB) is a data acquisition server that collects energy data from meters and environmental sensors. An installation needs an Ethernet connection with Cat 5 cable and a 24VDC power supply; Modbus RTU meters can be added over shielded two-wire RS-485. Use a 120 ohm termination resistor on RS-485 runs longer than 200ft, and get the IP address, netmask, gateway, DNS and any HTTP proxy settings from the site administrator.
