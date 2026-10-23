---
id: fc:sma-sunny-island-us-e710
type: FaultCode
name: SMA SI-US E710
aliases:
- E710
- e710
- SMA E710
- Cluster firmware updated
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E710
code_key: e710
display_message: Cluster firmware updated
page: 208
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=139.r6
    h: 1411571290f6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Event row reporting cluster firmware update completion.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=139.r6
    h: 1411571290f6
  review: drafted
---
