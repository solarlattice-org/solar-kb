---
id: proto:sunspec-model-710
type: Protocol
name: SunSpec model 710 DER Trip HF
aliases:
- SunSpec 710
- model 710
- DERTripHF
- DER Trip HF
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Listed as model 710 (DER Trip HF) in the SunSpec 700 series, which is meant to replace the 100
    series and meet IEEE 1547:2018 requirements.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: drafted
---
SunSpec model 710, DER Trip HF, is one of the information models in the SunSpec 700 series. The 700 series is meant to replace the older 100 series so devices can meet IEEE 1547:2018. The 100 series still works, but SunSpec now treats it as outdated. SMA's SunSpec Modbus documentation says a future firmware version will extend SunSpec profile 2.0 with the 700 series. Model 710 is on that list, alongside the trip models 707 (LV), 708 (HV) and 709 (LF). SunSpec is an application-layer protocol that lets distributed energy resource equipment work with smart grid applications. SunSpec groups registers into models. Each model starts with a header that gives its identity and length. Registers a device does not support are marked Reserved and should not be used. On SMA products, the SunSpec Modbus profile begins at register number 40001.

<!-- review notes
- sentence 3: support check: partial - The passages state the future firmware extension and list 710 alongside 707, 708 and 709, but the passages never name SMA or its documentation as the source.
- sentence 5: support check: partial - The passages support models, headers and Reserved marking of unsupported registers. They say 'only use supported registers', not that Reserved ones 'should not be used', and say nothing about a device marking them, though this is close.
-->
