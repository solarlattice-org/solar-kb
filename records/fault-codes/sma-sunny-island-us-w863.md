---
id: fc:sma-sunny-island-us-w863
type: FaultCode
name: SMA SI-US W863
aliases:
- W863
- w863
- SMA W863
- Overvoltage PV array Sunny Island Charger 2
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W863
code_key: w863
display_message: Overvoltage PV array Sunny Island Charger 2
vendor_severity: '1'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r24
    h: f59494ebbec1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r24
    h: f59494ebbec1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  note: Overvoltage on the PV array input
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r24
    h: f59494ebbec1
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r24
    h: f59494ebbec1
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r24
    h: f59494ebbec1
  review: drafted
---
