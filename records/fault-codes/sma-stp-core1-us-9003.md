---
id: fc:sma-stp-core1-us-9003
type: FaultCode
name: SMA CORE1-US 9003
aliases:
- '9003'
- SMA 9003
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '9003'
code_key: '9003'
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r3
    h: '7e7479893027'
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r3
    h: '7e7479893027'
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r3
    h: '7e7479893027'
  review: drafted
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
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
