---
id: fc:sma-sunny-island-us-w334
type: FaultCode
name: SMA SI-US W334
aliases:
- W334
- w334
- SMA W334
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W334
code_key: w334
vendor_severity: '1'
page: 212
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r15
    h: 312cdad7dcb8
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r15
    h: 312cdad7dcb8
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:islanding-detected
  note: Reported for slave unit 3
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r15
    h: 312cdad7dcb8
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Disconnects from utility grid or generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r15
    h: 312cdad7dcb8
  review: drafted
---
