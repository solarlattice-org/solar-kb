---
id: fc:sma-sunny-island-us-w138
type: FaultCode
name: SMA SI-US W138
aliases:
- W138
- w138
- SMA W138
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W138
code_key: w138
vendor_severity: '1'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r18
    h: 23942651ea7d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r18
    h: 23942651ea7d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-power-derating
  note: Reported for slave device 1.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r18
    h: 23942651ea7d
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r18
    h: 23942651ea7d
  review: drafted
  review_note: 'support check: partial - Temperature derating implies overtemperature but it isn''t stated
    explicitly.'
- claim_id: c5
  rel: affects
  target: comp:heat-sink
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r18
    h: 23942651ea7d
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:transformer
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r18
    h: 23942651ea7d
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:derate
  note: No reduced-output value is given.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r18
    h: 23942651ea7d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
