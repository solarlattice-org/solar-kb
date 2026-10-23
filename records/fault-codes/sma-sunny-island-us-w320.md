---
id: fc:sma-sunny-island-us-w320
type: FaultCode
name: SMA SI-US W320
aliases:
- W320
- w320
- SMA W320
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W320
code_key: w320
vendor_severity: '1'
page: 212
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r1
    h: 34e9d81d854a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r1
    h: 34e9d81d854a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overvoltage
  note: Reported for slave device 1.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r1
    h: 34e9d81d854a
  review: drafted
---
