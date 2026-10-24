---
id: fc:sma-sunny-island-us-e131
type: FaultCode
name: SMA SI-US E131
aliases:
- E131
- e131
- SMA E131
- Start of automatic frequency synchronization
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E131
code_key: e131
display_message: Start of automatic frequency synchronization
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r12
    h: 727bc558f64a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Event message reporting a frequency synchronization status step
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r12
    h: 727bc558f64a
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r12
    h: 727bc558f64a
  review: drafted
---
