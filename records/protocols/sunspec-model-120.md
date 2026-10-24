---
id: proto:sunspec-model-120
type: Protocol
name: SunSpec model 120 Nameplate
aliases:
- SunSpec 120
- model 120
- nameplate
- Model 120 - Nameplate
- Inverter Nameplate ratings
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 120 is one of the 100-series SunSpec information models; SMA lists it as Inverter Nameplate
    ratings and recommends model 702 instead.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-solectria-xgi-1500-docr-071063-xgi-1500-modbus-map-c
    loc: sec=h4
    h: c413147499ae
  - src: src:eq-equip-inverters-yaskawa-yaskawa-solectria-xgi-1500-programming-docr-071063-xgi-1500-modbus-map-d
    loc: sec=h4
    h: 8a537b6f00cb
  review: drafted
---
SunSpec model 120 Nameplate is a SunSpec information model. SunSpec sorts device registers into models, and each model starts with a header that gives its ID and length. The model also contains scale factor registers. One example is VARtg_SF at 40190, which scales the output volt-ampere rating. Read only the registers the device supports. Registers it does not support are marked Reserved in the map. SMA lists model 120 as Inverter Nameplate ratings among the models its SunSpec Modbus interface supports, and it recommends model 702 instead. SMA says the 700 series of models is meant to replace the 100 series to meet IEEE 1547:2018. The 100 series still works, but SunSpec marks it as outdated.

<!-- review notes
- sentence 2: support check: partial - VARtg_SF at 40190 is a scale factor for output VA rating, but the passages don't state it belongs to model 120 or that the model contains other scale factor registers.
-->
