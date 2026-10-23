---
id: fc:sma-sunny-island-us-f721
type: FaultCode
name: SMA SI-US F721
aliases:
- F721
- f721
- SMA F721
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F721
code_key: f721
vendor_severity: '4'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r12
    h: 8b6de1b3e36a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r12
    h: 8b6de1b3e36a
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:temperature-sensor-fault
  note: Short circuit or open wire on the heat sink temperature sensor.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r12
    h: 8b6de1b3e36a
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r12
    h: 8b6de1b3e36a
  review: drafted
---
