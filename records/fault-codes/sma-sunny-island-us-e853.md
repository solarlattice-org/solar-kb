---
id: fc:sma-sunny-island-us-e853
type: FaultCode
name: SMA SI-US E853
aliases:
- E853
- e853
- SMA E853
- 'Sunny Island Charger #3 detected'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E853
code_key: e853
display_message: 'Sunny Island Charger #3 detected'
page: 209
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=140.r1
    h: a546f0f74956
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Event row reporting detection of a connected charge controller.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=140.r1
    h: a546f0f74956
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
