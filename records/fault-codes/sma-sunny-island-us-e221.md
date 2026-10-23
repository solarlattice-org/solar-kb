---
id: fc:sma-sunny-island-us-e221
type: FaultCode
name: SMA SI-US E221
aliases:
- E221
- e221
- SMA E221
- Status change battery-preservation mode level 1
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E221
code_key: e221
display_message: Status change battery-preservation mode level 1
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r7
    h: 12fd9fe3ef03
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Battery preservation mode status change event
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r7
    h: 12fd9fe3ef03
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
---
