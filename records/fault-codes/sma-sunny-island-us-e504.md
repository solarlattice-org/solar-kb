---
id: fc:sma-sunny-island-us-e504
type: FaultCode
name: SMA SI-US E504
aliases:
- E504
- e504
- SMA E504
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E504
code_key: e504
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r4
    h: 408f8dd71fb0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Grid released because power falls below the set limit.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r4
    h: 408f8dd71fb0
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r4
    h: 408f8dd71fb0
  review: drafted
---
