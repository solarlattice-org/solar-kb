---
id: proto:sunspec-model-127
type: Protocol
name: SunSpec model 127 Freq-Watt Param
aliases:
- SunSpec 127
- model 127
- freq_watt_param
- Frequency-Watt P(f)
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: SMA lists model 127 among the SunSpec information models that SunSpec profile 2.0 no longer supports.
    Its replacement there is model 711.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=6
    h: 9cb9794eff5d
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=6
    h: 9cb9794eff5d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
SunSpec model 127 is the SunSpec information model for frequency-watt, or P(f), settings. SunSpec is an application-layer protocol that lets DER components work with smart grid applications. It groups registers into models, and each model starts with a header that gives its identity and length. In the same model, register 40464 (WGra) is the read-write active power gradient in percent, with a range of 10 % to 130 % and a default of 40 %. Its scale factor is in register 40470. SMA SunSpec documentation says model 127 is no longer supported in SunSpec profile 2.0, where model 711 replaces it. Vendors mark the registers they do not support as Reserved. Read or write only the supported ones.

<!-- review notes
- sentence 5: support check: partial - Passage says unsupported registers are marked Reserved and only supported ones should be used, but it is about SunSpec/SOLECTRIA, not stated as a general vendor practice, and doesn't mention reading vs writing.
-->
