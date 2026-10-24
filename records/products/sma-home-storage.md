---
id: prod:sma-home-storage
type: Product
name: SMA Home Storage
aliases:
- SMA Home Storage battery
- SMA Home Storage Module
category: Storage
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  note: Manufacturer listed as SMA Solar Technology AG.
  cite:
  - src: src:sma-doc-278870
    loc: tbl=2.r1
    h: 36d4b5ea5264
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:battery-storage
  cite:
  - src: src:sma-kb-welche-energiekapazit-ten-stehen-f-r-den-sma-home-storage-zur-verf-gung
    loc: sec=h1
    h: 8bb1a5b9fc66
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:sma-sunny-tripower-smart-energy
  note: Two to five battery modules can be used with this inverter.
  cite:
  - src: src:sma-kb-bietet-der-sma-home-storage-nachr-stm-glichkeiten
    loc: sec=h1
    h: fb10d5d13910
  - src: src:sma-kb-mit-welchen-wechselrichtern-ist-der-sma-home-storage-kompatibel
    loc: sec=h1
    h: 3ea3d9d26933
  - src: src:sma-kb-welche-energiekapazit-ten-stehen-f-r-den-sma-home-storage-zur-verf-gung
    loc: sec=h1
    h: 8bb1a5b9fc66
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: prod:sma-sunny-tripower-smart-energy
  scope:
    firmware_min: 1.01.16.R
  conditions: Battery firmware 1.01.16.R or later and inverter firmware 3.04.16.R or later, for SMA Home
    Storage 6.5 to 16.4.
  cite:
  - src: src:sma-doc-278870
    loc: tbl=2.r1
    h: 36d4b5ea5264
  review: drafted
  review_note: 'support check: partial - Firmware minimums are listed for SMA Home Storage 6.5-16.4, but
    the passage doesn''t explicitly tie them to the Sunny Tripower Smart Energy.'
- claim_id: c5
  rel: compatible_with
  target: prod:sma-sbse-us-50
  note: The units name the Sunny Boy Smart Energy hybrid inverter generally; one to four battery modules
    can be used.
  cite:
  - src: src:sma-kb-bietet-der-sma-home-storage-nachr-stm-glichkeiten
    loc: sec=h1
    h: fb10d5d13910
  - src: src:sma-kb-mit-welchen-wechselrichtern-ist-der-sma-home-storage-kompatibel
    loc: sec=h1
    h: 3ea3d9d26933
  - src: src:sma-kb-welche-energiekapazit-ten-stehen-f-r-den-sma-home-storage-zur-verf-gung
    loc: sec=h1
    h: 8bb1a5b9fc66
  review: drafted
  review_note: 'support check: partial - Compatibility with Sunny Boy Smart Energy and one to four modules
    are stated, but the specific US-50 variant is not mentioned.'
- claim_id: c6
  rel: implements
  target: func:black-start
  note: Black start is activated manually at the battery; the hybrid inverters start on their own at sunrise.
  cite:
  - src: src:sma-kb-bietet-der-sma-home-storage-eine-schwarzstartfunktion
    loc: sec=h1
    h: f7ce1b364f8f
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:can-bus
  note: Battery modules talk to each other over CAN bus; event 5161 reports a multimaster error when that
    bus is disturbed.
  cite:
  - src: src:sma-kb-ereignis-5161-a1-9347-mit-sma-home-storage
    loc: sec=h1
    h: 0423e7541e8f
  review: drafted
  review_note: 'support check: partial - Event 5161 reports a CAN bus multimaster communication disturbance,
    but the passage doesn''t explicitly say the modules talk to each other over CAN bus.'
- claim_id: c8
  rel: certified_to
  target: std:iec-62477
  scope:
    regions:
    - region:eu
  cite:
  - src: src:sma-kb-welche-zertifizierungen-hat-der-sma-home-storage
    loc: sec=h1
    h: 034a244a15c5
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:iec-62619
  scope:
    regions:
    - region:eu
  cite:
  - src: src:sma-kb-welche-zertifizierungen-hat-der-sma-home-storage
    loc: sec=h1
    h: 034a244a15c5
  review: drafted
- claim_id: c10
  rel: certified_to
  target: std:vde-ar-e-2510-50
  scope:
    regions:
    - region:eu
  cite:
  - src: src:sma-kb-welche-zertifizierungen-hat-der-sma-home-storage
    loc: sec=h1
    h: 034a244a15c5
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:un-38-3
  cite:
  - src: src:sma-kb-welche-zertifizierungen-hat-der-sma-home-storage
    loc: sec=h1
    h: 034a244a15c5
  review: drafted
- claim_id: c12
  attr: energy_capacity
  value:
    nominal: 3.28
    unit: unit:KiloW-HR
  conditions: Per battery module
  cite:
  - src: src:sma-kb-welche-energiekapazit-ten-stehen-f-r-den-sma-home-storage-zur-verf-gung
    loc: sec=h1
    h: 8bb1a5b9fc66
  - src: src:sma-doc-bms-rm-xx-10
    loc: tbl=25.r3
    h: d7dc22bc8ae7
  - src: src:sma-doc-bms-rm-xx-10
    loc: tbl=73.r3
    h: b414e036a18e
  review: drafted
  review_note: possible conflict with c13 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions);
    possible conflict with c16 (same source; check the conditions)
- claim_id: c13
  attr: energy_capacity
  value:
    nominal: 6.56
    unit: unit:KiloW-HR
  conditions: Two modules combined
  cite:
  - src: src:sma-kb-welche-energiekapazit-ten-stehen-f-r-den-sma-home-storage-zur-verf-gung
    loc: sec=h1
    h: 8bb1a5b9fc66
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions);
    possible conflict with c16 (same source; check the conditions)
- claim_id: c14
  attr: energy_capacity
  value:
    nominal: 9.84
    unit: unit:KiloW-HR
  conditions: Three modules combined
  cite:
  - src: src:sma-kb-welche-energiekapazit-ten-stehen-f-r-den-sma-home-storage-zur-verf-gung
    loc: sec=h1
    h: 8bb1a5b9fc66
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions); possible conflict with c15 (same source; check the conditions);
    possible conflict with c16 (same source; check the conditions)
- claim_id: c15
  attr: energy_capacity
  value:
    nominal: 13.12
    unit: unit:KiloW-HR
  conditions: Four modules combined
  cite:
  - src: src:sma-kb-welche-energiekapazit-ten-stehen-f-r-den-sma-home-storage-zur-verf-gung
    loc: sec=h1
    h: 8bb1a5b9fc66
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions); possible conflict with c14 (same source; check the conditions);
    possible conflict with c16 (same source; check the conditions)
- claim_id: c16
  attr: energy_capacity
  value:
    nominal: 16.4
    unit: unit:KiloW-HR
  conditions: Five modules combined
  cite:
  - src: src:sma-kb-welche-energiekapazit-ten-stehen-f-r-den-sma-home-storage-zur-verf-gung
    loc: sec=h1
    h: 8bb1a5b9fc66
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions); possible conflict with c14 (same source; check the conditions);
    possible conflict with c15 (same source; check the conditions)
- claim_id: c17
  attr: max_count
  value:
    min: 2
    max: 5
    unit: unit:NUM
  scope:
    products:
    - prod:sma-sunny-tripower-smart-energy
  conditions: Battery modules per system with a Sunny Tripower Smart Energy
  cite:
  - src: src:sma-kb-welche-energiekapazit-ten-stehen-f-r-den-sma-home-storage-zur-verf-gung
    loc: sec=h1
    h: 8bb1a5b9fc66
  review: drafted
- claim_id: c18
  attr: warranty_term
  value:
    nominal: 12
    unit: unit:YR
  conditions: Performance warranty
  cite:
  - src: src:sma-kb-wie-lang-ist-die-garantie-f-r-den-sma-home-storage
    loc: sec=h1
    h: 4c1433858bba
  review: drafted
---
The SMA Home Storage is a modular battery system built for European markets. It is made up of stacked 3.28 kWh modules and can reach up to 16.4 kWh with five modules. It works only with the SMA Smart Energy hybrid inverters. The Sunny Boy Smart Energy takes one to four modules and the Sunny Tripower Smart Energy takes two to five. It cannot be retrofitted to Sunny Boy Storage inverters. It is certified to IEC 62477, IEC 62619, VDE 2510-50 and UN38.3. Black start is supported and is activated by hand at the battery. The standard warranty runs two years and grows to ten years if the product is registered within 30 days of commissioning. A separate performance warranty runs twelve years. Known battery events include cell undervoltage, communication faults between modules, CAN bus multimaster errors, mismatched module firmware, an open DC switch and short circuits. Each event is shown by a red LED pattern on the module. For communication faults, check the cabling between modules and make sure the termination resistor is fitted on the last module. If module firmware does not match, connect each module to the inverter on its own so it updates.

<!-- review notes
- sentence 1: support check: partial - Modular, European design, 3.28 kWh modules and up to 16.4 kWh with five modules are stated, but 'stacked' is not.
- sentence 7: support check: partial - All listed events appear, but the LED patterns differ and the short circuit event shows a continuous red LED rather than a pattern; the communication faults are also two separate events, and 'each event' is somewhat overgeneralized though broadly supported.
-->
