---
id: fc:sma-sunny-island-us-e604
type: FaultCode
name: SMA SI-US E604
aliases:
- E604
- e604
- SMA E604
- Relay 1 slave 1 on
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E604
code_key: e604
display_message: Relay 1 slave 1 on
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r4
    h: 00689b7e9287
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Status event recording a slave device relay switching state.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r4
    h: 00689b7e9287
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r4
    h: 00689b7e9287
  review: drafted
---
