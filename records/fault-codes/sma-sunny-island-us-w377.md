---
id: fc:sma-sunny-island-us-w377
type: FaultCode
name: SMA SI-US W377
aliases:
- W377
- w377
- SMA W377
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W377
code_key: w377
vendor_severity: '1'
page: 213
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r16
    h: c23dfc523647
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r16
    h: c23dfc523647
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-overcurrent
  note: Output current exceeds nominal grid or generator current on master
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r16
    h: c23dfc523647
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r16
    h: c23dfc523647
  review: drafted
---
