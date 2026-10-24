---
id: prod:accuenergy-acuvim-ii
type: Product
name: Accuenergy Acuvim II power meter
aliases:
- Acuvim II
- AcuvimII
- Acuvim-II
- Acuvim Front Panel
- Acuvim Enclosure
- Accuvim Enclosure
- Acuvim II series
- Acuvim II Series Power Meter
category: Metering
make: accuenergy
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:accuenergy
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: sec=h2
    h: a1055307bd96
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:energy-meter
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: sec=h2
    h: a1055307bd96
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:rs485
  note: Built-in digital RS485 port; an extra RS485 module is optional.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: sec=h2
    h: a1055307bd96
  review: drafted
  review_note: 'support check: partial - Built-in RS485 port is stated, and the table lists an RS485 module
    with additional Modbus RTU, but the note that it is optional is only loosely implied.'
- claim_id: c4
  rel: uses_protocol
  target: proto:modbus-rtu
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: sec=h2
    h: a1055307bd96
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: tbl=2
    h: 1450582cae90
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:dnp3
  note: DNP 3.0 on RS485; DNP 3.0 over IP is listed as a communication option.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: sec=h2
    h: a1055307bd96
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: tbl=2
    h: 1450582cae90
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:ethernet
  conditions: Optional Ethernet module, 10M/100M
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: sec=h2
    h: a1055307bd96
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-power-meter-user-manual-1040e130
    loc: sec=h10
    h: 9904dc7cda7b
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: tbl=2
    h: 1450582cae90
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c7
  rel: uses_protocol
  target: proto:modbus-tcp
  conditions: Through the Ethernet module
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: tbl=2
    h: 1450582cae90
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:bacnet
  conditions: Optional module, IP or MS/TP
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: sec=h2
    h: a1055307bd96
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: tbl=2
    h: 1450582cae90
  review: drafted
- claim_id: c9
  rel: uses_protocol
  target: proto:profibus-dp
  conditions: Optional module, Profibus-DP/V0
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: sec=h2
    h: a1055307bd96
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: tbl=2
    h: 1450582cae90
  review: drafted
- claim_id: c10
  rel: uses_protocol
  target: proto:iec-61850
  conditions: 2nd edition; BTL listed for B-SA on Acuvim II, IIR, IIE, IIW
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=13.r6
    h: 47945a5f3541
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: tbl=2
    h: 1450582cae90
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:iec-62053-22
  note: Active energy class 0.1s
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=13.r1
    h: c8976d8f6255
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-power-meter-user-manual-1040e130
    loc: tbl=241
    h: 09aaf6653463
  review: drafted
- claim_id: c12
  rel: certified_to
  target: std:ansi-c12-20
  note: Active energy class 0.1
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=13.r1
    h: c8976d8f6255
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-power-meter-user-manual-1040e130
    loc: tbl=241
    h: 09aaf6653463
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c13
  rel: certified_to
  target: std:iec-61557-12
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=13.r1
    h: c8976d8f6255
  review: drafted
- claim_id: c14
  rel: certified_to
  target: std:iec-60068-2
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=13.r2
    h: 273608bf9a40
  review: drafted
- claim_id: c15
  rel: certified_to
  target: std:ce-marking
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=13.r2
    h: 273608bf9a40
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c16
  rel: certified_to
  target: std:eu-rohs
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=13.r2
    h: 273608bf9a40
  review: drafted
- claim_id: c17
  rel: certified_to
  target: std:iec-61010-1
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=13.r3
    h: ff0cf712f9d2
  review: drafted
- claim_id: c18
  rel: certified_to
  target: std:ul-61010-1
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=13.r3
    h: ff0cf712f9d2
  review: drafted
- claim_id: c19
  rel: implements
  target: func:power-quality-analysis
  note: Harmonics, crest factors and unbalance factors for voltage and current
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-power-meter-user-manual-1040e130
    loc: sec=h10
    h: 9904dc7cda7b
  review: drafted
- claim_id: c20
  rel: implements
  target: func:power-quality-event-logging
  conditions: Acuvim IIW model; up to 50,000 events with timestamp and trigger condition
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-power-meter-user-manual-1040e130
    loc: sec=h13
    h: 25ee66a0d6a9
  review: drafted
- claim_id: c21
  rel: compatible_with
  target: prod:accuenergy-axm-modules
  note: AXM-WEB2 Ethernet module
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-web2-web-push-axm-web2-user-manual
    loc: sec=front
    h: a266fa2db693
  review: drafted
  review_note: 'support check: partial - Only a manual title shows AXM WEB2 for Acuvim II; ''Ethernet
    module'' appears elsewhere, but WEB PUSH and compatibility are not detailed.'
- claim_id: c22
  attr: nominal_voltage
  value:
    nominal: 400
    unit: unit:V
  conditions: Voltage input nominal full scale, line-to-neutral (+20%)
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-power-meter-user-manual-1040e130
    loc: tbl=241
    h: 09aaf6653463
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=1
    h: a1545cc167ac
  review: drafted
  review_note: possible conflict with c23 (same source; check the conditions)
- claim_id: c23
  attr: nominal_voltage
  value:
    nominal: 690
    unit: unit:V
  conditions: Voltage input nominal full scale, line-to-line (+20%)
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-power-meter-user-manual-1040e130
    loc: tbl=241
    h: 09aaf6653463
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=1
    h: a1545cc167ac
  review: disputed
  review_note: possible conflict with c22 (same source; check the conditions)
  conflicts_with:
  - prod:accuenergy-acuvim-ii#c24
- claim_id: c24
  attr: nominal_voltage
  value:
    min: 100
    max: 415
    unit: unit:V
  conditions: Auxiliary power supply option P1, AC (also 100-300 Vdc)
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: tbl=8.r3
    h: 87018799fd7e
  review: disputed
  review_note: 'support check: partial - P1 is 100~415Vac and 100~300Vdc, but the passage does not call
    it ''nominal voltage'' of the auxiliary supply; it''s a supply range, which is acceptable, though
    it matches closely.'
  conflicts_with:
  - prod:accuenergy-acuvim-ii#c23
- claim_id: c25
  attr: frequency
  value:
    min: 45
    max: 65
    unit: unit:HZ
  conditions: Metering frequency range, standard type
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-power-meter-user-manual-1040e130
    loc: tbl=241
    h: 09aaf6653463
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=1
    h: a1545cc167ac
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c26 (same source; check the conditions)
- claim_id: c26
  attr: frequency
  value:
    min: 300
    max: 500
    unit: unit:HZ
  conditions: Metering frequency range, 400 Hz type
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-power-meter-user-manual-1040e130
    loc: tbl=241
    h: 09aaf6653463
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: tbl=1
    h: a1545cc167ac
  review: drafted
  review_note: 'support check: partial - 300-500Hz is listed and 400Hz type is mentioned for harmonics,
    but the link to the 400 Hz type is only implied.; possible conflict with c25 (same source; check the
    conditions)'
- claim_id: c27
  attr: warranty_term
  value:
    nominal: 5
    unit: unit:YR
  conditions: Brochure warranty statement
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: sec=h2
    h: a1055307bd96
  review: drafted
---
The Acuvim II series is a family of high-end multifunction power and energy meters made by Accuenergy for monitoring and controlling power distribution systems. Voltage inputs have a nominal full scale of 400 V line-to-neutral and 690 V line-to-line. Current inputs come in 5 A and 1 A options, including 333 mV and Rogowski coil types. Active energy accuracy is class 0.1s under IEC 62053-22 and class 0.1 under ANSI C12.20. Harmonics are resolved up to the 63rd on 50 or 60 Hz types. The standard RS485 port carries Modbus RTU and DNP 3.0. Optional modules add Ethernet with Modbus TCP, BACnet IP or MS/TP, Profibus DP, and IEC 61850 2nd edition. The meter analyzes power quality, covering harmonics, crest factors and unbalance. The IIW model also logs power quality events such as sags and swells. It is listed to IEC 61010-1, UL 61010-1, IEC 61557-12, IEC 60068-2, CE and RoHS, and it works with the AXM-WEB2 Ethernet module. The brochure states a five-year warranty.

<!-- review notes
- sentence 2: support check: partial - Voltage and 5A/1A options with 333mV are stated, but the '100mV Rope CT' is not explicitly Rogowski.
- sentence 4: support check: partial - Most protocols are stated, but 'optional' for the modules and IEC 61850 as a module are not explicit, though listed in the option table.
- sentence 6: support check: partial - Standards are listed, but 'listed' status and working with AXM-WEB2 are only implied by a manual title.
-->
