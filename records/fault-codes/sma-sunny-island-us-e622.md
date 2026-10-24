---
id: fc:sma-sunny-island-us-e622
type: FaultCode
name: SMA SI-US E622
aliases:
- E622
- e622
- SMA E622
- Relay 2 slave 2 closed
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E622
code_key: e622
display_message: Relay 2 slave 2 closed
page: 208
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r9
    h: f200a9665595
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Row only reports a relay state change; no fault or action stated.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r9
    h: f200a9665595
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r9
    h: f200a9665595
  review: drafted
---
