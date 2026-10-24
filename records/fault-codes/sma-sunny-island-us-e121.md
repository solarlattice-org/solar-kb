---
id: fc:sma-sunny-island-us-e121
type: FaultCode
name: SMA SI-US E121
aliases:
- E121
- e121
- SMA E121
- Start of energy saving mode
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E121
code_key: e121
display_message: Start of energy saving mode
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r8
    h: c25532cfcce9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: 'Status message: energy saving mode starts.'
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r8
    h: c25532cfcce9
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r8
    h: c25532cfcce9
  review: drafted
---
