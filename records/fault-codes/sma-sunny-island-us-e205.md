---
id: fc:sma-sunny-island-us-e205
type: FaultCode
name: SMA SI-US E205
aliases:
- E205
- e205
- SMA E205
- State change, battery charging algorithm for full charge
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E205
code_key: e205
display_message: State change, battery charging algorithm for full charge
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r4
    h: 71f3d966459d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Charging state change event
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r4
    h: 71f3d966459d
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r4
    h: 71f3d966459d
  review: drafted
---
