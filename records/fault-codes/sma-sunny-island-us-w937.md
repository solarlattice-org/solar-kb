---
id: fc:sma-sunny-island-us-w937
type: FaultCode
name: SMA SI-US W937
aliases:
- W937
- w937
- SMA W937
- 'Warning via SiCom: Battery overvoltage'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W937
code_key: w937
display_message: 'Warning via SiCom: Battery overvoltage'
vendor_severity: '1'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r4
    h: 81514a4bc426
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r4
    h: 81514a4bc426
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-overvoltage
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r4
    h: 81514a4bc426
  review: drafted
---
