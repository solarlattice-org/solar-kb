---
id: fc:sma-sunny-island-us-w315
type: FaultCode
name: SMA SI-US W315
aliases:
- W315
- w315
- SMA W315
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W315
code_key: w315
vendor_severity: '1'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r6
    h: bbfb9d2158da
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r6
    h: bbfb9d2158da
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-undervoltage
  note: Insufficient voltage from utility grid or generator.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r6
    h: bbfb9d2158da
  review: drafted
---
