---
id: func:volt-watt
type: Function
name: Volt-Watt
aliases:
- voltage-active power mode
- P(U)
- P(V)
- DVWC
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  attr: setting_range
  value:
    min: 240
    max: 288
    unit: unit:V
  scope:
    products:
    - prod:solis-rhi-1p-hv-us
    standard: std:cpuc-rule-21
  conditions: Volt-Watt V2 (Vstart), Rule 21 settings, 240 V rated grid
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: sec=h155
    h: 6479cb047e94
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  attr: default_value
  value:
    nominal: 254
    unit: unit:V
  scope:
    products:
    - prod:solis-rhi-1p-hv-us
    standard: std:cpuc-rule-21
  conditions: Volt-Watt V2 (Vstart), Rule 21 default, 240 V rated grid
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: sec=h155
    h: 6479cb047e94
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c3
  attr: setting_range
  value:
    min: 240
    max: 288
    unit: unit:V
  scope:
    products:
    - prod:solis-rhi-1p-hv-us
    standard: std:cpuc-rule-21
  conditions: Volt-Watt V3 (Vstop), Rule 21 settings, 240 V rated grid
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: sec=h155
    h: 6479cb047e94
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  attr: default_value
  value:
    nominal: 264
    unit: unit:V
  scope:
    products:
    - prod:solis-rhi-1p-hv-us
    standard: std:cpuc-rule-21
  conditions: Volt-Watt V3 (Vstop), Rule 21 default, 240 V rated grid
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: sec=h155
    h: 6479cb047e94
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c5
  attr: setting_range
  value:
    min: 221
    max: 304
    unit: unit:V
  scope:
    products:
    - prod:canadian-solar-25-40k-t480gl01
    standard: std:cpuc-rule-21
  conditions: Volt-Watt V2 (Vstart), Rule 21 settings, 480 V rated grid
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=h201
    h: 53e82fd98f0b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  attr: default_value
  value:
    nominal: 293
    unit: unit:V
  scope:
    products:
    - prod:canadian-solar-25-40k-t480gl01
    standard: std:cpuc-rule-21
  conditions: Volt-Watt V2 (Vstart), Rule 21 default, 480 V rated grid
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=h201
    h: 53e82fd98f0b
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c7
  attr: setting_range
  value:
    min: 277
    max: 332
    unit: unit:V
  scope:
    products:
    - prod:canadian-solar-25-40k-t480gl01
    standard: std:cpuc-rule-21
  conditions: Volt-Watt V3 (Vstop), Rule 21 settings, 480 V rated grid
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=h201
    h: 53e82fd98f0b
  review: drafted
- claim_id: c8
  attr: default_value
  value:
    nominal: 304
    unit: unit:V
  scope:
    products:
    - prod:canadian-solar-25-40k-t480gl01
    standard: std:cpuc-rule-21
  conditions: Volt-Watt V3 (Vstop), Rule 21 default, 480 V rated grid
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=h201
    h: 53e82fd98f0b
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions)
---
Volt-Watt lowers the active power output of an inverter or battery system as grid voltage rises, following a programmable voltage versus power curve. On the Tesla commercial controls the response is open-loop, based on overvoltage measured at the POI meter. The curve is set with an enable flag, high voltage setpoints V1 and V2, a power limit P2 and a response time constant, and the resulting power limit can be read back over Modbus. Tesla project engineers can program the curve during commissioning, or it can be changed in real time over Modbus or DNP3 points. IEEE 1547-2018 defines a voltage-active power mode that can be switched on or off. Category A DER do not have to provide it, and the default settings guidance leaves it off. Volt-Watt is listed as a feature of the CPS SCA25KTL-DO/US-208 and SCA36KTL, the Solectria PVI series and Generac PWRmicro equipment. On the CPS SCA25KTL it is enabled for IEEE 1547-2018 and Rule 21 and disabled for ISO-NE.

<!-- review notes
- sentence 1: support check: partial - Passages say active power changes with voltage and Tesla limits via programmable curve against overvoltage, but 'inverter or battery' lowering as voltage rises is mostly implied; generally supported though not explicit about lowering for inverters (P3/P4 0%).
- sentence 5: support check: partial - Volt-Watt listed for SCA36KTL, PVI series, and the enabled/disabled settings are shown, but SCA25KTL-DO/US-208 listing and Generac PWRmicro are not clearly shown, and the settings table isn't tied to SCA25KTL.
-->
