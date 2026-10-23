---
id: fc:sma-sunny-island-us-f141
type: FaultCode
name: SMA SI-US F141
aliases:
- F141
- f141
- SMA F141
- Inverter undervoltage
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F141
code_key: f141
display_message: Inverter undervoltage
vendor_severity: '2'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r21
    h: 4ed6fc38abf6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r21
    h: 4ed6fc38abf6
  review: drafted
---
