---
id: fc:sma-sunny-island-us-e854
type: FaultCode
name: SMA SI-US E854
aliases:
- E854
- e854
- SMA E854
- 'Sunny Island Charger #4 detected'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E854
code_key: e854
display_message: 'Sunny Island Charger #4 detected'
page: 209
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=140.r2
    h: 1dee40917f2e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Event row reporting detection of a connected charge controller.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=140.r2
    h: 1dee40917f2e
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
