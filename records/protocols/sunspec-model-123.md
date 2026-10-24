---
id: proto:sunspec-model-123
type: Protocol
name: SunSpec model 123 Immediate Controls
aliases:
- SunSpec 123
- model 123
- controls
- SunSpec model 123
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: subclass_of
  target: proto:sunspec-information-model
  note: Listed as one of the SunSpec models in the XGI 1500 SunSpec model overview.
  cite:
  - src: src:eq-equip-inverters-solectria-xgi-1500-docr-071063-xgi-1500-modbus-map-c
    loc: tbl=2
    h: 1c93cb0d72a7
  - src: src:eq-equip-inverters-yaskawa-yaskawa-solectria-xgi-1500-programming-docr-071063-xgi-1500-modbus-map-d
    loc: tbl=2
    h: 1c93cb0d72a7
  - src: src:eq-equip-inverters-solectria-xgi-1500-docr-071063-xgi-1500-modbus-map-c
    loc: sec=h4
    h: c413147499ae
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
SunSpec model 123 Immediate Controls is one of the SunSpec information models, which group device registers into models that each start with a header giving the model ID and length. The first register at 40290 is a read-only uint16 holding the model number 123. The block also carries a read-only reactive power percent scale factor, VArPct_SF, at 40315 with a value of -1. On the XGI 1500, not every register in a model is supported; unsupported ones are marked Reserved and should not be used.
