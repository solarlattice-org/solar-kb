---
id: fc:sma-sunny-island-us-e222
type: FaultCode
name: SMA SI-US E222
aliases:
- E222
- e222
- SMA E222
- Status change battery-preservation mode level 2
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E222
code_key: e222
display_message: Status change battery-preservation mode level 2
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r8
    h: 4672e0a736bb
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Battery preservation mode status change event
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r8
    h: 4672e0a736bb
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r8
    h: 4672e0a736bb
  review: drafted
---
