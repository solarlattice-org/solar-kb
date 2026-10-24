---
id: prod:axitec-axistorage
type: Product
name: AXITEC AXIstorage Li
aliases:
- AXIstorage
- AXIstorage Li SH
- AXIStorage Li 8S
category: Storage
make: axitec
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:axitec
  cite:
  - src: src:sma-doc-278870
    loc: tbl=2.r10
    h: a87a195d5f7b
  - src: src:sma-doc-275666
    loc: tbl=6.r1
    h: bf6baa905b27
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:battery-storage
  note: Lithium-ion high-voltage modular battery
  cite:
  - src: src:sma-kb-sunny-boy-storage-sbs-3-7-6-0-battery-compatibility-bmz-hyperion-ibc-era-powerbase
    loc: sec=h1
    h: 7186352d94de
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:sma-sunny-boy-storage
  scope:
    firmware_min: 3.12.26.R
  conditions: AXIstorage Li SH with new Helios VE modules (since September 2021); requires inverter firmware
    3.12.26.R or later
  cite:
  - src: src:sma-kb-sunny-boy-storage-sbs-3-7-6-0-battery-compatibility-bmz-hyperion-ibc-era-powerbase
    loc: sec=h1
    h: 7186352d94de
  review: drafted
- claim_id: c4
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
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c5
  attr: energy_capacity
  value:
    min: 7.5
    max: 15
    unit: unit:KiloW-HR
  conditions: Per system, built from 3 to 6 modules
  cite:
  - src: src:sma-kb-sunny-boy-storage-sbs-3-7-6-0-battery-compatibility-bmz-hyperion-ibc-era-powerbase
    loc: sec=h1
    h: 7186352d94de
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c6
  attr: max_count
  value:
    min: 3
    max: 6
    unit: unit:NUM
  conditions: Battery modules per AXIstorage Li SH system
  cite:
  - src: src:sma-kb-sunny-boy-storage-sbs-3-7-6-0-battery-compatibility-bmz-hyperion-ibc-era-powerbase
    loc: sec=h1
    h: 7186352d94de
  - src: src:sma-doc-275666
    loc: tbl=6.r1
    h: bf6baa905b27
  review: drafted
---
AXITEC AXIstorage Li is a modular lithium-ion high-voltage battery family, with the SH version used with SMA storage inverters. An SH system holds 3 to 6 battery modules of 2.5 kWh each, giving 7.5 to 15 kWh per system. The Sunny Boy Storage 3.7-6.0 has supported it since August 2020. The newer Helios VE module generation needs inverter firmware 3.12.26.R or later. You can only tell the older Helios 1.5 modules from the newer Helios VE modules by the system item number. The Sunny Boy Storage updates the battery management system firmware automatically, so check that the inverter firmware is current. The AXIstorage Li 8S version is listed for use with Sunny Island 6.0H and 8.0H inverters, and with the SI 6048US in split-phase systems.

<!-- review notes
- sentence 6: support check: partial - Evidence shows 8S with SI 6.0H, 8.0H and SI 6048US split-phase, but the 'listed' and 'Sunny Island' naming plus ≥ tower counts are only implied.
-->
