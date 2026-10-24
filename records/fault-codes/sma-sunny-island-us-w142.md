---
id: fc:sma-sunny-island-us-w142
type: FaultCode
name: SMA SI-US W142
aliases:
- W142
- w142
- SMA W142
- Inverter undervoltage slave 1
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W142
code_key: w142
display_message: Inverter undervoltage slave 1
vendor_severity: '1'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r22
    h: 0e4bac8ce3b9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r22
    h: 0e4bac8ce3b9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-undervoltage
  note: Reported for slave device 1 in a multi-unit cluster.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r22
    h: 0e4bac8ce3b9
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r22
    h: 0e4bac8ce3b9
  review: drafted
---
