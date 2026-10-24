---
id: fc:sma-sb-us-40-7351
type: FaultCode
name: SMA SB-US-40 7351
aliases:
- '7351'
- SMA 7351
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-40
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP/1TP-US-40)
code: '7351'
code_key: '7351'
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-40-ba-en-13
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=19.r2
    h: 576c7d273e37
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r3
    h: fb36bcc7e0da
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r3
    h: fb36bcc7e0da
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=19.r2
    h: 576c7d273e37
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:wifi-module
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r3
    h: fb36bcc7e0da
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r3
    h: fb36bcc7e0da
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=19.r2
    h: 576c7d273e37
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sb-us-40
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=19.r2
    h: 576c7d273e37
  review: drafted
---
