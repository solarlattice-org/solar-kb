---
id: fc:sma-sunny-island-us-e502
type: FaultCode
name: SMA SI-US E502
aliases:
- E502
- e502
- SMA E502
- Release of grid due to SOC (exceeds)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E502
code_key: e502
display_message: Release of grid due to SOC (exceeds)
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r2
    h: 0a2de9d3ebda
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Grid released because battery state of charge exceeds threshold.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r2
    h: 0a2de9d3ebda
  review: drafted
---
