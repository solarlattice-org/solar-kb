---
id: prod:generac-pwrcell-battery
type: Product
name: Generac PWRcell Battery
aliases:
- PWRcell battery cabinet
category: Storage
make: generac
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:generac
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: sec=h9
    h: aceb56075bc5
  review: drafted
  review_note: 'support check: partial - Passage names it the Generac PWRcell Battery and refers to ''the
    manufacturer'' but doesn''t explicitly say Generac makes it, though the brand name implies it.'
- claim_id: c2
  rel: instance_of
  target: comp:battery-storage
  note: Described as the storage component of the PWRcell system.
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: sec=h48
    h: cf1354850431
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:generac-pwrcell-inverter
  note: Connects directly to the PWRcell Inverter over REbus DC lines.
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: sec=h48
    h: cf1354850431
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: sec=h9
    h: aceb56075bc5
  review: drafted
  review_note: 'support check: partial - Connects directly to the PWRcell Inverter over REbus DC lines
    is stated, but the specific model numbers aren''t.'
- claim_id: c4
  rel: compatible_with
  target: prod:generac-pv-link
  note: Works with PV Links on the REbus DC nanogrid.
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: sec=h48
    h: cf1354850431
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: arch:dc-coupled-storage
  scope:
    applications:
    - on-grid
  note: Battery, PV Links and inverter share REbus DC lines for grid-tied solar-plus-storage.
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: sec=h48
    h: cf1354850431
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:rebus
  note: Listed as the communication protocol for PWRcell M3 to M6.
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=6.r16
    h: 7baf74e85e25
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: sec=h48
    h: cf1354850431
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:rs485
  note: Listed as the communication interface of the DCB and EX battery modules.
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=7.r16
    h: 6cfc2b6a7bcc
  review: drafted
- claim_id: c8
  rel: implements
  target: func:self-consumption-optimization
  scope:
    applications:
    - self-consumption
  note: Called Self Supply in the source.
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: sec=h48
    h: cf1354850431
  review: drafted
- claim_id: c9
  rel: implements
  target: func:time-of-use-optimization
  note: Called Rate Arbitrage in the source.
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: sec=h48
    h: cf1354850431
  review: drafted
- claim_id: c10
  rel: implements
  target: func:backup-power
  scope:
    applications:
    - backup
  note: Called Clean Backup Power in the source.
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: sec=h48
    h: cf1354850431
  review: drafted
- claim_id: c11
  attr: efficiency
  value:
    nominal: 96.5
    unit: unit:PERCENT
  conditions: Round-trip efficiency, DC to DC, PWRcell M3, M4, M5 and M6
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=6.r18
    h: 278345a77b6c
  review: drafted
- claim_id: c12
  attr: rated_power
  value:
    nominal: 3.4
    unit: unit:KiloW
  conditions: Nominal continuous power, PWRcell M3
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=6.r4
    h: 27fe5baa4a3c
  review: drafted
  review_note: possible conflict with c13 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions)
- claim_id: c13
  attr: rated_power
  value:
    nominal: 4.5
    unit: unit:KiloW
  conditions: Nominal continuous power, PWRcell M4
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=6.r4
    h: 27fe5baa4a3c
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions)
- claim_id: c14
  attr: rated_power
  value:
    nominal: 5.6
    unit: unit:KiloW
  conditions: Nominal continuous power, PWRcell M5
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=6.r4
    h: 27fe5baa4a3c
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions); possible conflict with c15 (same source; check the conditions)
- claim_id: c15
  attr: rated_power
  value:
    nominal: 6.7
    unit: unit:KiloW
  conditions: Nominal continuous power, PWRcell M6
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=6.r4
    h: 27fe5baa4a3c
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions); possible conflict with c14 (same source; check the conditions)
- claim_id: c16
  attr: rated_output_current
  value:
    nominal: 11.6
    unit: unit:A
  conditions: Nominal continuous DC current, charge or discharge, PWRcell M3
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=6.r6
    h: 5ff4043f2915
  review: drafted
  review_note: possible conflict with c17 (same source; check the conditions); possible conflict with
    c18 (same source; check the conditions); possible conflict with c19 (same source; check the conditions)
- claim_id: c17
  attr: rated_output_current
  value:
    nominal: 15.5
    unit: unit:A
  conditions: Nominal continuous DC current, charge or discharge, PWRcell M4
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=6.r6
    h: 5ff4043f2915
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c18 (same source; check the conditions); possible conflict with c19 (same source; check the conditions)
- claim_id: c18
  attr: rated_output_current
  value:
    nominal: 19.4
    unit: unit:A
  conditions: Nominal continuous DC current, charge or discharge, PWRcell M5
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=6.r6
    h: 5ff4043f2915
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions); possible conflict with c19 (same source; check the conditions)
- claim_id: c19
  attr: rated_output_current
  value:
    nominal: 23.3
    unit: unit:A
  conditions: Nominal continuous DC current, charge or discharge, PWRcell M6
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=6.r6
    h: 5ff4043f2915
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions); possible conflict with c18 (same source; check the conditions)
- claim_id: c20
  attr: nominal_voltage
  value:
    nominal: 380
    unit: unit:V
  conditions: REbus DC nanogrid voltage used by all PWRcell products
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: sec=h48
    h: cf1354850431
  review: drafted
  review_note: 'review: partial - The passage gives 380 VDC as the REbus nanogrid voltage that all PWRcell
    products use, which matches the stated condition, but it never gives this as the battery''s own nominal
    voltage.'
---
The Generac PWRcell Battery is the storage part of the PWRcell system. It is a cabinet that holds compatible lithium ion battery modules. It connects directly to the PWRcell Inverter and to PV Links over the REbus DC nanogrid, which runs at 380 VDC and allows plug-and-play setup. It is meant for grid-connected solar applications: self supply, rate arbitrage and clean backup power. Nominal continuous power goes from 3.4 kW for the M3 to 6.7 kW for the M6, and nominal continuous DC current goes from 11.6 A to 23.3 A. DC-to-DC round-trip efficiency is 96.5 percent for every size from M3 to M6. The internal control electronics are preprogrammed for safe charging and discharging. They monitor system voltage, system current, cell voltage and cell temperature, and the modules communicate over RS-485.

<!-- review notes
- sentence 1: support check: partial - Storage component and houses lithium ion modules are stated; 'cabinet' is not explicitly stated.
-->
