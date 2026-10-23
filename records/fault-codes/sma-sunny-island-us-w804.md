---
id: fc:sma-sunny-island-us-w804
type: FaultCode
name: SMA SI-US W804
aliases:
- W804
- w804
- SMA W804
- Grid operation not possible
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W804
code_key: w804
display_message: Grid operation not possible
vendor_severity: '1'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r2
    h: d7c0d7ac6709
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r2
    h: d7c0d7ac6709
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:operation-inhibited
  note: Applies to grid operation mode
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r2
    h: d7c0d7ac6709
  review: drafted
---
