---
id: fc:sma-sunny-island-us-f206
type: FaultCode
name: SMA SI-US F206
aliases:
- F206
- f206
- SMA F206
- Battery overtemperature
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F206
code_key: f206
display_message: Battery overtemperature
vendor_severity: '3'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r5
    h: 740eb7c94729
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r5
    h: 740eb7c94729
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r5
    h: 740eb7c94729
  review: drafted
---
