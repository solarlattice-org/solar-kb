---
id: fc:sma-sunny-island-us-w874
type: FaultCode
name: SMA SI-US W874
aliases:
- W874
- w874
- SMA W874
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W874
code_key: w874
vendor_severity: '1'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r1
    h: 4d78b121f0d1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r1
    h: 4d78b121f0d1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:pv-input-abnormal
  note: Covers either missing PV voltage or a short circuit at the charger input.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r1
    h: 4d78b121f0d1
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:charge-controller
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r1
    h: 4d78b121f0d1
  review: drafted
---
