---
id: fc:sma-sunny-island-us-e120
type: FaultCode
name: SMA SI-US E120
aliases:
- E120
- e120
- SMA E120
- Manual stop (transition from operation to standby mode)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E120
code_key: e120
display_message: Manual stop (transition from operation to standby mode)
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r7
    h: 9caf04cd64ad
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: 'Status message: manual transition from operation to standby.'
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r7
    h: 9caf04cd64ad
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: The device leaves operation and enters standby.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r7
    h: 9caf04cd64ad
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r7
    h: 9caf04cd64ad
  review: drafted
---
