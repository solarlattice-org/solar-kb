---
id: fc:sma-sunny-island-us-w350
type: FaultCode
name: SMA SI-US W350
aliases:
- W350
- w350
- SMA W350
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W350
code_key: w350
vendor_severity: '1'
page: 213
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r11
    h: 36c770b59c1e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r11
    h: 36c770b59c1e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overload
  note: Reported for slave 3
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r11
    h: 36c770b59c1e
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r11
    h: 36c770b59c1e
  review: drafted
---
