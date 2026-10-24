---
id: fc:sma-sunny-island-us-w112
type: FaultCode
name: SMA SI-US W112
aliases:
- W112
- w112
- SMA W112
- Overtemperature transformer slave 3
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W112
code_key: w112
display_message: Overtemperature transformer slave 3
vendor_severity: '1'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r4
    h: 4a403adcdd35
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r4
    h: 4a403adcdd35
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  note: Transformer overtemperature reported on slave device 3.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r4
    h: 4a403adcdd35
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:transformer
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r4
    h: 4a403adcdd35
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r4
    h: 4a403adcdd35
  review: drafted
---
