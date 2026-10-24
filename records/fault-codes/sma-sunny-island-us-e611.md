---
id: fc:sma-sunny-island-us-e611
type: FaultCode
name: SMA SI-US E611
aliases:
- E611
- e611
- SMA E611
- Transfer relay on slave 1 open
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E611
code_key: e611
display_message: Transfer relay on slave 1 open
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r11
    h: e78bd8263be1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Relay state event listed alongside operating status messages
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r11
    h: e78bd8263be1
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:transfer-relay
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r11
    h: e78bd8263be1
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r11
    h: e78bd8263be1
  review: drafted
---
