---
id: fc:sma-sunny-island-us-w508
type: FaultCode
name: SMA SI-US W508
aliases:
- W508
- w508
- SMA W508
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W508
code_key: w508
vendor_severity: '1'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r8
    h: d1cb3b779ecf
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r8
    h: d1cb3b779ecf
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-overcurrent
  note: Feed-in current exceeds configured nominal grid current on slave 3.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r8
    h: d1cb3b779ecf
  review: drafted
---
