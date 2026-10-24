---
id: proto:sunspec-model-713
type: Protocol
name: SunSpec model 713 DER Storage Capacity
aliases:
- SunSpec 713
- model 713
- DERStorageCapacity
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 713 DER Storage Capacity is one of the 700 series SunSpec information models; per SMA documentation
    it applies only to battery inverters.
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
SunSpec model 713, DER Storage Capacity, is an information model in the SunSpec 700 series. It defines a group of data points and does not set a transport. SunSpec models are standard Modbus-based information models used to monitor and control DER devices. SunSpec as a whole is described as an application-layer protocol for DER interoperability. SMA's SunSpec Modbus technical information lists model 713 in the 700 series. It notes that model 713 is only available on battery inverters. The 700 series is meant to replace the older 100 series so devices can meet IEEE 1547:2018. SMA says it will add the 700 series in a future firmware version, and the 100 series can still be used but is marked outdated. Each SunSpec model starts with a header that gives its identity and length. A device may not support every register in a model, so check the vendor map and only use the registers it supports. On SMA products, the SunSpec Modbus profile starts at register number 40001.

<!-- review notes
- sentence 1: support check: partial - 713 as a 700-series model is stated, but nothing says it defines a group of data points or that it does not set a transport.
- sentence 4: support check: partial - Passages say the 700 series substitutes the 100 series and the profile will be extended in a future firmware version to meet IEEE1547:2018, and the 100 series is outdated but usable; 'SMA says it will add the 700 series' is a slight rewording of extending the profile.
- sentence 5: support check: partial - Header with identity/length and 'only use supported registers' are stated (unsupported marked Reserved), but 'check the vendor map' is not stated and the source is SOLECTRIA-specific.
- sentence 1: review: partial - The passages list 713 DER Storage Capacity in the 700 series, but they say nothing about it defining a group of data points or not setting a transport.
-->
