---
id: fc:sma-sunny-island-us-e852
type: FaultCode
name: SMA SI-US E852
aliases:
- E852
- e852
- SMA E852
- 'Sunny Island Charger #2 detected'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E852
code_key: e852
display_message: 'Sunny Island Charger #2 detected'
page: 208
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=139.r10
    h: baa02d35f201
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Event row reporting detection of a connected charge controller.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=139.r10
    h: baa02d35f201
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=139.r10
    h: baa02d35f201
  review: drafted
---
