---
id: fc:sma-sunny-island-us-e204
type: FaultCode
name: SMA SI-US E204
aliases:
- E204
- e204
- SMA E204
- State change, battery charging algorithm for boost charge
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E204
code_key: e204
display_message: State change, battery charging algorithm for boost charge
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r3
    h: '5e0631966767'
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Charging state change event
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r3
    h: '5e0631966767'
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
---
