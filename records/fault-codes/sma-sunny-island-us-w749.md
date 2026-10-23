---
id: fc:sma-sunny-island-us-w749
type: FaultCode
name: SMA SI-US W749
aliases:
- W749
- w749
- SMA W749
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W749
code_key: w749
vendor_severity: '1'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r6
    h: 90fb78b43190
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r6
    h: 90fb78b43190
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r6
    h: 90fb78b43190
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:temperature-sensor
  note: Transformer temperature sensor of a slave device.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r6
    h: 90fb78b43190
  review: drafted
---
