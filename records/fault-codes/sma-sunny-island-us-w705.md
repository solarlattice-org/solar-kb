---
id: fc:sma-sunny-island-us-w705
type: FaultCode
name: SMA SI-US W705
aliases:
- W705
- w705
- SMA W705
- Watchdog DSP has been tripped
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W705
code_key: w705
display_message: Watchdog DSP has been tripped
vendor_severity: '1'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=150.r4
    h: 6b0ecd6c39ce
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=150.r4
    h: 6b0ecd6c39ce
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:digital-signal-processor
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=150.r4
    h: 6b0ecd6c39ce
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=150.r4
    h: 6b0ecd6c39ce
  review: drafted
---
