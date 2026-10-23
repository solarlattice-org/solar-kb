---
id: fc:sma-sunny-island-us-w347
type: FaultCode
name: SMA SI-US W347
aliases:
- W347
- w347
- SMA W347
- Disconnection from external source due to excessive load
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W347
code_key: w347
display_message: Disconnection from external source due to excessive load
vendor_severity: '1'
page: 213
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r8
    h: cca7c4b7d3a0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r8
    h: cca7c4b7d3a0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overload
  note: Excessive load causes disconnection from external source
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r8
    h: cca7c4b7d3a0
  review: drafted
---
