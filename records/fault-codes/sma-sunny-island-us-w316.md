---
id: fc:sma-sunny-island-us-w316
type: FaultCode
name: SMA SI-US W316
aliases:
- W316
- w316
- SMA W316
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W316
code_key: w316
vendor_severity: '1'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r7
    h: 401917ed01ed
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r7
    h: 401917ed01ed
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-undervoltage
  note: Reported for slave device 1.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r7
    h: 401917ed01ed
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r7
    h: 401917ed01ed
  review: drafted
---
