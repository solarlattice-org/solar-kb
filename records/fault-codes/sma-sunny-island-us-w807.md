---
id: fc:sma-sunny-island-us-w807
type: FaultCode
name: SMA SI-US W807
aliases:
- W807
- w807
- SMA W807
- No valid line voltage for requested grid operation
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W807
code_key: w807
display_message: No valid line voltage for requested grid operation
vendor_severity: '1'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r5
    h: aaa823bc4da7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r5
    h: aaa823bc4da7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-voltage-out-of-range
  note: No valid line voltage when grid operation is requested
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r5
    h: aaa823bc4da7
  review: drafted
---
