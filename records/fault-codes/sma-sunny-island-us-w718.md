---
id: fc:sma-sunny-island-us-w718
type: FaultCode
name: SMA SI-US W718
aliases:
- W718
- w718
- SMA W718
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W718
code_key: w718
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r9
    h: 0bc244de8340
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r9
    h: 0bc244de8340
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-voltage-out-of-range
  note: Reported for slave device 2.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r9
    h: 0bc244de8340
  review: drafted
---
