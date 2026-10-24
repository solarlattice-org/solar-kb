---
id: fc:sma-sunny-island-us-w335
type: FaultCode
name: SMA SI-US W335
aliases:
- W335
- w335
- SMA W335
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W335
code_key: w335
vendor_severity: '1'
page: 212
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r16
    h: ba0e3343b825
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r16
    h: ba0e3343b825
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-voltage-out-of-range
  note: Detected by redundant voltage measurement
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r16
    h: ba0e3343b825
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Disconnects from utility grid or generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r16
    h: ba0e3343b825
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r16
    h: ba0e3343b825
  review: drafted
---
