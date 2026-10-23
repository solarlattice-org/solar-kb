---
id: fc:sma-sunny-island-us-f892
type: FaultCode
name: SMA SI-US F892
aliases:
- F892
- f892
- SMA F892
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F892
code_key: f892
vendor_severity: '2'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r14
    h: f1395dfd5d1b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r14
    h: f1395dfd5d1b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:measurement-signal-error
  note: Applies to Multicluster Box slave 2
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r14
    h: f1395dfd5d1b
  review: drafted
---
