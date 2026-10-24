---
id: proto:sunspec-model-128
type: Protocol
name: SunSpec model 128 Dynamic Reactive Current
aliases:
- SunSpec 128
- model 128
- reactive_current
- Dynamic Reactive Current
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Listed as SunSpec information model 128, Dynamic Reactive Current; SMA SunSpec documentation states
    it is no longer supported in SunSpec profile 2.0, and no replacement model is named.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=6
    h: 9cb9794eff5d
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=6
    h: 9cb9794eff5d
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-modbus-html-shpxx-20-us-v10-modbuslist-en
    loc: tbl=1.r172
    h: 2cbe42c0baf8
  review: drafted
---
SunSpec model 128 is the SunSpec information model for dynamic reactive current. It describes a group of registers. It is not a transport. Like other SunSpec models, it starts with a header that gives the model ID and its length. A device may support only some registers inside a model. There, ModEna at SunSpec register 40479 sets full or limited dynamic grid support. ArGraMod at 40476 sets the reactive current droop. BlkZnV at 40483 sets the PWM inverse voltage, with a default of 70 %. HysBlkZnV at 40484 sets the hysteresis voltage, with a default of 5 %. SMA SunSpec Modbus documentation says model 128 is no longer supported in SunSpec profile 2.0. Unlike several other old models, no replacement model is listed for it.

<!-- review notes
- sentence 1: support check: partial - Model 128 is named Dynamic Reactive Current and its registers appear, but the passages don't explicitly say it describes a group of registers or that it is not a transport.
-->
