---
id: fc:sma-sunny-island-us-w380
type: FaultCode
name: SMA SI-US W380
aliases:
- W380
- w380
- SMA W380
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W380
code_key: w380
vendor_severity: '1'
page: 213
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r19
    h: 927903d76e79
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r19
    h: 927903d76e79
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-overcurrent
  note: Output current exceeds nominal grid or generator current on slave 3.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r19
    h: 927903d76e79
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r19
    h: 927903d76e79
  review: drafted
---
