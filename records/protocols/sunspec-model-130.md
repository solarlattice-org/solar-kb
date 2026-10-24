---
id: proto:sunspec-model-130
type: Protocol
name: SunSpec model 130 HVRTD
aliases:
- SunSpec 130
- model 130
- hvrt
- HVRTD
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: SunSpec groups registers into numbered models, each starting with a header that identifies the
    model and its length; model 130 (HVRTD) is listed in the SunSpec model overview.
  cite:
  - src: src:eq-equip-inverters-yaskawa-yaskawa-solectria-xgi-1500-programming-docr-071063-xgi-1500-modbus-map-d
    loc: tbl=2
    h: 1c93cb0d72a7
  - src: src:eq-equip-inverters-solectria-xgi-1500-docr-071063-xgi-1500-modbus-map-c
    loc: sec=h4
    h: c413147499ae
  - src: src:eq-equip-inverters-yaskawa-yaskawa-solectria-xgi-1500-programming-docr-071063-xgi-1500-modbus-map-d
    loc: sec=h4
    h: 8a537b6f00cb
  - src: src:yaskawa-xgi-1500-modbus-map-docr-071063-rev-h
    loc: sec=h4
    h: b6c562ff2dd3
  review: drafted
---
SunSpec model 130 (HVRTD) is a SunSpec information model. It is a defined block of Modbus registers that starts with a header giving the model ID and its length. The first register of the block, at 40378, is a read-only uint16 that holds the model number 130. SMA firmware notes for models 129 and 130 report a correction: V1, V2 and V3 are now given in percent of VRef instead of volts. Not every register in the model is supported. Unsupported ones are marked Reserved, and only the supported registers should be used.

<!-- review notes
- sentence 1: support check: partial - Passages say models are register groups starting with a header giving identity and length, and list model 130, but don't explicitly say the header holds the model ID (though the ID register is elsewhere) or mention Modbus.
- sentence 3: support check: partial - Passages say V1, V2, V3 unit corrected to % of VRef instead of V for models 129/130, but do not attribute it to SMA firmware notes explicitly.
-->
