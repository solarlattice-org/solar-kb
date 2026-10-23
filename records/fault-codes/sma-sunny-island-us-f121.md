---
id: fc:sma-sunny-island-us-f121
type: FaultCode
name: SMA SI-US F121
aliases:
- F121
- f121
- SMA F121
- Inverter overvoltage
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F121
code_key: f121
display_message: Inverter overvoltage
vendor_severity: '3'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r13
    h: 53e57360043a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r13
    h: 53e57360043a
  review: drafted
---
