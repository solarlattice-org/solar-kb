---
id: fc:sma-sunny-island-us-e203
type: FaultCode
name: SMA SI-US E203
aliases:
- E203
- e203
- SMA E203
- State change, battery charging algorithm for float charge
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E203
code_key: e203
display_message: State change, battery charging algorithm for float charge
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r2
    h: 308d2a48fb55
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Charging state change event
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r2
    h: 308d2a48fb55
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r2
    h: 308d2a48fb55
  review: drafted
---
