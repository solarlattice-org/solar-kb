---
id: fc:sma-sunny-island-us-f817
type: FaultCode
name: SMA SI-US F817
aliases:
- F817
- f817
- SMA F817
- Error Q9 contactor
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F817
code_key: f817
display_message: Error Q9 contactor
vendor_severity: '4'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r12
    h: 9f8f6f22eb0d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r12
    h: 9f8f6f22eb0d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:switch-status-fault
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r12
    h: 9f8f6f22eb0d
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-contactor
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r12
    h: 9f8f6f22eb0d
  review: drafted
---
