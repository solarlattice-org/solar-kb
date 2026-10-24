---
id: proto:sunspec-model-702
type: Protocol
name: SunSpec model 702 DER Capacity
aliases:
- SunSpec 702
- model 702
- DERCapacity
- DER Capacity
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 702 DER Capacity is listed among the 700 series of SunSpec information models, which is
    meant to replace the 100 series.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: drafted
---
SunSpec model 702, DER Capacity, belongs to the SunSpec 700 series of information models. That series is meant to replace the older 100 series so devices can meet IEEE 1547:2018. SMA SunSpec Modbus documentation recommends model 702 in place of model 120 (inverter nameplate ratings) and model 121 (inverter nameplate settings). SunSpec now marks the 100 series as outdated, but it can still be used. SMA says the 700 series will arrive with a future firmware version, when its SunSpec profile 2.0 is extended. Check which models the inverter firmware actually supports before relying on model 702. SunSpec groups registers into models. Each model starts with a header that gives its identity and length, and registers a device does not support are marked Reserved. The SunSpec Alliance defines these Modbus-based information models for monitoring and controlling DER devices. SunSpec itself is described as an application-layer protocol. On SMA products, the SunSpec Modbus profile starts at register number 40001.

<!-- review notes
- sentence 3: support check: partial - The future firmware extension is stated, but the advice to check firmware support before relying on 702 is not in the passages (also 'SMA says' of 700 series arriving is a reasonable paraphrase).
-->
