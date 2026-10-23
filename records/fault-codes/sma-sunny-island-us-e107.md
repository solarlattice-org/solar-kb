---
id: fc:sma-sunny-island-us-e107
type: FaultCode
name: SMA SI-US E107
aliases:
- E107
- e107
- SMA E107
- Sleep mode (slave in single-phase systems)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E107
code_key: e107
display_message: Sleep mode (slave in single-phase systems)
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r1
    h: 1b804cf44394
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: 'Status message: slave sleep mode in single-phase systems.'
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r1
    h: 1b804cf44394
  review: drafted
---
