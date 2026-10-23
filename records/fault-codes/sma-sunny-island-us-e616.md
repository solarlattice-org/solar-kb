---
id: fc:sma-sunny-island-us-e616
type: FaultCode
name: SMA SI-US E616
aliases:
- E616
- e616
- SMA E616
- Transfer relay on slave 3 closed
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E616
code_key: e616
display_message: Transfer relay on slave 3 closed
page: 208
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r3
    h: 23476982ecf2
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Relay state event listed alongside operating status messages
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r3
    h: 23476982ecf2
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:transfer-relay
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r3
    h: 23476982ecf2
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
