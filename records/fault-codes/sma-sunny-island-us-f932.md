---
id: fc:sma-sunny-island-us-f932
type: FaultCode
name: SMA SI-US F932
aliases:
- F932
- f932
- SMA F932
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F932
code_key: f932
vendor_severity: '3'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r1
    h: e7e1a00b10f1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r1
    h: e7e1a00b10f1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-cell-imbalance
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r1
    h: e7e1a00b10f1
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r1
    h: e7e1a00b10f1
  review: drafted
---
