---
id: fc:sma-sunny-island-us-w322
type: FaultCode
name: SMA SI-US W322
aliases:
- W322
- w322
- SMA W322
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W322
code_key: w322
vendor_severity: '1'
page: 212
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r3
    h: 62b7ac543a24
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r3
    h: 62b7ac543a24
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overvoltage
  note: Excessive external voltage seen at slave 3
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r3
    h: 62b7ac543a24
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Unit disconnects from the utility grid or generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r3
    h: 62b7ac543a24
  review: drafted
---
