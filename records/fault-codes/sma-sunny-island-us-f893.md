---
id: fc:sma-sunny-island-us-f893
type: FaultCode
name: SMA SI-US F893
aliases:
- F893
- f893
- SMA F893
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F893
code_key: f893
vendor_severity: '2'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r15
    h: 5860f9c7d03c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r15
    h: 5860f9c7d03c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:measurement-signal-error
  note: Applies to Multicluster Box slave 3
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r15
    h: 5860f9c7d03c
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r15
    h: 5860f9c7d03c
  review: drafted
---
