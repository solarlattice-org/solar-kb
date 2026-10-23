---
id: fc:sma-sunny-island-us-w336
type: FaultCode
name: SMA SI-US W336
aliases:
- W336
- w336
- SMA W336
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W336
code_key: w336
vendor_severity: '1'
page: 212
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r17
    h: 95895f8b515d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r17
    h: 95895f8b515d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-voltage-out-of-range
  note: Slave 1, redundant voltage measurement
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r17
    h: 95895f8b515d
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Disconnects from utility grid or generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r17
    h: 95895f8b515d
  review: drafted
---
