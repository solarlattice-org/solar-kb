---
id: fc:sma-sunny-island-us-e707
type: FaultCode
name: SMA SI-US E707
aliases:
- E707
- e707
- SMA E707
- New system configured in QCG
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E707
code_key: e707
display_message: New system configured in QCG
page: 208
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=139.r3
    h: 88ac6f692635
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Event row reporting a configuration status, not a fault or warning.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=139.r3
    h: 88ac6f692635
  review: drafted
---
