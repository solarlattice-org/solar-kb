---
id: fc:sma-sunny-island-us-f605
type: FaultCode
name: SMA SI-US F605
aliases:
- F605
- f605
- SMA F605
- Transfer relay does not open
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F605
code_key: f605
display_message: Transfer relay does not open
vendor_severity: '4'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r1
    h: fa7b3187ba5b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r1
    h: fa7b3187ba5b
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r1
    h: fa7b3187ba5b
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:transfer-relay
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r1
    h: fa7b3187ba5b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
