---
id: proto:sunspec-model-131
type: Protocol
name: SunSpec model 131 Watt-PF
aliases:
- SunSpec 131
- model 131
- watt_pf
- Watt-PF cosPhi(P)
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: SMA's SunSpec Modbus documentation lists model 131 among the SunSpec information models, under
    the ones that are no longer supported in SunSpec profile 2.0.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=6
    h: 9cb9794eff5d
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=6
    h: 9cb9794eff5d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
SunSpec model 131 is a SunSpec information model for the Watt-PF function, which sets power factor as a function of active power (cosPhi(P)). As an information model, it defines a block of registers that a SunSpec Modbus client reads and writes. In that same list, the curve point W3 sits at SunSpec address 40507 as a read-write int16 value with a range of -1000 to 1000. It maps to the SMA parameter for the X values of characteristic curve 3. SMA SunSpec Modbus technical information says model 131 is no longer supported in SunSpec profile 2.0, so check which profile the inverter firmware uses before you rely on it. Under SunSpec profile 2.0, SMA recommends the 700-series models in place of the older 100-series models. Those include model 712 for Watt-Var and model 704 for AC controls.

<!-- review notes
- sentence 1: support check: partial - The passages name model 131 as Watt-PF cosPhi(P), but they don't say it sets power factor as a function of active power.
- sentence 2: support check: partial - The passages show registers carrying model 131 (ID 131, W3), but they don't state that the model is a block of registers a client reads and writes. That is only implied by the R and RW access columns.
- sentence 4: support check: partial - The passages say model 131 is no longer supported in profile 2.0. The advice to check the firmware's profile is not in them, and it is the statement's own recommendation.
- sentence 5: support check: partial - The passages say the 700 series is intended as the substitute for the 100 series and list 712 Watt-Var and 704 AC Controls. They don't say SMA 'recommends' the 700 series in general, only for specific models. This is a profile 2.0 extension planned for a future firmware version.
- sentence 4: review: partial - The SMA passages state model 131 is no longer supported in profile 2.0, but the advice to check the firmware's profile before relying on it is not in them.
-->
