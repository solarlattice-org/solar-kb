---
id: fc:sma-sunny-island-us-f213
type: FaultCode
name: SMA SI-US F213
aliases:
- F213
- f213
- SMA F213
- Warning low battery voltage
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F213
code_key: f213
display_message: Warning low battery voltage
vendor_severity: '2'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r11
    h: d81b14bc6a1e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r11
    h: d81b14bc6a1e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-undervoltage
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r11
    h: d81b14bc6a1e
  review: drafted
---
