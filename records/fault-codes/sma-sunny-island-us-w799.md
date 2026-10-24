---
id: fc:sma-sunny-island-us-w799
type: FaultCode
name: SMA SI-US W799
aliases:
- W799
- w799
- SMA W799
- Failure of the grid monitoring slave 3
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W799
code_key: w799
display_message: Failure of the grid monitoring slave 3
vendor_severity: '1'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r30
    h: 525853dc4d98
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r30
    h: 525853dc4d98
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-monitoring-failure
  note: Slave device 3 of the cluster
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r30
    h: 525853dc4d98
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r30
    h: 525853dc4d98
  review: drafted
---
