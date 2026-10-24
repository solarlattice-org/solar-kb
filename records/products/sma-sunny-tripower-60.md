---
id: prod:sma-sunny-tripower-60
type: Product
name: Sunny Tripower 60
aliases:
- STP 60-10
- STP60
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:inverter
  cite:
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=50.r3
    h: 61d1755b5307
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=92.r3
    h: 9e10c32e65db
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=136.r3
    h: 5a5226cddfea
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=177.r3
    h: ce04b85ceb7a
  - src: src:sma-doc-278879
    loc: tbl=13.r5
    h: fc8424477a27
  - src: src:sma-doc-278879
    loc: tbl=75.r5
    h: 164b81071807
  review: drafted
- claim_id: c2
  rel: compatible_with
  target: prod:sma-inverter-manager
  note: Inverter Manager appears in the Spanish wiring overview for the Sunny Tripower 60 / Sunny Highpower
    75 system.
  cite:
  - src: src:sma-doc-278879
    loc: tbl=56
    h: db4d9471118b
  review: drafted
  review_note: 'support check: partial - Inverter Manager appears in the wiring overview with the Sunny
    Tripower 60, but the passage doesn''t explicitly state compatibility, and it is listed as ''Inverter
    Manager'' not explicitly SMA product.'
---
The Sunny Tripower 60, type designation STP 60-10, is an SMA inverter product. It shares its documentation with the Sunny Highpower PEAK1 (SHP 75-10), including the installation guide and a description of the operating parameters. SMA documents describe the Sunny Tripower 60, the Sunny Highpower Peak1 and the Sunny Tripower Storage 60 together and simply call them the inverter. The SMA wiring overview for the system shows the inverter alongside a PC running the LCS-Tool and a router, plus an optional SunSpec Alliance compatible weather station and an optional I/O Box. One version of that wiring overview also shows an SMA Inverter Manager in the system.

<!-- review notes
- sentence 1: support check: partial - STP 60-10 is the Sunny Tripower 60 and it is an inverter, but the passages don't explicitly say it is an SMA product (SMA brand not stated in them).
- sentence 2: support check: partial - Shared documents with SHP 75-10 and an operating parameters description are shown, but an installation guide is not explicitly identified.
-->
