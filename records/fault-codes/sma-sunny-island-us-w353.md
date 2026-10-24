---
id: fc:sma-sunny-island-us-w353
type: FaultCode
name: SMA SI-US W353
aliases:
- W353
- w353
- SMA W353
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W353
code_key: w353
vendor_severity: '1'
page: 213
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r14
    h: 3414e4c1677a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r14
    h: 3414e4c1677a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:external-short-circuit
  note: Reported for slave 2
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r14
    h: 3414e4c1677a
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r14
    h: 3414e4c1677a
  review: drafted
---
