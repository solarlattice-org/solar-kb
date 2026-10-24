---
id: fc:sma-sunny-island-us-w209
type: FaultCode
name: SMA SI-US W209
aliases:
- W209
- w209
- SMA W209
- Battery overvoltage error
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W209
code_key: w209
display_message: Battery overvoltage error
vendor_severity: '1'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r7
    h: 736a37a25fc3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r7
    h: 736a37a25fc3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-overvoltage
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r7
    h: 736a37a25fc3
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r7
    h: 736a37a25fc3
  review: drafted
---
