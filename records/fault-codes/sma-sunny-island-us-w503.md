---
id: fc:sma-sunny-island-us-w503
type: FaultCode
name: SMA SI-US W503
aliases:
- W503
- w503
- SMA W503
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W503
code_key: w503
vendor_severity: '1'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r3
    h: e4c35145bbac
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r3
    h: e4c35145bbac
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-power-flow
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r3
    h: e4c35145bbac
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Quick grid disconnection on slave 2.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r3
    h: e4c35145bbac
  review: drafted
---
