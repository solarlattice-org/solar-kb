---
id: fc:sma-sunny-island-us-w351
type: FaultCode
name: SMA SI-US W351
aliases:
- W351
- w351
- SMA W351
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W351
code_key: w351
vendor_severity: '1'
page: 213
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r12
    h: 6782d0b01756
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r12
    h: 6782d0b01756
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:external-short-circuit
  note: Short circuit causes disconnection from external source
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r12
    h: 6782d0b01756
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r12
    h: 6782d0b01756
  review: drafted
---
