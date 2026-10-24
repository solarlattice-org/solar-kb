---
id: proto:sunspec-model-703
type: Protocol
name: SunSpec model 703 Enter Service
aliases:
- SunSpec 703
- model 703
- DEREnterService
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 703 Enter Service belongs to the 700 series of SunSpec information models, which is intended
    to replace the 100 series.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: drafted
---
SunSpec model 703, Enter Service, is one of the 700-series SunSpec information models. The 700 series is meant to replace the older 100 series of models so the SunSpec profile meets IEEE 1547:2018. The 100 series still works but SunSpec now marks it as outdated. SMA's SunSpec Modbus technical information lists model 703 among the 700-series models planned for a future inverter firmware version. SunSpec groups registers into models. Each model starts with a header that gives its identity and length, and a device may not support every register in a model. On SMA inverters the Modbus interface is turned off by default. To use it, select Modbus as the communication type and set the TCP port in the installation assistant. In SMA products, the SunSpec Modbus profile starts at register number 40001.

<!-- review notes
- sentence 3: support check: partial - Passages say the 700 series including 703 comes in a future firmware version, but they don't name SMA or a SunSpec Modbus technical information document.
-->
