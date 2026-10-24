---
id: fc:sma-sunny-island-us-e501
type: FaultCode
name: SMA SI-US E501
aliases:
- E501
- e501
- SMA E501
- Grid request due to SOC (insufficient value)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E501
code_key: e501
display_message: Grid request due to SOC (insufficient value)
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r1
    h: 4ba0c3277246
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Grid requested because battery state of charge is insufficient.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r1
    h: 4ba0c3277246
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r1
    h: 4ba0c3277246
  review: drafted
---
