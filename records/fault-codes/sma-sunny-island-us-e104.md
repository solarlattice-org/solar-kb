---
id: fc:sma-sunny-island-us-e104
type: FaultCode
name: SMA SI-US E104
aliases:
- E104
- e104
- SMA E104
- Operating on the generator (at external input)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E104
code_key: e104
display_message: Operating on the generator (at external input)
page: 205
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131.r4
    h: 787e1ec4e70b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Operating-state message for generator operation at the external input.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131.r4
    h: 787e1ec4e70b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_production_effect
  target: ec:no-production-effect
  note: The device is in operation.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131.r4
    h: 787e1ec4e70b
  review: drafted
---
