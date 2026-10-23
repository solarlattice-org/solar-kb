---
id: fc:sma-sunny-island-us-w805
type: FaultCode
name: SMA SI-US W805
aliases:
- W805
- w805
- SMA W805
- Generator operation not possible
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W805
code_key: w805
display_message: Generator operation not possible
vendor_severity: '1'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r3
    h: d7e96c7a21f6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r3
    h: d7e96c7a21f6
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:operation-inhibited
  note: Applies to generator operation mode
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r3
    h: d7e96c7a21f6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:backup-generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r3
    h: d7e96c7a21f6
  review: drafted
  review_note: 'support check: partial - Passage says generator operation not possible but does not state
    the backup generator component is affected, though implied.'
---
