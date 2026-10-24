---
id: proto:sunspec-model-709
type: Protocol
name: SunSpec model 709 DER Trip LF
aliases:
- SunSpec 709
- model 709
- DERTripLF
- DER Trip LF
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Listed as model 709 DER Trip LF within the SunSpec 700 series of DER information models.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: drafted
---
SunSpec model 709, DER Trip LF, belongs to the SunSpec 700 series of information models. It sits next to 707 Trip LV, 708 Trip HV and 710 Trip HF. SMA's SunSpec Modbus documents say the 700 series is meant to replace the older 100 series so that SunSpec profile 2.0 meets IEEE 1547-2018. Those documents say this will come in a future firmware version. SunSpec is an application-layer protocol that lets DER equipment work with smart grid applications. Its information models are carried over Modbus to monitor and control DER devices. SunSpec groups registers into models, and each model starts with a header that gives its ID and its length. For Solectria XGI 1500 inverters, only the models listed in the Modbus map are supported, and registers that are not supported are marked Reserved. Use only the supported registers. On supported SMA products, the SunSpec Modbus profile starts at register number 40001.

<!-- review notes
- sentence 2: support check: partial - Passages say that in a future firmware version profile 2.0 is extended to meet IEEE1547:2018 and the 700 series substitutes the 100 series, but they never name SMA's documents, and they don't say that the 700 series is what brings the compliance.
- sentence 5: support check: partial - The passages say only the models listed in the document (Section 2.3) are supported, unsupported registers are marked Reserved, and only supported registers should be used. They don't say the listing is the 'Modbus map'.
-->
