---
id: fc:sma-sunny-island-us-f314
type: FaultCode
name: SMA SI-US F314
aliases:
- F314
- f314
- SMA F314
- External voltage failure
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F314
code_key: f314
display_message: External voltage failure
vendor_severity: '2'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r5
    h: a0e4b36670f0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r5
    h: a0e4b36670f0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-loss
  note: External source is utility grid or generator.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r5
    h: a0e4b36670f0
  review: drafted
  review_note: 'support check: partial - F314 ''External voltage failure'' supports grid loss loosely,
    but the note about the source being utility grid or generator is…'
---
