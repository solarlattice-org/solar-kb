---
id: fc:sma-sunny-island-us-e106
type: FaultCode
name: SMA SI-US E106
aliases:
- E106
- e106
- SMA E106
- Feeding-in grid operation (at external input)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E106
code_key: e106
display_message: Feeding-in grid operation (at external input)
page: 205
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131.r6
    h: 5cb10a936f54
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Operating-state message for grid feed-in operation.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131.r6
    h: 5cb10a936f54
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:no-production-effect
  note: The device is feeding in.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131.r6
    h: 5cb10a936f54
  review: drafted
---
