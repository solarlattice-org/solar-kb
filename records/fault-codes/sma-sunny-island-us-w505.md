---
id: fc:sma-sunny-island-us-w505
type: FaultCode
name: SMA SI-US W505
aliases:
- W505
- w505
- SMA W505
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W505
code_key: w505
vendor_severity: '1'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r5
    h: 53a6bfdba95e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r5
    h: 53a6bfdba95e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-overcurrent
  note: Feed-in current exceeds configured nominal grid current.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r5
    h: 53a6bfdba95e
  review: drafted
---
