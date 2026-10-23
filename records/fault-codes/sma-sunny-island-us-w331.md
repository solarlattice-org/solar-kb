---
id: fc:sma-sunny-island-us-w331
type: FaultCode
name: SMA SI-US W331
aliases:
- W331
- w331
- SMA W331
- Disconnection from utility grid/generator due to islanding
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W331
code_key: w331
display_message: Disconnection from utility grid/generator due to islanding
vendor_severity: '1'
page: 212
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r12
    h: d8d1677d00cb
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r12
    h: d8d1677d00cb
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:islanding-detected
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r12
    h: d8d1677d00cb
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Unit disconnects from the utility grid or generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r12
    h: d8d1677d00cb
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
