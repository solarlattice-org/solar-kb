---
id: fc:sma-sunny-island-us-w865
type: FaultCode
name: SMA SI-US W865
aliases:
- W865
- w865
- SMA W865
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W865
code_key: w865
vendor_severity: '1'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r26
    h: a8b7ceb835d6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r26
    h: a8b7ceb835d6
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:abnormal-temperature-reading
  note: Covers a sensor error or an undertemperature condition
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r26
    h: a8b7ceb835d6
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:charge-controller
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r26
    h: a8b7ceb835d6
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r26
    h: a8b7ceb835d6
  review: drafted
---
