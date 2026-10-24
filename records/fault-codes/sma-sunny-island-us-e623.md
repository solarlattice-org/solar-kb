---
id: fc:sma-sunny-island-us-e623
type: FaultCode
name: SMA SI-US E623
aliases:
- E623
- e623
- SMA E623
- Relay 2 slave 3 open
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E623
code_key: e623
display_message: Relay 2 slave 3 open
page: 208
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r10
    h: 94820d05ccfc
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Row only reports a relay state change; no fault or action stated.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r10
    h: 94820d05ccfc
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r10
    h: 94820d05ccfc
  review: drafted
---
