---
id: fc:sma-sunny-island-us-w504
type: FaultCode
name: SMA SI-US W504
aliases:
- W504
- w504
- SMA W504
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W504
code_key: w504
vendor_severity: '1'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r4
    h: 255ce066f3fd
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r4
    h: 255ce066f3fd
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-power-flow
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r4
    h: 255ce066f3fd
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Quick grid disconnection on slave 3.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r4
    h: 255ce066f3fd
  review: drafted
---
