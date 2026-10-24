---
id: fc:sma-sunny-island-us-f891
type: FaultCode
name: SMA SI-US F891
aliases:
- F891
- f891
- SMA F891
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F891
code_key: f891
vendor_severity: '2'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r13
    h: 62109eec33ea
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r13
    h: 62109eec33ea
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:measurement-signal-error
  note: Applies to Multicluster Box slave 1
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r13
    h: 62109eec33ea
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r13
    h: 62109eec33ea
  review: drafted
---
