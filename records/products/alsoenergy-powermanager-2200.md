---
id: prod:alsoenergy-powermanager-2200
type: Product
name: AlsoEnergy PowerManager 2200
aliases:
- PowerManager 2200
- CH-E0-2200
category: Monitoring and communications
make: alsoenergy
product_level: family
claims:
- claim_id: c1
  rel: uses_protocol
  target: proto:ethernet
  note: The MC-1111/1112 hardware has 2 auto-sensing 10/100/1000 Mbps RJ45 ports. The MC-1121/1122 hardware
    has 4.
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-ch-e0-2200-powermanager-2200-2020-06-10
    loc: tbl=2.r18
    h: cc2addf13b44
  review: drafted
  review_note: 'support check: partial - Evidence shows Ethernet ports with counts per series, but doesn''t
    mention PowerManager 2200 by name; core claim is stated.'
- claim_id: c2
  rel: uses_protocol
  target: proto:rs485
  note: Serial port has automatic data direction control (ADDC) for RS-485. Flow control options are RTS/CTS
    and XON/XOFF.
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-ch-e0-2200-powermanager-2200-2020-06-10
    loc: tbl=2.r18
    h: cc2addf13b44
  review: drafted
  review_note: 'support check: partial - Evidence mentions ADDC for RS-485 and RTS/CTS, XON/XOFF, but
    the serial port and product link are only implied by the garbled row.'
---
The cut sheet lists the MC-1111, MC-1121 and MC-1122 hardware versions. The MC-1111/1112 versions have two gigabit-capable RJ45 Ethernet ports, and the MC-1121/1122 versions have four. The serial interface supports RS-485 with automatic data direction control, plus RTS/CTS and XON/XOFF flow control.

<!-- review notes
- sentence 1: support check: partial - Evidence only shows the model labels, with no statement that a cut sheet lists them as hardware versions; MC-1112 also not listed separately.
- sentence 1: review: partial - The cut sheet shows MC-1111, MC-1121 and MC-1122 only as bare section headings, so nothing in the passages says they are hardware versions.
-->
