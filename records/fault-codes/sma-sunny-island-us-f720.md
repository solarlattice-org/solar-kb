---
id: fc:sma-sunny-island-us-f720
type: FaultCode
name: SMA SI-US F720
aliases:
- F720
- f720
- SMA F720
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F720
code_key: f720
vendor_severity: '4'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r11
    h: 3efdf63743b5
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r11
    h: 3efdf63743b5
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:temperature-sensor-fault
  note: Short circuit or open wire on the transformer temperature sensor.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r11
    h: 3efdf63743b5
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r11
    h: 3efdf63743b5
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r11
    h: 3efdf63743b5
  review: drafted
---
