---
id: proto:sunspec-model-706
type: Protocol
name: SunSpec model 706 DER Volt-Watt
aliases:
- SunSpec 706
- model 706
- DERVoltWatt
- DER Volt-Watt P(U)
- DER Volt-Watt
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 706 belongs to the 700 series of SunSpec information models, which is meant to replace the
    older 100 series and meet IEEE 1547-2018.
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
SunSpec model 706 is the DER Volt-Watt information model, also called P(U). It belongs to the SunSpec 700 series, which is intended to meet IEEE 1547:2018 requirements. SunSpec information models are standard data models carried over Modbus to monitor and control DER devices. In SunSpec profile 2.0, model 706 replaces the older model 132 Volt-Watt. SMA no longer supports model 132 in that profile. SMA's SunSpec Modbus notes for its US inverter firmware list the 700 series, including 706, as planned for a future firmware version. The older 100 series can still be used but is marked as outdated.

<!-- review notes
- sentence 2: support check: partial - Passages say SunSpec specifies Modbus-based information models for monitoring and control of DER, but 'standard data models carried over Modbus' is close; core supported, though it's a slight paraphrase.
- sentence 4: support check: partial - Passages say 700 series (incl. 706) comes in a future firmware version and 100 series is outdated but usable; nothing specifies US inverter firmware.
-->
