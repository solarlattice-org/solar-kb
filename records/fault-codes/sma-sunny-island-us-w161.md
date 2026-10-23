---
id: fc:sma-sunny-island-us-w161
type: FaultCode
name: SMA SI-US W161
aliases:
- W161
- w161
- SMA W161
- Voltage on output AC1 slave 3
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W161
code_key: w161
display_message: Voltage on output AC1 slave 3
vendor_severity: '1'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r28
    h: dd346c648cd6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r28
    h: dd346c648cd6
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-output-voltage-present
  note: Reported for slave 3
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r28
    h: dd346c648cd6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
