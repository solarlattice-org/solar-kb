---
id: fc:sma-sunny-island-us-w944
type: FaultCode
name: SMA SI-US W944
aliases:
- W944
- w944
- SMA W944
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W944
code_key: w944
vendor_severity: '1'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r11
    h: 31317c5d1763
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r11
    h: 31317c5d1763
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-charge-overcurrent
  note: Applies while the battery is in charge mode.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r11
    h: 31317c5d1763
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
