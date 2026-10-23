---
id: fc:sma-sunny-island-us-w502
type: FaultCode
name: SMA SI-US W502
aliases:
- W502
- w502
- SMA W502
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W502
code_key: w502
vendor_severity: '1'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r2
    h: 7db3efd539ae
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r2
    h: 7db3efd539ae
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-power-flow
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r2
    h: 7db3efd539ae
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Quick grid disconnection on slave 1.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r2
    h: 7db3efd539ae
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
