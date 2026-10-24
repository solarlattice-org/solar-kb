---
id: fc:sma-sunny-island-us-w864
type: FaultCode
name: SMA SI-US W864
aliases:
- W864
- w864
- SMA W864
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W864
code_key: w864
vendor_severity: '1'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r25
    h: 6d6e5dd54107
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r25
    h: 6d6e5dd54107
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:pv-input-abnormal
  note: No PV voltage present or short circuit on the PV input
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r25
    h: 6d6e5dd54107
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r25
    h: 6d6e5dd54107
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r25
    h: 6d6e5dd54107
  review: drafted
---
