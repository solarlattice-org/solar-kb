---
id: fc:sma-sunny-island-us-e223
type: FaultCode
name: SMA SI-US E223
aliases:
- E223
- e223
- SMA E223
- Status change battery-preservation mode level 3
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E223
code_key: e223
display_message: Status change battery-preservation mode level 3
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r9
    h: 791f3d9625cf
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Battery preservation mode status change event
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r9
    h: 791f3d9625cf
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r9
    h: 791f3d9625cf
  review: drafted
---
