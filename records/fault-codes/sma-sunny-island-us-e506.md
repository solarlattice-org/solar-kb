---
id: fc:sma-sunny-island-us-e506
type: FaultCode
name: SMA SI-US E506
aliases:
- E506
- e506
- SMA E506
- Manual grid release
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E506
code_key: e506
display_message: Manual grid release
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r6
    h: 78015cab44c6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Event log entry listed among status events; describes an operating step, not a fault.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r6
    h: 78015cab44c6
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r6
    h: 78015cab44c6
  review: drafted
---
