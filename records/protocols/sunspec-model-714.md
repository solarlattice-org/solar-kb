---
id: proto:sunspec-model-714
type: Protocol
name: SunSpec model 714 DER DC Measurement
aliases:
- SunSpec 714
- model 714
- DERMeasureDC
- DC Monitoring
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 714 (DC Monitoring) is one of the SunSpec 700-series information models.
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
SunSpec model 714 is a SunSpec information model in the 700 series, listed as DC Monitoring. SMA's SunSpec Modbus technical information lists model 714 as the recommended choice over the older model 160 for DC monitoring. The 700 series is meant to replace the 100 series so that the SunSpec profile meets IEEE 1547-2018. The 100 series still works, but SunSpec marks it as outdated. SunSpec sorts registers into models, and each model starts with a header that gives its identity and length. A device does not have to support every register in a model. Unsupported registers are marked Reserved and should not be used. SunSpec Modbus information models are standard Modbus-based models for monitoring and controlling DER devices.

<!-- review notes
- sentence 5: support check: partial - The passages say not all registers in a model are supported, unsupported ones are marked Reserved, and only supported registers should be used. They don't say this applies to any device in general; the context is the SOLECTRIA XGI 1500.
-->
