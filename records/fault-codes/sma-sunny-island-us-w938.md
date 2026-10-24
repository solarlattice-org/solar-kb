---
id: fc:sma-sunny-island-us-w938
type: FaultCode
name: SMA SI-US W938
aliases:
- W938
- w938
- SMA W938
- 'Warning via SiCom: Battery undervoltage'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W938
code_key: w938
display_message: 'Warning via SiCom: Battery undervoltage'
vendor_severity: '1'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r5
    h: a1d54c6223cc
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r5
    h: a1d54c6223cc
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-undervoltage
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r5
    h: a1d54c6223cc
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r5
    h: a1d54c6223cc
  review: drafted
---
