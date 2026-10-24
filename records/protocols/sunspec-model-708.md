---
id: proto:sunspec-model-708
type: Protocol
name: SunSpec model 708 DER Trip HV
aliases:
- SunSpec 708
- model 708
- DERTripHV
- DER Trip HV
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Listed as model 708 within the 700 series of SunSpec information models, which extends SunSpec
    profile 2.0 toward IEEE 1547:2018.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: drafted
---
Model 708, DER Trip HV, is one of the SunSpec information models in the 700 series. The 700 series is meant to replace the older 100 series so that SunSpec profile 2.0 meets the requirements of IEEE 1547:2018. The 100 series can still be used, but SunSpec marks it as outdated. In SunSpec profile 2.0, model 708 takes the place of the older model 130, Trip HV, which that profile no longer supports. SMA's SunSpec Modbus technical information lists model 708 among the 700 series models planned for a future inverter firmware version. Check the firmware's supported-model list before trying to read it. SunSpec groups registers into models. Each model starts with a header that gives its identity and length, and you should only use the registers a device marks as supported.

<!-- review notes
- sentence 4: support check: partial - The passages say the 700 series is planned for a future firmware version, but they don't name SMA or say to check the supported-model list before reading 708. The 'SMA' attribution and the advice are missing.
-->
