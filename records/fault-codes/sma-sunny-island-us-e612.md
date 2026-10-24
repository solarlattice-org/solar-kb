---
id: fc:sma-sunny-island-us-e612
type: FaultCode
name: SMA SI-US E612
aliases:
- E612
- e612
- SMA E612
- Transfer relay on slave 1 closed
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E612
code_key: e612
display_message: Transfer relay on slave 1 closed
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r12
    h: ca325c8b16b9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Relay state event listed alongside operating status messages
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r12
    h: ca325c8b16b9
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:transfer-relay
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r12
    h: ca325c8b16b9
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r12
    h: ca325c8b16b9
  review: drafted
---
