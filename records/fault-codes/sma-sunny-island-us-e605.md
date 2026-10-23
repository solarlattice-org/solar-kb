---
id: fc:sma-sunny-island-us-e605
type: FaultCode
name: SMA SI-US E605
aliases:
- E605
- e605
- SMA E605
- Relay 1 slave 2 off
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E605
code_key: e605
display_message: Relay 1 slave 2 off
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r5
    h: b675ddfbab44
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Status event recording a slave device relay switching state.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r5
    h: b675ddfbab44
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
---
