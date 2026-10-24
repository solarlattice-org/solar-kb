---
id: prod:byd-battery-box-lv
type: Product
name: BYD Battery-Box LV
aliases:
- Battery-Box LVS
- Battery-Box LVL
- B-Box
- Battery-Box Premium LVS
- LV Flex
- LV Flex Lite
- LVL 15.4
category: Storage
make: byd
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:byd
  cite:
  - src: src:sma-doc-278303
    loc: sec=h53
    h: 9c3c0c8338ee
  - src: src:sma-doc-278303
    loc: sec=h55
    h: 0059247fe9f6
  review: drafted
  review_note: 'support check: partial - Passages only name the products (Premium LVS, LV Flex) without
    stating BYD as maker explicitly beyond the ''BYD'' name in titles; roughly supported by names but
    no explicit manufacturer statement.'
- claim_id: c2
  rel: compatible_with
  target: arch:off-grid-system
  scope:
    applications:
    - backup
    - off-grid
  conditions: B-BOX as of firmware version 2.7; LV Flex and LV Flex Lite as of BMU firmware V1.22 or later
    and BMS firmware V1.13 or later; single-phase, split-phase, three-phase and double split-phase systems
  cite:
  - src: src:sma-doc-278303
    loc: tbl=11
    h: 1d3a226e72be
  review: drafted
---
The BYD Battery-Box LV is BYD's family of low-voltage battery storage. SMA documentation lists it under the variants Battery-Box Premium LVS, B-BOX, LV Flex and LV Flex Lite. SMA lists it with the Sunny Island SI 6.0H and SI 8.0H for self-consumption. Each configuration needs a minimum number of battery modules and towers. Battery backup and off-grid setups with the Sunny Island need at least four battery modules, and some configurations need two towers. The B-BOX is approved for battery backup and off-grid systems in single-phase, split-phase, three-phase and double split-phase layouts from firmware version 2.7. LV Flex and LV Flex Lite need BMU firmware V1.22 or later and BMS firmware V1.13 or later for those same system types.

<!-- review notes
- sentence 1: support check: partial - Variants Premium LVS, B-BOX, LV Flex, LV Flex Lite appear, but nothing states it's BYD's low-voltage family or that SMA lists them under it.
- sentence 1: review: partial - The passages name the Premium LVS, B-BOX, LV Flex and LV Flex Lite variants, but nothing calls Battery-Box LV a BYD low-voltage family or says SMA groups these variants under that name.
-->
