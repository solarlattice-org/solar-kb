---
id: fc:sma-sunny-island-us-e607
type: FaultCode
name: SMA SI-US E607
aliases:
- E607
- e607
- SMA E607
- Relay 1 slave 3 off
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E607
code_key: e607
display_message: Relay 1 slave 3 off
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r7
    h: f58c2b2880ab
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Status event recording a slave device relay switching state.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r7
    h: f58c2b2880ab
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
---
