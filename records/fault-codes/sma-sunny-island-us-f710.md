---
id: fc:sma-sunny-island-us-f710
type: FaultCode
name: SMA SI-US F710
aliases:
- F710
- f710
- SMA F710
- Autostart meter elapsed (several autostarts in succession)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F710
code_key: f710
display_message: Autostart meter elapsed (several autostarts in succession)
vendor_severity: '4'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r5
    h: 1361ad045a3e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r5
    h: 1361ad045a3e
  review: drafted
---
