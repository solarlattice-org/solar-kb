---
id: fc:sma-sunny-island-us-e108
type: FaultCode
name: SMA SI-US E108
aliases:
- E108
- e108
- SMA E108
- Silent mode on utility grid
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E108
code_key: e108
display_message: Silent mode on utility grid
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r2
    h: 396b7714ab51
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: 'Status message: silent mode while on the utility grid.'
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r2
    h: 396b7714ab51
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r2
    h: 396b7714ab51
  review: drafted
---
