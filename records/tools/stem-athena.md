---
id: tool:stem-athena
type: Tool
name: Stem Athena
aliases:
- Athena Power Controller
- Athena Explorer
- Athena AI
- Athena Controller
- Athena Apps
category: Platforms
tool_kind: platform
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:stem
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-misc-collateral-the-stem-pa
    loc: sec=h7
    h: 7609af7ab4aa
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-stem-overview-booklet-c-i-9
    loc: sec=h8
    h: efba27388073
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-stem-overview-booklet-c-i-9-2
    loc: sec=h7
    h: 8747d55069e6
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:ethernet
  note: The Athena Power Controller links to the Stem CommLink over TCP-IP/Ethernet with PoE.
  cite:
  - src: src:eq-equip-bess-stem-metering-procurement-guidance
    loc: tbl=3.r10
    h: f1382e3eb9ee
  - src: src:eq-equip-bess-stem-metering-procurement-guidance
    loc: tbl=3.r9
    h: 5b7bb9e3bfd4
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:tcp-ip
  note: The Athena Power Controller links to the Stem CommLink over TCP-IP/Ethernet with PoE.
  cite:
  - src: src:eq-equip-bess-stem-metering-procurement-guidance
    loc: tbl=3.r10
    h: f1382e3eb9ee
  - src: src:eq-equip-bess-stem-metering-procurement-guidance
    loc: tbl=3.r9
    h: 5b7bb9e3bfd4
  review: drafted
---
Stem Athena is Stem's artificial intelligence platform for energy storage, using big data and machine learning to time energy use and cut energy bills. Athena software optimizes storage operation both behind and in front of the meter, across several applications. It is delivered as Athena Apps, including Utility Bill Optimization, Export Optimization and Solar Self-Consumption apps, and which apps are available depends on the market and tariff. Athena can link facilities into virtual power plants that earn demand response revenue. On site, the Athena Power Controller is an industrial PC inside the Stem enclosure, and it talks to the Stem CommLink over TCP-IP/Ethernet with PoE. During Athena Setup, Stem configures and tests the Athena Apps that control the storage system through the Stem Edge Controller, and Stem experts verify performance before permission to operate. Stem certifies all of the storage hardware it supplies to run with Athena in control. Stem says it calibrated the Energy Toolbase simulation to match how Athena performs in the field, and every Athena App comes with a performance guarantee.

<!-- review notes
- sentence 3: support check: partial - Athena Apps, Utility Bill Optimization, Export Optimization, Solar Self-Consumption and availability by market are shown, but tariff dependence is only implied and the apps' delivery framing is not explicit.
-->
