---
id: fc:sma-sunny-island-us-e119
type: FaultCode
name: SMA SI-US E119
aliases:
- E119
- e119
- SMA E119
- Manual start (transition from standby mode to operation)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E119
code_key: e119
display_message: Manual start (transition from standby mode to operation)
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r6
    h: 9904e47606f2
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: 'Status message: manual transition from standby to operation.'
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r6
    h: 9904e47606f2
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
