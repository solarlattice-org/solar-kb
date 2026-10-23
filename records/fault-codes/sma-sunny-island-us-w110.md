---
id: fc:sma-sunny-island-us-w110
type: FaultCode
name: SMA SI-US W110
aliases:
- W110
- w110
- SMA W110
- Overtemperature transformer slave 1
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W110
code_key: w110
display_message: Overtemperature transformer slave 1
vendor_severity: '1'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r2
    h: 35bb5dd7dc92
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r2
    h: 35bb5dd7dc92
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  note: Transformer overtemperature reported on slave device 1.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r2
    h: 35bb5dd7dc92
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:transformer
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r2
    h: 35bb5dd7dc92
  review: drafted
---
