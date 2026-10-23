---
id: fc:sma-sunny-island-us-w871
type: FaultCode
name: SMA SI-US W871
aliases:
- W871
- w871
- SMA W871
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W871
code_key: w871
vendor_severity: '1'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r29
    h: 737ffee60d2c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r29
    h: 737ffee60d2c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  note: Battery-side reverse connection; alternative cause is a short circuit
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r29
    h: 737ffee60d2c
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:external-short-circuit
  note: Short circuit on the battery side of the charger
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r29
    h: 737ffee60d2c
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:charge-controller
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r29
    h: 737ffee60d2c
  review: drafted
---
