---
id: fc:sma-sunny-island-us-e122
type: FaultCode
name: SMA SI-US E122
aliases:
- E122
- e122
- SMA E122
- End of energy saving mode
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E122
code_key: e122
display_message: End of energy saving mode
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r9
    h: 23a7311a40c1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: 'Status message: energy saving mode ends.'
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r9
    h: 23a7311a40c1
  review: drafted
---
