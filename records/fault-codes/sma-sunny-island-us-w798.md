---
id: fc:sma-sunny-island-us-w798
type: FaultCode
name: SMA SI-US W798
aliases:
- W798
- w798
- SMA W798
- Failure of the grid monitoring slave 2
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W798
code_key: w798
display_message: Failure of the grid monitoring slave 2
vendor_severity: '1'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r29
    h: ae70d7a84271
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r29
    h: ae70d7a84271
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-monitoring-failure
  note: Slave device 2 of the cluster
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r29
    h: ae70d7a84271
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r29
    h: ae70d7a84271
  review: drafted
---
