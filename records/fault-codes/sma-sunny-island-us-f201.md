---
id: fc:sma-sunny-island-us-f201
type: FaultCode
name: SMA SI-US F201
aliases:
- F201
- f201
- SMA F201
- Measuring range of battery voltage exceeded
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F201
code_key: f201
display_message: Measuring range of battery voltage exceeded
vendor_severity: '2'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r1
    h: 02a0d3b727a9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r1
    h: 02a0d3b727a9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-voltage-out-of-range
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r1
    h: 02a0d3b727a9
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r1
    h: 02a0d3b727a9
  review: drafted
---
