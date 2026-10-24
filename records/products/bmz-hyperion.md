---
id: prod:bmz-hyperion
type: Product
name: BMZ Hyperion
aliases:
- ESS-Z
- BMZ ESS
- Hyperion 7.5-15
- Hyperion 7.5-15 (SE)
category: Storage
make: bmz
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:bmz
  note: Listed as BMZ GmbH
  cite:
  - src: src:sma-doc-275666
    loc: tbl=6.r3
    h: 8e572757de37
  - src: src:sma-doc-278870
    loc: tbl=2.r8
    h: 470dba3875a0
  - src: src:sma-doc-275666
    loc: tbl=6.r4
    h: 75831bb734ba
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:battery-storage
  note: Modular lithium-ion high-voltage battery
  cite:
  - src: src:sma-kb-sunny-boy-storage-sbs-3-7-6-0-battery-compatibility-bmz-hyperion-ibc-era-powerbase
    loc: sec=h1
    h: 7186352d94de
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:sma-sunny-boy-storage
  scope:
    products:
    - prod:sma-sunny-boy-storage
    valid_from: '2020-08-01'
  conditions: Sunny Boy Storage 3.7-6.0; compatible since August 2020; new Helios VE module generation
    requires inverter firmware 3.12.26.R or later
  cite:
  - src: src:sma-kb-sunny-boy-storage-sbs-3-7-6-0-battery-compatibility-bmz-hyperion-ibc-era-powerbase
    loc: sec=h1
    h: 7186352d94de
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: prod:sma-sunny-boy-storage
  conditions: Hyperion 7.5-15 item 41871 with Helios 1.5 modules, 3 to 6 modules; battery firmware 0.03.07.R
    or later; inverter firmware 3.11.10.R or later
  cite:
  - src: src:sma-doc-275666
    loc: tbl=6.r3
    h: 8e572757de37
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: prod:sma-sunny-boy-storage
  conditions: Hyperion 7.5-15 (SE) items 615424 and 616038 with Helios VE modules, 3 to 6 modules; battery
    firmware 0.03.15.R or later; inverter firmware 3.12.61.R or later
  cite:
  - src: src:sma-doc-275666
    loc: tbl=6.r4
    h: 75831bb734ba
  review: drafted
- claim_id: c6
  attr: energy_capacity
  value:
    nominal: 2.5
    unit: unit:KiloW-HR
  conditions: Per battery module (Helios 1.5)
  cite:
  - src: src:sma-kb-sunny-boy-storage-sbs-3-7-6-0-battery-compatibility-bmz-hyperion-ibc-era-powerbase
    loc: sec=h1
    h: 7186352d94de
  review: drafted
  review_note: possible conflict with c7 (same source; check the conditions)
- claim_id: c7
  attr: energy_capacity
  value:
    min: 7.5
    max: 15
    unit: unit:KiloW-HR
  conditions: Complete system built from 3 to 6 modules
  cite:
  - src: src:sma-kb-sunny-boy-storage-sbs-3-7-6-0-battery-compatibility-bmz-hyperion-ibc-era-powerbase
    loc: sec=h1
    h: 7186352d94de
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions)
- claim_id: c8
  attr: max_count
  value:
    min: 3
    max: 6
    unit: unit:NUM
  conditions: Battery modules per system with Sunny Boy Storage
  cite:
  - src: src:sma-doc-275666
    loc: tbl=6.r3
    h: 8e572757de37
  - src: src:sma-kb-sunny-boy-storage-sbs-3-7-6-0-battery-compatibility-bmz-hyperion-ibc-era-powerbase
    loc: sec=h1
    h: 7186352d94de
  - src: src:sma-doc-275666
    loc: tbl=6.r4
    h: 75831bb734ba
  review: drafted
---
BMZ Hyperion is a modular high-voltage lithium-ion home battery made by BMZ GmbH. A system uses 3 to 6 battery modules of 2.5 kWh each, which gives 7.5 to 15 kWh in total. SMA has listed it as compatible with the Sunny Boy Storage 3.7-6.0 since August 2020, and a cabling plan is provided for the SBS3.7-10, SBS5.0-10 and SBS6.0-10. From September 2021 the older Helios 1.5 modules were replaced by Helios VE modules, and the only way to tell the two generations apart is the item number. Helios VE modules need Sunny Boy Storage firmware 3.12.26.R or later, and the inverter updates the battery's BMS firmware automatically. Hyperion 10.0, 12.5 and 15.0 with Helios VE modules also work with the Sunny Tripower Smart Energy, using the communication cable supplied by the battery manufacturer.

<!-- review notes
- sentence 4: support check: partial - Conversion to Helios VE since September 2021 and item-number distinction are stated, but 'replaced' is slightly stronger than 'converting'.
- sentence 6: support check: partial - Table row for Hyperion 10.0/12.5/15.0 with Helios VE and the Sunny Tripower Smart Energy figure with manufacturer's cable are present, but the row doesn't name the inverter explicitly and compatibility with STP SE is implied.
-->
