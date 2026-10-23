---
id: fc:sma-sunny-island-us-w760
type: FaultCode
name: SMA SI-US W760
aliases:
- W760
- w760
- SMA W760
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W760
code_key: w760
vendor_severity: '1'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r17
    h: 6f2bac753cf5
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r17
    h: 6f2bac753cf5
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:no-output-voltage
  note: Applies to slave 2 of the main cluster
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r17
    h: 6f2bac753cf5
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
