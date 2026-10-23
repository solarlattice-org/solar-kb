---
id: fc:sma-sunny-island-us-w340
type: FaultCode
name: SMA SI-US W340
aliases:
- W340
- w340
- SMA W340
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W340
code_key: w340
vendor_severity: '1'
page: 213
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r1
    h: 90da4da0b90b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r1
    h: 90da4da0b90b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overvoltage
  note: Voltage increase protection on slave 1
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r1
    h: 90da4da0b90b
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Disconnects from utility grid or generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r1
    h: 90da4da0b90b
  review: drafted
---
