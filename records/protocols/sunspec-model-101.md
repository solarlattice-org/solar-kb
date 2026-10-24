---
id: proto:sunspec-model-101
type: Protocol
name: SunSpec model 101 Inverter (Single Phase)
aliases:
- SunSpec 101
- model 101
- inverter_single_phase
- single phase AC Monitoring
- SunSpec module ID 101
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 101 is one of the 100-series inverter models, listed as single phase AC monitoring; SMA
    designates the 100 series as outdated and recommends model 701 instead.
  cite:
  - src: src:eq-equip-inverters-solaredge-sunspec-implementation-technical-note
    loc: sec=h36
    h: d0cf25520c31
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: drafted
---
SunSpec model 101 is the SunSpec information model for AC monitoring data from a single-phase inverter. It is exposed as a block of Modbus registers. Like every SunSpec model, it starts with a header that gives the model ID and its length. Registers a device does not support are marked Reserved. SolarEdge inverters use model 101, 102 or 103 mappings for read-only Modbus monitoring data, based on the SunSpec inverter models specification. In the SolarEdge map, the model ID register C_SunSpec_DID sits at address 40069 (base 0) or 40070 (base 1). A value of 101 there means single phase, 102 split phase and 103 three phase. On SolarEdge inverters, the common block before the inverter model starts at 40000 (base 0) or 40001 (base 1). It holds the manufacturer, model, version, serial number and Modbus device ID. The Modbus list for the SMA Sunny Highpower PEAK3 maps the grid phase currents to model 101 registers 40189 to 40191. Their scale factor is in register 40192. SMA SunSpec Modbus documents still list model 101 as supported but recommend model 701. They describe the 100 series as outdated and the 700 series as its replacement for IEEE 1547-2018.

<!-- review notes
- sentence 1: support check: partial - Passages say 101 is single phase AC monitoring, but nothing states it is exposed as a block of Modbus registers beyond register mapping context (loosely implied).
- sentence 5: support check: partial - Base addresses 40000/40001 and manufacturer, model, version, serial, device ID are stated, but nothing says the block precedes the inverter model.
- sentence 7: support check: partial - Passages show 101 supported with 701 recommended and 100 series outdated, replaced by the 700 series for IEEE1547:2018, but don't name SMA or 'SMA documents' explicitly.
-->
