---
id: fc:sma-sunny-island-us-e610
type: FaultCode
name: SMA SI-US E610
aliases:
- E610
- e610
- SMA E610
- Transfer relay closed
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E610
code_key: e610
display_message: Transfer relay closed
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r10
    h: 71d0aac7756b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Relay state event listed alongside operating status messages
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r10
    h: 71d0aac7756b
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:transfer-relay
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r10
    h: 71d0aac7756b
  review: drafted
---
