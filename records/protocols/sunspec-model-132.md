---
id: proto:sunspec-model-132
type: Protocol
name: SunSpec model 132 Volt-Watt
aliases:
- SunSpec 132
- model 132
- volt_watt
- Volt-Watt P(U)
- 132 - Volt-Watt
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 132 is one of the SunSpec information models; SunSpec groups registers into models that
    each start with an identifying header.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=6
    h: 9cb9794eff5d
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=6
    h: 9cb9794eff5d
  - src: src:eq-equip-inverters-solectria-xgi-1500-docr-071063-xgi-1500-modbus-map-c
    loc: sec=h4
    h: c413147499ae
  review: drafted
---
SunSpec model 132 is the Volt-Watt information model. It is a defined group of registers that sets up a voltage-dependent active power curve, P(U). The Solectria XGI 1500 implements model 132 in its Modbus map. The ModEna bitfield turns Volt-Watt control on, and it is off by default. The NPt register is read-only and reports how many curve points the array holds. Its default is 10. Each curve point has a read-write voltage register (V1 to V10) expressed in percent of Vref, with an unscaled setting range of 0-1200. Each point also has a watts register (W1, W2 and so on) with an unscaled range of 0-1000. On the XGI 1500, only the listed models are supported, and registers marked Reserved within a model should not be used. SMA SunSpec profile 2.0 no longer supports model 132. In that profile, model 706 DER Volt-Watt replaces it.

<!-- review notes
- sentence 1: support check: partial - Passages show 132 is Volt-Watt P(U) and models are register groups, but 'sets up a voltage-dependent active power curve' is only implied by the name and register descriptions.
- sentence 4: support check: partial - V1-V10 are RW, % Vref, range 0-1200 and W1/W2 range 0-1000 are shown, though only some of the points appear in the passages and W registers' scaling isn't elaborated.
- sentence 6: support check: partial - Passages say 132 is no longer supported in profile 2.0 and replaced by 706 (DER Volt-Watt P(U)), but the passages don't attribute this to SMA by name.
-->
