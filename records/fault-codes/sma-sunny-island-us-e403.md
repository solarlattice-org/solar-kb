---
id: fc:sma-sunny-island-us-e403
type: FaultCode
name: SMA SI-US E403
aliases:
- E403
- e403
- SMA E403
- Manual generator start
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E403
code_key: e403
display_message: Manual generator start
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=134.r3
    h: '383998081e05'
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Logs an operator-initiated generator start.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=134.r3
    h: '383998081e05'
  review: drafted
---
