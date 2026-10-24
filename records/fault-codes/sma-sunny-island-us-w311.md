---
id: fc:sma-sunny-island-us-w311
type: FaultCode
name: SMA SI-US W311
aliases:
- W311
- w311
- SMA W311
- Relay protection slave 2
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W311
code_key: w311
display_message: Relay protection slave 2
vendor_severity: '1'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r3
    h: 3601edbd4aa7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r3
    h: 3601edbd4aa7
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r3
    h: 3601edbd4aa7
  review: drafted
---
