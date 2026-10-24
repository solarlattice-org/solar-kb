---
id: fc:sma-sunny-island-us-e624
type: FaultCode
name: SMA SI-US E624
aliases:
- E624
- e624
- SMA E624
- Relay 2 slave 3 closed
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E624
code_key: e624
display_message: Relay 2 slave 3 closed
page: 208
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r11
    h: 5faf17dde0c3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Row only reports a relay state change; no fault or action stated.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r11
    h: 5faf17dde0c3
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r11
    h: 5faf17dde0c3
  review: drafted
---
