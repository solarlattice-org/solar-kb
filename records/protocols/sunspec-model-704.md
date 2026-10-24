---
id: proto:sunspec-model-704
type: Protocol
name: SunSpec model 704 DER AC Controls
aliases:
- SunSpec 704
- model 704
- DERCtlAC
- AC Controls
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 704 (AC Controls) is listed as one of the 700 series of SunSpec information models, which
    are meant to replace the 100 series so that devices can meet IEEE 1547:2018.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: drafted
---
SunSpec model 704 is the AC Controls information model. It belongs to the 700 series of SunSpec information models. SunSpec information models are standard data models built on Modbus. They are used to monitor and control distributed energy resources. The 700 series was planned as the replacement for the older 100 series, so that the SunSpec profile could meet IEEE 1547:2018 requirements. SMA's SunSpec Modbus documentation recommends model 704 instead of model 123, Inverter Immediate Controls. The 100 series models still work, but SunSpec labels them as outdated. On SMA products, the SunSpec Modbus profile begins at register number 40001.

<!-- review notes
- sentence 2: support check: partial - Passage says SunSpec specifies standard Modbus-based information models for monitoring and control of DER devices, which supports the statement.
-->
