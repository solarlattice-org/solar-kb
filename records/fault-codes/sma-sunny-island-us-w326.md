---
id: fc:sma-sunny-island-us-w326
type: FaultCode
name: SMA SI-US W326
aliases:
- W326
- w326
- SMA W326
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W326
code_key: w326
vendor_severity: '1'
page: 212
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r7
    h: aff1aa9e6185
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r7
    h: aff1aa9e6185
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-underfrequency
  note: Seen at slave 3
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r7
    h: aff1aa9e6185
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Unit disconnects from the utility grid or generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r7
    h: aff1aa9e6185
  review: drafted
---
