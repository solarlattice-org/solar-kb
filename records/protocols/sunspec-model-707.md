---
id: proto:sunspec-model-707
type: Protocol
name: SunSpec model 707 DER Trip LV
aliases:
- SunSpec 707
- model 707
- DERTripLV
- DER Trip LV
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 707 belongs to the 700 series of SunSpec information models, intended to meet IEEE 1547:2018
    requirements.
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
SunSpec model 707, DER Trip LV, is one of the 700 series SunSpec information models. SunSpec information models are standard Modbus-based data definitions from the SunSpec Alliance for monitoring and controlling DER devices. SMA's SunSpec documentation says a future firmware will extend SunSpec profile 2.0 to meet IEEE 1547:2018. It names the 700 series as the replacement for the older 100 series, which SunSpec now marks as outdated. In SunSpec profile 2.0, model 707 replaces the older model 129 Trip LV, which SMA no longer supports. On SMA products, the SunSpec Modbus profile starts at register number 40001.
