---
id: fc:sma-sunny-island-us-w948
type: FaultCode
name: SMA SI-US W948
aliases:
- W948
- w948
- SMA W948
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W948
code_key: w948
vendor_severity: '1'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r15
    h: 9fc3a00f4839
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r15
    h: 9fc3a00f4839
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-cell-imbalance
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r15
    h: 9fc3a00f4839
  review: drafted
---
