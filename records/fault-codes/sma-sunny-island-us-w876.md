---
id: fc:sma-sunny-island-us-w876
type: FaultCode
name: SMA SI-US W876
aliases:
- W876
- w876
- SMA W876
- Overtemperature Sunny Island Charger 3
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W876
code_key: w876
display_message: Overtemperature Sunny Island Charger 3
vendor_severity: '1'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r3
    h: 14100a3d1fb2
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r3
    h: 14100a3d1fb2
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:charge-controller-overtemperature
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r3
    h: 14100a3d1fb2
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:charge-controller
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r3
    h: 14100a3d1fb2
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
