---
id: fc:sma-sunny-island-us-e632
type: FaultCode
name: SMA SI-US E632
aliases:
- E632
- e632
- SMA E632
- Digital input slave 3 to ON (high)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E632
code_key: e632
display_message: Digital input slave 3 to ON (high)
page: 208
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r19
    h: b6b2c76459a7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Row only reports a digital input level change.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r19
    h: b6b2c76459a7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=138.r19
    h: b6b2c76459a7
  review: drafted
---
