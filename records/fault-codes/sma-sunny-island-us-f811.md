---
id: fc:sma-sunny-island-us-f811
type: FaultCode
name: SMA SI-US F811
aliases:
- F811
- f811
- SMA F811
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F811
code_key: f811
vendor_severity: '4'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r9
    h: 278572668d1d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r9
    h: 278572668d1d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:supply-voltage-invalid
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r9
    h: 278572668d1d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: indicates
  target: fm:internal-power-supply-fault
  note: 24 V supply of the Multicluster Box.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r9
    h: 278572668d1d
  review: drafted
---
