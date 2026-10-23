---
id: fc:sma-sunny-island-us-w402
type: FaultCode
name: SMA SI-US W402
aliases:
- W402
- w402
- SMA W402
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W402
code_key: w402
vendor_severity: '1'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=147.r2
    h: 0761d5d81f87
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=147.r2
    h: 0761d5d81f87
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:generator-locked-error
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=147.r2
    h: 0761d5d81f87
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:backup-generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=147.r2
    h: 0761d5d81f87
  review: drafted
---
