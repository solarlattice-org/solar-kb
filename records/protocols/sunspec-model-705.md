---
id: proto:sunspec-model-705
type: Protocol
name: SunSpec model 705 DER Volt-Var
aliases:
- SunSpec 705
- model 705
- DERVoltVar
- DER Volt-Var Q(U)
- 705 - DER Volt-Var
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 705 belongs to the 700 series of SunSpec information models, intended to replace the 100
    series to meet IEEE 1547-2018.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: drafted
---
SunSpec model 705 is the DER Volt-Var information model, also listed as Q(U). It belongs to the 700 series of SunSpec models. The 700 series is meant to replace the older 100 series so that SunSpec profile 2.0 can meet IEEE 1547:2018. SunSpec still allows the 100 series but marks it as outdated. In profile 2.0, model 705 takes the place of model 126 Volt-Var, and model 126 is no longer supported there. SunSpec groups registers into models, and each model starts with a header that gives its identity and length. Use only the registers the device supports, because unsupported ones are marked Reserved. SMA SunSpec Modbus documentation for Sunny Tripower US inverter firmware lists model 705 among the 700-series models planned for a future firmware version.

<!-- review notes
- sentence 5: support check: partial - The passages list 705 among the 700-series models for a future firmware version, but they don't name Sunny Tripower US or SMA in the text.
-->
