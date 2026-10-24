---
id: fc:sma-sb-us-41-7113
type: FaultCode
name: SMA SB-US-41 7113
aliases:
- '7113'
- SMA 7113
- The memory card is full or write-protected
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '7113'
code_key: '7113'
display_message: The memory card is full or write-protected
page: 63
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.40
    h: 0e685377683a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h340
    h: 8d2aa30d76e6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:memory-card-unwritable
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r8
    h: fa5d00a293af
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r8
    h: fa5d00a293af
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r8
    h: fa5d00a293af
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h340
    h: 8d2aa30d76e6
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sb-us-41
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.40
    h: 0e685377683a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h340
    h: 8d2aa30d76e6
  review: drafted
---
