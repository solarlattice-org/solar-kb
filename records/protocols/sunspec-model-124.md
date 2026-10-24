---
id: proto:sunspec-model-124
type: Protocol
name: SunSpec model 124 Storage
aliases:
- SunSpec 124
- model 124
- storage_basic
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: SunSpec groups registers into numbered models. In a SunSpec register map, model 124 is identified
    by an ID register whose value is 124.
  cite:
  - src: src:eq-equip-inverters-solectria-xgi-1500-docr-071063-xgi-1500-modbus-map-c
    loc: sec=h4
    h: c413147499ae
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-modbus-html-shpxx-20-us-v10-modbuslist-en
    loc: tbl=1.r370
    h: a50d9170b832
  review: drafted
  review_note: 'support check: partial - Passages show models are register groups and an ID register at
    40370 with default 124, but don''t name it as model 124 Storage.; review: partial - The passages show
    that SunSpec groups registers into models and that an ID register at 40370 defaults to 124, but no
    quoted passage names model 124 as ''Storage'' or ties that row to the Storage model.'
---
SunSpec model 124 (Storage) is one of the numbered register groups that make up the SunSpec information models. SunSpec is an application-layer protocol. Its aim is to let distributed energy resource equipment and smart grid applications work together. Every SunSpec model starts with a header that gives its identity and its length. A client finds model 124 by reading an ID register that holds the value 124. A device may leave some registers in a model unsupported and mark them Reserved. Read only the registers that the device's own map lists as supported.

<!-- review notes
- sentence 1: support check: partial - Models as register groups and an ID register value of 124 are shown, but the Storage name for model 124 is not stated.
- sentence 3: support check: partial - Headers identifying model and length are stated, and an ID register with default 124 appears, but it isn't stated that a client finds model 124 this way.
- sentence 1: review: partial - The passages show that models are register groups and that an ID register defaults to 124, but neither one names model 124 as Storage.
-->
