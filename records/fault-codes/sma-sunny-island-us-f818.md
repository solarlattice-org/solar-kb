---
id: fc:sma-sunny-island-us-f818
type: FaultCode
name: SMA SI-US F818
aliases:
- F818
- f818
- SMA F818
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F818
code_key: f818
vendor_severity: '4'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r13
    h: 799888e003c7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r13
    h: 799888e003c7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:phase-loss
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r13
    h: 799888e003c7
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Multicluster Box enters failure status when a phase is missing.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r13
    h: 799888e003c7
  review: drafted
  review_note: 'support check: partial - Goes into Failure status suggests stop, but trip/production stop
    is not explicitly stated.'
---
