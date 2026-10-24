---
id: proto:sunspec-model-701
type: Protocol
name: SunSpec model 701 DER AC Measurement
aliases:
- SunSpec 701
- model 701
- DERMeasureAC
- '701'
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 701 is listed as the first model of the SunSpec 700 series, which is meant to replace the
    100 series for IEEE 1547-2018 support.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: drafted
---
SunSpec model 701, DER AC Measurement, is an information model in the SunSpec 700 series. It is not a transport layer. The SunSpec Alliance defines standard information models built on Modbus for monitoring and controlling DER devices. The 700 series is meant to replace the older 100 series so that devices can meet IEEE 1547-2018. The 100 series still works, but SunSpec now marks it as outdated. SMA's SunSpec Modbus documentation recommends model 701 instead of the single-phase, split-phase and three-phase AC monitoring models 101, 102 and 103. SMA's documentation says the 700 series will come with a future firmware version, when its SunSpec profile is extended for IEEE 1547-2018. Check the firmware notes to see whether a given inverter actually offers model 701. SunSpec groups registers into models. Each model starts with a header that gives its ID and length, so a client should scan the headers to find a model and read only the registers marked as supported. On SMA products, the SunSpec Modbus profile starts at register 40001.

<!-- review notes
- sentence 1: support check: partial - The passages say 701 is an information model in the 700 series, but they never state it is not a transport layer.
- sentence 5: support check: partial - The passages say the profile will be extended in a future firmware version, but they say nothing about checking firmware notes to see whether an inverter offers 701.
- sentence 6: support check: partial - Models, headers with ID and length, and using only supported registers are stated; the advice to scan headers to find a model is not stated, and the passage is for SOLECTRIA inverters.
-->
