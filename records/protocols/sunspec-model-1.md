---
id: proto:sunspec-model-1
type: Protocol
name: SunSpec model 1 Common
aliases:
- SunSpec 1
- model 1
- common
- SunSpec 1.0 Common Model
- SunSpec Common Model Block
- SunSpec common model
- Common Block
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-modbus
  note: The common model block follows the SunS identifier that marks a SunSpec Modbus map.
  cite:
  - src: src:eq-equip-inverters-solaredge-sunspec-implementation-technical-note
    loc: tbl=4
    h: 182f8d267c44
  review: drafted
---
SunSpec model 1 is the Common model. It is an information model that identifies a device, and it sits at the start of a SunSpec Modbus register map. A reader recognizes the block because its C_SunSpec_DID register holds the well-known value 0x0001, followed by a C_SunSpec_Length register showing 65 registers. The block holds manufacturer, model, version and serial number strings, plus the device Modbus address. On SolarEdge inverters the common block starts at Modbus address 40001 (base 1) or 40000 (base 0). The manufacturer reads SolarEdge, the version is the CPU software version, and C_Options is not implemented. SolarEdge also exposes a separate common block for each connected meter, for example at 40121 (base 0), ahead of the meter model. Every SunSpec model starts with a header giving its ID and length, so use only the registers a device marks as supported.

<!-- review notes
- sentence 1: support check: partial - Passages show it is the Common Model Block, identifies the device, and starts right after the SunS ID at 40000; but 'model 1' as an 'information model' is not stated explicitly.
- sentence 5: support check: partial - A meter common block at 40121 (base 0) preceding the meter model is shown, but 'for each connected meter' (multiple meters) is not stated in the passages.
- sentence 6: support check: partial - Each model begins with a header giving ID and length, and only supported registers should be used; but 'a device marks as supported' is stated as unsupported being marked 'Reserved', and 'Every' model is slightly general; mostly consistent though.
-->
