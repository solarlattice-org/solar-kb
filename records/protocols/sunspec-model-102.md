---
id: proto:sunspec-model-102
type: Protocol
name: SunSpec model 102 Inverter (Split-Phase)
aliases:
- SunSpec 102
- model 102
- inverter_split_phase
- split phase AC Monitoring
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Listed as model 102 in the SunSpec 100 series of inverter information models, which SunSpec now
    marks as outdated in favour of the 700 series.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
SunSpec model 102 is the split-phase inverter AC monitoring model. It is one of the SunSpec information models, alongside model 101 for single phase and model 103 for three phase. It works at the information-model layer and is read over Modbus. SolarEdge inverters base their read-only Modbus monitoring map on the SunSpec inverter models. On SolarEdge inverters the model ID register C_SunSpec_DID sits at address 40069 (base 0) or 40070 (base 1). A value of 102 there means split phase, and the next register gives the block length. SolarEdge supports model 102 only in split-phase configurations: the Japanese grid and the 240V grid in North America. SMA SunSpec Modbus documentation also lists model 102 as supported, but recommends model 701 instead. SunSpec designates the 100 series as outdated and intends the 700 series to replace it to meet IEEE 1547:2018 requirements. The 100 series can still be used.

<!-- review notes
- sentence 5: support check: partial - The passages list 102 as supported and recommend 701, but nothing in them names SMA as the source.
-->
