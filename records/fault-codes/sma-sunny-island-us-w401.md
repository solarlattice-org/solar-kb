---
id: fc:sma-sunny-island-us-w401
type: FaultCode
name: SMA SI-US W401
aliases:
- W401
- w401
- SMA W401
- Reverse power protection (generator)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W401
code_key: w401
display_message: Reverse power protection (generator)
vendor_severity: '1'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=147.r1
    h: fc5f1fabb9eb
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=147.r1
    h: fc5f1fabb9eb
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-power-flow
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=147.r1
    h: fc5f1fabb9eb
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:backup-generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=147.r1
    h: fc5f1fabb9eb
  review: drafted
---
