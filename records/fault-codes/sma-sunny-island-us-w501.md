---
id: fc:sma-sunny-island-us-w501
type: FaultCode
name: SMA SI-US W501
aliases:
- W501
- w501
- SMA W501
- Grid reverse current prevented (quick grid disconnection)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W501
code_key: w501
display_message: Grid reverse current prevented (quick grid disconnection)
vendor_severity: '1'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r1
    h: 7b71fe3480c9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r1
    h: 7b71fe3480c9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-power-flow
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r1
    h: 7b71fe3480c9
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Quick disconnection from the grid prevents reverse current.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r1
    h: 7b71fe3480c9
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r1
    h: 7b71fe3480c9
  review: drafted
---
