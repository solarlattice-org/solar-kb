---
id: prod:byd-battery-box-premium-hv
type: Product
name: BYD Battery-Box Premium HVS/HVM
aliases:
- Battery-Box HVS
- Battery-Box HVM
- Battery-Box Premium
- Battery-Box Premium HVS
- Battery-Box Premium HVM
category: Storage
make: byd
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:byd
  note: Listed as BYD Company Limited.
  cite:
  - src: src:sma-doc-278870
    loc: tbl=2.r2
    h: 83f71d4e8d8f
  - src: src:sma-doc-275666
    loc: tbl=7.r4
    h: 96dde07e9b50
  - src: src:sma-doc-278870
    loc: tbl=4
    h: 0427f923eb22
  - src: src:sma-doc-278870
    loc: tbl=2.r3
    h: 3f7781df6006
  review: drafted
- claim_id: c2
  rel: compatible_with
  target: prod:sma-sunny-boy-storage
  scope:
    firmware_min: 3.11.03.R
  conditions: HVM 8.3-22.1 with 3 to 8 modules; battery BMU 3.13 or later and BMS 3.19 or later; firmware_min
    refers to the inverter
  cite:
  - src: src:sma-doc-275666
    loc: tbl=7.r4
    h: 96dde07e9b50
  review: drafted
  review_note: 'support check: partial - Row is in passages, but the passage doesn''t name Sunny Boy Storage
    as the inverter explicitly (only inverter firmware).'
- claim_id: c3
  rel: compatible_with
  target: prod:sma-sunny-boy-storage
  scope:
    firmware_min: 3.11.10.R
  conditions: HVS 5.1-10.2 with 2 to 4 modules; battery BMU 3.13 or later and BMS 3.19 or later; firmware_min
    refers to the inverter
  cite:
  - src: src:sma-doc-275666
    loc: tbl=7.r3
    h: cdc7876631c8
  review: drafted
  review_note: 'support check: partial - Row matches the numbers, but the passage doesn''t name Sunny
    Boy Storage explicitly.'
- claim_id: c4
  rel: compatible_with
  target: prod:sma-sunny-boy-storage
  scope:
    firmware_min: 3.11.06.R
  conditions: HVS 5.1-10.2 with 2 to 4 modules; battery BMU 3.13 or later and BMS 3.19 or later; firmware_min
    refers to the inverter
  cite:
  - src: src:sma-doc-275666
    loc: tbl=1.r2
    h: 292835b9cbbe
  review: drafted
  review_note: 'support check: partial - Row matches the numbers, but the passage doesn''t name Sunny
    Boy Storage explicitly.'
- claim_id: c5
  rel: compatible_with
  target: prod:sma-sunny-boy-storage
  conditions: Cabling plans exist for SBS3.7/5.0/6.0-10 with HVS and HVM and for SBS2.5-1VL-10 with HVS;
    with SBS 2.5 the Sunny Boy Storage 2.5 inverter must be selected during configuration
  cite:
  - src: src:sma-doc-275666
    loc: sec=2.4.6
    h: 95b181a54b8d
  - src: src:sma-doc-275666
    loc: sec=1.3.4
    h: 04e1de1a80ad
  - src: src:sma-doc-275666
    loc: sec=h6
    h: 72a6b6306644
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:sma-sunny-tripower-smart-energy
  scope:
    firmware_min: 1.00.00.R
  conditions: HVM 11.0-22.1 and HVS 5.1-12.8; battery firmware BMU 3.16 and BMS 3.24; firmware_min refers
    to the inverter
  cite:
  - src: src:sma-doc-278870
    loc: tbl=2.r2
    h: 83f71d4e8d8f
  - src: src:sma-doc-278870
    loc: tbl=2.r3
    h: 3f7781df6006
  - src: src:sma-doc-278870
    loc: sec=h28
    h: 48e2a9314c21
  review: drafted
  review_note: 'support check: partial - Battery/inverter firmware values match, but the passages don''t
    name Sunny Tripower Smart Energy for the u3/u6 rows (only the u16 cabling plan does).'
- claim_id: c7
  rel: compatible_with
  target: prod:sma-sunny-tripower-smart-energy
  scope:
    firmware_min: 3.04.16.R
  conditions: Parallel operation mode with up to 3 battery units; battery firmware BMU 3.16 and BMS 3.24;
    firmware_min refers to the inverter
  cite:
  - src: src:sma-doc-278870
    loc: tbl=4
    h: 0427f923eb22
  review: drafted
  review_note: 'support check: partial - Parallel-mode firmware and ≤3 units match, but the passages don''t
    name Sunny Tripower Smart Energy for that table.; review: partial - The table supports parallel mode
    with up to 3 units, BMU 3.16 / BMS 3.24 and inverter firmware 3.04.16.R or later, but the quoted passage
    does not name Sunny Tripower Smart Energy.'
- claim_id: c8
  rel: incompatible_with
  target: prod:sma-sunny-tripower-smart-energy
  scope:
    firmware_min: 3.04.16.R
    firmware_max: 3.04.16.R
  conditions: Three HVM 16.6 batteries in one pack with BYD Combiner Box after BYD battery firmware 3.22
  note: 'Inverter stops charging and discharging and shows event 6462, because it can only process discharge
    current values up to 128 A while three batteries can supply up to 150 A. Workaround: use at most two
    batteries until a corrected inverter firmware is released.'
  cite:
  - src: src:sma-kb-sunny-tripower-smart-energy-stpxx-3se-40-no-charging-discharging-when-three-byd-bat
    loc: sec=h1
    h: dff3fe8005e3
  review: drafted
  review_note: 'support check: partial - The article supports the issue, event 6462, 128 A vs 150 A and
    workaround, but it describes it as an inverter firmware limitation rather than the pair being incompatible;
    the max-firmware bound isn''t stated.'
- claim_id: c9
  rel: uses_protocol
  target: proto:can-bus
  conditions: CAN L and CAN H on twisted pair conductors, at least CAT5e, to the Sunny Boy Storage
  cite:
  - src: src:sma-doc-275666
    loc: tbl=17
    h: bbdccfb7b51c
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: 'support check: partial - The passage shows CAN L/H as twisted pair at least CAT5e for
    the SBS cabling plan, but doesn''t explicitly say the battery uses CAN bus.'
- claim_id: c10
  attr: max_count
  value:
    max: 3
    unit: unit:NUM
  conditions: Battery units in parallel operation mode with Sunny Tripower Smart Energy
  cite:
  - src: src:sma-doc-278870
    loc: tbl=4
    h: 0427f923eb22
  review: drafted
  review_note: 'support check: partial - The ≤3 parallel units is stated, but the passage doesn''t name
    Sunny Tripower Smart Energy.'
- claim_id: c11
  attr: max_count
  value:
    min: 3
    max: 8
    unit: unit:NUM
  conditions: Modules per HVM 8.3-22.1 battery with Sunny Boy Storage
  cite:
  - src: src:sma-doc-275666
    loc: tbl=7.r4
    h: 96dde07e9b50
  review: drafted
  review_note: 'support check: partial - Modules 3-8 for HVM 8.3-22.1 are stated; Sunny Boy Storage isn''t
    named and the number is a module range, not a maximum count.'
- claim_id: c12
  attr: max_count
  value:
    min: 2
    max: 4
    unit: unit:NUM
  conditions: Modules per HVS 5.1-10.2 battery with Sunny Boy Storage
  cite:
  - src: src:sma-doc-275666
    loc: tbl=7.r3
    h: cdc7876631c8
  - src: src:sma-doc-275666
    loc: tbl=1.r2
    h: 292835b9cbbe
  review: drafted
  review_note: 'support check: partial - Modules 2-4 for HVS 5.1-10.2 are stated; Sunny Boy Storage isn''t
    named and the number is a module range, not a maximum count.; review: partial - Both rows state 2-4
    modules for HVS 5.1-10.2, but they give a range rather than a maximum of 2-4, and neither passage
    names Sunny Boy Storage.'
- claim_id: c13
  attr: rated_output_current
  value:
    max: 25
    unit: unit:A
  conditions: HVS models; battery current limit in SMA backup planning table
  cite:
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=23
    h: c197afd6ed49
  review: drafted
- claim_id: c14
  attr: rated_output_current
  value:
    max: 50
    unit: unit:A
  conditions: HVM models; battery current limit in SMA backup planning table
  cite:
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=23
    h: c197afd6ed49
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=23.r8
    h: 574d5c83bc1f
  review: drafted
- claim_id: c15
  attr: rated_output_current
  value:
    max: 50
    unit: unit:A
  conditions: Discharge current limit per battery after BYD battery firmware update 3.22 (previously 40
    A)
  cite:
  - src: src:sma-kb-sunny-tripower-smart-energy-stpxx-3se-40-no-charging-discharging-when-three-byd-bat
    loc: sec=h1
    h: dff3fe8005e3
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c16
  attr: nominal_voltage
  value:
    min: 160
    max: 230
    unit: unit:V
  conditions: Battery voltage range, HVS 5.1
  cite:
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=23
    h: c197afd6ed49
  review: drafted
  review_note: 'support check: partial - The 160-230 V range is stated for HVS 5.1, but it is a battery
    voltage range, not a nominal voltage.; possible conflict with c17 (same source; check the conditions);
    possible conflict with c19 (same source; check the conditions)'
- claim_id: c17
  attr: nominal_voltage
  value:
    min: 400
    max: 576
    unit: unit:V
  conditions: Battery voltage range, HVS 12.8
  cite:
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=23
    h: c197afd6ed49
  review: drafted
  review_note: 'support check: partial - The 400-576 V range is stated for HVS 12.8, but it is a battery
    voltage range, not a nominal voltage.; possible conflict with c16 (same source; check the conditions);
    possible conflict with c18 (same source; check the conditions)'
- claim_id: c18
  attr: nominal_voltage
  value:
    min: 120
    max: 180
    unit: unit:V
  conditions: Battery voltage range, HVM 8.3
  cite:
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=23
    h: c197afd6ed49
  review: drafted
  review_note: 'support check: partial - The 120-180 V range is stated for HVM 8.3, but it is a battery
    voltage range, not a nominal voltage.; possible conflict with c17 (same source; check the conditions);
    possible conflict with c19 (same source; check the conditions)'
- claim_id: c19
  attr: nominal_voltage
  value:
    min: 320
    max: 480
    unit: unit:V
  conditions: Battery voltage range, HVM 22.1
  cite:
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=23
    h: c197afd6ed49
  review: drafted
  review_note: 'support check: partial - The 320-480 V range is stated for HVM 22.1, but it is a battery
    voltage range, not a nominal voltage.; possible conflict with c16 (same source; check the conditions);
    possible conflict with c18 (same source; check the conditions)'
---
The BYD Battery-Box Premium HVS and HVM is a family of high-voltage battery storage systems made by BYD Company Limited. It is approved for SMA Sunny Boy Storage and Sunny Tripower Smart Energy inverters, with minimum firmware versions for both the battery (BMU and BMS) and the inverter. The battery talks to the inverter over CAN, wired as a twisted pair of at least CAT5e quality. With Sunny Boy Storage, HVM batteries take 3 to 8 modules and HVS batteries take 2 to 4 modules. With Sunny Tripower Smart Energy, up to 3 units can run in parallel. In SMA backup planning, battery current is limited to 25 A for HVS and 50 A for HVM. The HVM 8.3 is listed as not compatible there because its voltage is outside the range. Known issue: after BYD battery firmware 3.22, a Sunny Tripower Smart Energy on firmware 3.04.16.R stops charging and discharging a three-battery HVM 16.6 pack and shows event 6462. The workaround is to use only two batteries until SMA releases a firmware fix.

<!-- review notes
- sentence 1: support check: partial - The passages show HVS and HVM from BYD Company Limited, but not that they are high-voltage storage systems.
- sentence 2: support check: partial - Minimum battery and inverter firmware are given, but the u3/u6 rows list BMU = 3.16 exact, and the passages don't name the inverters or the word 'approved'.
- sentence 3: support check: partial - CAN L/H on twisted pair of at least CAT5e is shown, but only for the SBS cabling plan.
- sentence 4: support check: partial - The module ranges and ≤3 parallel units are stated, but the inverter names are not in the passages.
- sentence 1: review: partial - The rows name Battery-Box Premium HVS and HVM by BYD Company Limited, but nothing calls them high-voltage storage systems.
- sentence 4: review: partial - The module ranges (HVM 3-8, HVS 2-4) and up to 3 parallel units are in the tables, but the passages never name Sunny Boy Storage or Sunny Tripower Smart Energy.
-->
