---
id: prod:sma-hybrid-controller
type: Product
name: SMA Hybrid Controller
aliases:
- Hybrid Controller
- Hybrid Controller XL 1xGMP 1A
- Hybrid Controller XL 1xGMP 5A
category: Monitoring and communications
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-doc-275752
    loc: tbl=5.r3
    h: b617c16ab9e5
  - src: src:sma-doc-275752
    loc: tbl=5
    h: 3e3dbf17d562
  review: drafted
  review_note: 'support check: partial - Passages show the SMA-prefixed designation, but don''t explicitly
    state the manufacturer; it is only implied by the name.'
- claim_id: c2
  rel: instance_of
  target: comp:programmable-logic-controller
  cite:
  - src: src:sma-doc-275752
    loc: tbl=5.r3
    h: b617c16ab9e5
  - src: src:sma-doc-275752
    loc: tbl=5
    h: 3e3dbf17d562
  review: drafted
- claim_id: c3
  rel: part_of
  target: prod:sma-power-plant-manager
  note: Listed as an optional component in the Power Plant Manager technical data and documentation.
  cite:
  - src: src:sma-doc-275752
    loc: tbl=5
    h: 3e3dbf17d562
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2.r2
    h: 56f3a8c2f76c
  review: drafted
- claim_id: c4
  rel: implements
  target: func:closed-loop-plant-control
  note: Provides advanced open-loop and closed-loop control functions.
  cite:
  - src: src:sma-doc-275752
    loc: tbl=44.r22
    h: c9287f03dfa6
  review: drafted
  review_note: 'support check: partial - Advanced open-loop and closed-loop control functions are attributed
    to the Hybrid Controller, but ''closed-loop plant control'' is only loosely matched.'
- claim_id: c5
  rel: uses_protocol
  target: proto:canopen
  note: Used to communicate with genset controllers.
  cite:
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2.r8
    h: 052855ff2dab
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:dnp3
  note: Listed as IEEE 1815 (DNP3).
  cite:
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2.r6
    h: 2d04d85263cd
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:modbus-tcp
  note: Acts as Modbus TCP master over Ethernet (100BASE-FX and TX).
  cite:
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2.r7
    h: 04e6ac63962d
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:ethernet
  note: 100BASE-FX and 100BASE-TX.
  cite:
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2.r7
    h: 04e6ac63962d
  review: drafted
- claim_id: c9
  rel: compatible_with
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2.r13
    h: 60b27eba1709
  review: drafted
- claim_id: c10
  rel: compatible_with
  target: prod:sma-sunny-central-storage
  cite:
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2.r13
    h: 60b27eba1709
  review: drafted
- claim_id: c11
  rel: compatible_with
  target: prod:janitza-umg-604
  note: Compatible external power measurement device.
  cite:
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2.r10
    h: 17269655c100
  review: drafted
---
The SMA Hybrid Controller is a programmable logic controller made by SMA and offered as an optional part of the SMA Power Plant Manager. It provides advanced open-loop and closed-loop plant control functions, and the datasheet lists the PV system size it can handle as unlimited. It talks to genset controllers over CANopen, supports DNP3 (IEEE 1815), and acts as a Modbus TCP master over Ethernet. Compatible inverters include the Sunny Central CP-XT and Sunny Central Storage, and the Janitza UMG 604 is listed as a compatible external power meter. An optional router allows remote access and VPN. XL variants with high-precision current and voltage measurement exist in 1 A and 5 A versions.

<!-- review notes
- sentence 1: support check: partial - PLC and optional status are supported, but 'made by SMA' is only implied by the name.
-->
