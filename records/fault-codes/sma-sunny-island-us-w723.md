---
id: fc:sma-sunny-island-us-w723
type: FaultCode
name: SMA SI-US W723
aliases:
- W723
- w723
- SMA W723
- Cable break on battery temperature sensor
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W723
code_key: w723
display_message: Cable break on battery temperature sensor
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r14
    h: 790781dbcf50
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r14
    h: 790781dbcf50
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:temperature-sensor-fault
  note: Open wire on the battery temperature sensor.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r14
    h: 790781dbcf50
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r14
    h: 790781dbcf50
  review: drafted
---
