---
id: fc:sma-sunny-island-us-w882
type: FaultCode
name: SMA SI-US W882
aliases:
- W882
- w882
- SMA W882
- Battery overvoltage Sunny Island Charger 4
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W882
code_key: w882
display_message: Battery overvoltage Sunny Island Charger 4
vendor_severity: '1'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r6
    h: b6bbdd63ecc8
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r6
    h: b6bbdd63ecc8
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-overvoltage
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r6
    h: b6bbdd63ecc8
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:charge-controller
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r6
    h: b6bbdd63ecc8
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r6
    h: b6bbdd63ecc8
  review: drafted
---
