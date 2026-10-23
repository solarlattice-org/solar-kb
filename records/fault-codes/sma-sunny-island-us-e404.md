---
id: fc:sma-sunny-island-us-e404
type: FaultCode
name: SMA SI-US E404
aliases:
- E404
- e404
- SMA E404
- Manual generator stop
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E404
code_key: e404
display_message: Manual generator stop
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=135.r1
    h: 15deac453e90
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Logs an operator-initiated generator stop.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=135.r1
    h: 15deac453e90
  review: drafted
---
