---
id: fc:sma-sunny-island-us-e621
type: FaultCode
name: SMA SI-US E621
aliases:
- E621
- e621
- SMA E621
- Relay 2 slave 2 open
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E621
code_key: e621
display_message: Relay 2 slave 2 open
page: 208
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r8
    h: 5584d752f9cf
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Relay state event listed alongside operating status messages
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r8
    h: 5584d752f9cf
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
---
