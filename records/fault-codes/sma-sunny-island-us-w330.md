---
id: fc:sma-sunny-island-us-w330
type: FaultCode
name: SMA SI-US W330
aliases:
- W330
- w330
- SMA W330
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W330
code_key: w330
vendor_severity: '1'
page: 212
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r11
    h: 01d3702ae4d2
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r11
    h: 01d3702ae4d2
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overfrequency
  note: Seen at slave 3
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r11
    h: 01d3702ae4d2
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Unit disconnects from the utility grid or generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=145.r11
    h: 01d3702ae4d2
  review: drafted
---
