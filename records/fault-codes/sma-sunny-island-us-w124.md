---
id: fc:sma-sunny-island-us-w124
type: FaultCode
name: SMA SI-US W124
aliases:
- W124
- w124
- SMA W124
- Inverter overvoltage slave 3
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W124
code_key: w124
display_message: Inverter overvoltage slave 3
vendor_severity: '1'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r16
    h: 5dc8ca753f31
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r16
    h: 5dc8ca753f31
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overvoltage
  note: Reported for slave device 3 in a multi-unit cluster.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r16
    h: 5dc8ca753f31
  review: drafted
---
