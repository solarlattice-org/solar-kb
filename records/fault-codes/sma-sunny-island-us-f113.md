---
id: fc:sma-sunny-island-us-f113
type: FaultCode
name: SMA SI-US F113
aliases:
- F113
- f113
- SMA F113
- Overtemperature heat sink
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F113
code_key: f113
display_message: Overtemperature heat sink
vendor_severity: '3'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r5
    h: ad3199b459e5
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r5
    h: ad3199b459e5
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r5
    h: ad3199b459e5
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:heat-sink
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r5
    h: ad3199b459e5
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r5
    h: ad3199b459e5
  review: drafted
---
