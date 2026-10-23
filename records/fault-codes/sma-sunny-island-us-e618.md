---
id: fc:sma-sunny-island-us-e618
type: FaultCode
name: SMA SI-US E618
aliases:
- E618
- e618
- SMA E618
- Relay 2 closed
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E618
code_key: e618
display_message: Relay 2 closed
page: 208
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r5
    h: a38ba44ae300
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Relay state event listed alongside operating status messages
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r5
    h: a38ba44ae300
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
