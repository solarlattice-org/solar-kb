---
id: fc:sma-sunny-island-us-e130
type: FaultCode
name: SMA SI-US E130
aliases:
- E130
- e130
- SMA E130
- External stop (remote)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E130
code_key: e130
display_message: External stop (remote)
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r11
    h: daa2b2c8cbd0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: 'Status message: remote external stop.'
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r11
    h: daa2b2c8cbd0
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r11
    h: daa2b2c8cbd0
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:remote-shutdown
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r11
    h: daa2b2c8cbd0
  review: drafted
---
