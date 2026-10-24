---
id: fc:sma-sunny-island-us-w143
type: FaultCode
name: SMA SI-US W143
aliases:
- W143
- w143
- SMA W143
- Inverter undervoltage slave 2
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W143
code_key: w143
display_message: Inverter undervoltage slave 2
vendor_severity: '1'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r23
    h: 015c2a9367f7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r23
    h: 015c2a9367f7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-undervoltage
  note: Reported for slave device 2 in a multi-unit cluster.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r23
    h: 015c2a9367f7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r23
    h: 015c2a9367f7
  review: drafted
---
