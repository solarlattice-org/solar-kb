---
id: fc:sma-sunny-island-us-w886
type: FaultCode
name: SMA SI-US W886
aliases:
- W886
- w886
- SMA W886
- Overtemperature Sunny Island Charger 4
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W886
code_key: w886
display_message: Overtemperature Sunny Island Charger 4
vendor_severity: '1'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r10
    h: 2e744a077eff
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r10
    h: 2e744a077eff
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:charge-controller-overtemperature
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r10
    h: 2e744a077eff
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:charge-controller
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r10
    h: 2e744a077eff
  review: drafted
---
