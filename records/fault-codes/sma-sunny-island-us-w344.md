---
id: fc:sma-sunny-island-us-w344
type: FaultCode
name: SMA SI-US W344
aliases:
- W344
- w344
- SMA W344
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W344
code_key: w344
vendor_severity: '1'
page: 213
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r5
    h: 90b04feb72eb
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r5
    h: 90b04feb72eb
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: Disconnects from the external source
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r5
    h: 90b04feb72eb
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r5
    h: 90b04feb72eb
  review: drafted
---
