---
id: fc:sma-sunny-island-us-w203
type: FaultCode
name: SMA SI-US W203
aliases:
- W203
- w203
- SMA W203
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W203
code_key: w203
vendor_severity: '1'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r3
    h: 4cdec74be5c7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r3
    h: 4cdec74be5c7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-voltage-out-of-range
  note: Reported for slave 2
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r3
    h: 4cdec74be5c7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
