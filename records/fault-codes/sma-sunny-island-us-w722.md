---
id: fc:sma-sunny-island-us-w722
type: FaultCode
name: SMA SI-US W722
aliases:
- W722
- w722
- SMA W722
- Short circuit on battery temperature sensor
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W722
code_key: w722
display_message: Short circuit on battery temperature sensor
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r13
    h: 2a1a56735c83
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r13
    h: 2a1a56735c83
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:temperature-sensor-fault
  note: Short circuit on the battery temperature sensor.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r13
    h: 2a1a56735c83
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r13
    h: 2a1a56735c83
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r13
    h: 2a1a56735c83
  review: drafted
---
