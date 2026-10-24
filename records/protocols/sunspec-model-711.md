---
id: proto:sunspec-model-711
type: Protocol
name: SunSpec model 711 DER Frequency Droop
aliases:
- SunSpec 711
- model 711
- DERFreqDroop
- DER Frequency Droop P(f)
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 711 belongs to the 700 series of SunSpec information models, which the SMA documents describe
    as the replacement for the 100 series so that SunSpec profile 2.0 meets IEEE 1547-2018.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: drafted
---
SunSpec model 711 is an information model in the SunSpec 700 series. Its name there is DER Frequency Droop P(f). The 700 series is meant to replace the older 100 series so that SunSpec profile 2.0 meets IEEE 1547-2018. The 100 series can still be used, but SunSpec marks it as outdated. In profile 2.0, model 711 takes the place of model 127 Frequency-Watt P(f), which is no longer supported. The SMA SunSpec Modbus technical information lists model 711 among the 700-series models planned for a future firmware version. The models supported now are 100-series models such as 101 to 103, 120 to 123 and 160. SunSpec groups registers into models. Each model starts with a header that gives its identity and length, and you should only use the registers a device marks as supported.

<!-- review notes
- sentence 4: support check: partial - Passages say the 700 series comes in a future firmware version and list currently supported 100-series models, but they don't name 711 as planned and the 'SMA SunSpec Modbus technical information' source is not named.
-->
