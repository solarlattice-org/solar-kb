---
id: fc:sma-sunny-island-us-f208
type: FaultCode
name: SMA SI-US F208
aliases:
- F208
- f208
- SMA F208
- Battery overvoltage error
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F208
code_key: f208
display_message: Battery overvoltage error
vendor_severity: '3'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r6
    h: 5fd46c8d9e47
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r6
    h: 5fd46c8d9e47
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-overvoltage
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r6
    h: 5fd46c8d9e47
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r6
    h: 5fd46c8d9e47
  review: drafted
---
