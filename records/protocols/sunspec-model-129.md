---
id: proto:sunspec-model-129
type: Protocol
name: SunSpec model 129 LVRTD
aliases:
- SunSpec 129
- model 129
- lvrt
- LVRTD
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Listed as one of the SunSpec models in the SunSpec Model Overview table of the XGI 1500 Modbus
    map.
  cite:
  - src: src:eq-equip-inverters-yaskawa-yaskawa-solectria-xgi-1500-programming-docr-071063-xgi-1500-modbus-map-d
    loc: tbl=2
    h: 1c93cb0d72a7
  - src: src:eq-equip-inverters-solectria-xgi-1500-docr-071063-xgi-1500-modbus-map-c
    loc: tbl=2
    h: 1c93cb0d72a7
  - src: src:eq-equip-inverters-solectria-xgi-1500-docr-071063-xgi-1500-modbus-map-c
    loc: sec=h4
    h: c413147499ae
  - src: src:eq-equip-inverters-yaskawa-yaskawa-solectria-xgi-1500-programming-docr-071063-xgi-1500-modbus-map-d
    loc: sec=h4
    h: 8a537b6f00cb
  review: drafted
---
SunSpec model 129 (LVRTD) is an information model: a fixed group of registers within the SunSpec register map, read and written over Modbus. SunSpec sorts registers into models, and each model opens with a header that gives its ID and its length. The model includes read-only scale factors. Tms_SF at 40325 is -2 and scales durations, and V_SF at 40326 is -1 and scales the voltage values given as a percentage of VRef. Not every register in a model is supported. Unsupported ones are marked Reserved and should not be used.

<!-- review notes
- sentence 1: support check: partial - The passages show that models are groups of registers in the SunSpec map and that Model 129 exists, but they never say the model is read and written over Modbus (the 'Modbus' framing comes only from the statement).
- sentence 2: support check: partial - The passages say registers are organized into models and each model begins with a header identifying it and its length; they don't state that the header gives an ID specifically, though 'identify it' implies this.
-->
