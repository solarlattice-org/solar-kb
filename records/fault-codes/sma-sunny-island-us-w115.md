---
id: fc:sma-sunny-island-us-w115
type: FaultCode
name: SMA SI-US W115
aliases:
- W115
- w115
- SMA W115
- Overtemperature heat sink slave 2
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W115
code_key: w115
display_message: Overtemperature heat sink slave 2
vendor_severity: '1'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r7
    h: 1ec4808c40c4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r7
    h: 1ec4808c40c4
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  note: Heat sink overtemperature on slave device 2.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r7
    h: 1ec4808c40c4
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:heat-sink
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r7
    h: 1ec4808c40c4
  review: drafted
---
