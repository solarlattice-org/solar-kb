---
id: fc:sma-sunny-island-us-w342
type: FaultCode
name: SMA SI-US W342
aliases:
- W342
- w342
- SMA W342
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W342
code_key: w342
vendor_severity: '1'
page: 213
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r3
    h: 2c6f4f0303a4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r3
    h: 2c6f4f0303a4
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overvoltage
  note: Voltage increase protection on slave 3
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r3
    h: 2c6f4f0303a4
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Disconnects from utility grid or generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r3
    h: 2c6f4f0303a4
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r3
    h: 2c6f4f0303a4
  review: drafted
---
