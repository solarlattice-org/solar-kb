---
id: fc:sma-sunny-island-us-w507
type: FaultCode
name: SMA SI-US W507
aliases:
- W507
- w507
- SMA W507
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W507
code_key: w507
vendor_severity: '1'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r7
    h: 06c5f773245a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r7
    h: 06c5f773245a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-overcurrent
  note: Feed-in current exceeds configured nominal grid current on slave 2.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r7
    h: 06c5f773245a
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r7
    h: 06c5f773245a
  review: drafted
---
