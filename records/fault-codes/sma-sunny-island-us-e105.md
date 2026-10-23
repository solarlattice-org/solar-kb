---
id: fc:sma-sunny-island-us-e105
type: FaultCode
name: SMA SI-US E105
aliases:
- E105
- e105
- SMA E105
- Operation on utility grid (at external input)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E105
code_key: e105
display_message: Operation on utility grid (at external input)
page: 205
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131.r5
    h: 27db0f99363f
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Operating-state message for utility grid operation at the external input.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131.r5
    h: 27db0f99363f
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:no-production-effect
  note: The device is in operation.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131.r5
    h: 27db0f99363f
  review: drafted
---
