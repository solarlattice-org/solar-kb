---
id: fc:sma-sb-us-40-9003
type: FaultCode
name: SMA SB-US-40 9003
aliases:
- '9003'
- SMA 9003
- Grid parameter locked
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-40
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP/1TP-US-40)
code: '9003'
code_key: '9003'
display_message: Grid parameter locked
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-40-ba-en-13
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h251
    h: 4023f322ac7a
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h252
    h: 49fda73cc4d1
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:parameter-change-rejected
  note: Grid parameters are now locked against changes.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r3
    h: '7e7479893027'
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r3
    h: '7e7479893027'
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r3
    h: '7e7479893027'
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h252
    h: 49fda73cc4d1
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r1
    h: dca11bb38795
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:enter-access-code
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r3
    h: '7e7479893027'
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r3
    h: '7e7479893027'
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r3
    h: '7e7479893027'
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r1
    h: dca11bb38795
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h428
    h: d764b2ea748c
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:login-with-required-rights
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h428
    h: d764b2ea748c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h614
    h: 0b635057a69f
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h447
    h: d764b2ea748c
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r3
    h: '7e7479893027'
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r3
    h: '7e7479893027'
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r3
    h: '7e7479893027'
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h252
    h: 49fda73cc4d1
  review: drafted
---
