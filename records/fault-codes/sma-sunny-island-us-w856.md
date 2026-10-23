---
id: fc:sma-sunny-island-us-w856
type: FaultCode
name: SMA SI-US W856
aliases:
- W856
- w856
- SMA W856
- Overtemperature Sunny Island Charger 1
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W856
code_key: w856
display_message: Overtemperature Sunny Island Charger 1
vendor_severity: '1'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r20
    h: 22318508d624
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r20
    h: 22318508d624
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:charge-controller-overtemperature
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r20
    h: 22318508d624
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:charge-controller
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r20
    h: 22318508d624
  review: drafted
---
