---
id: fc:sma-sunny-island-us-w808
type: FaultCode
name: SMA SI-US W808
aliases:
- W808
- w808
- SMA W808
- Error Q4 contactor
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W808
code_key: w808
display_message: Error Q4 contactor
vendor_severity: '1'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r6
    h: b2dacde2489f
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r6
    h: b2dacde2489f
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:switch-status-fault
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r6
    h: b2dacde2489f
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-contactor
  note: Contactor designated Q4
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r6
    h: b2dacde2489f
  review: drafted
---
