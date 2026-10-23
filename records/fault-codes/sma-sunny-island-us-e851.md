---
id: fc:sma-sunny-island-us-e851
type: FaultCode
name: SMA SI-US E851
aliases:
- E851
- e851
- SMA E851
- 'Sunny Island Charger #1 detected'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E851
code_key: e851
display_message: 'Sunny Island Charger #1 detected'
page: 208
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=139.r9
    h: 143b538f6386
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Event row reporting detection of a connected charge controller.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=139.r9
    h: 143b538f6386
  review: drafted
---
