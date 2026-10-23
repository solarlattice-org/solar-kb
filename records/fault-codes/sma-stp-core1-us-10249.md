---
id: fc:sma-stp-core1-us-10249
type: FaultCode
name: SMA CORE1-US 10249
aliases:
- '10249'
- SMA 10249
- '[Interface]: network overloaded'
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10249'
code_key: '10249'
display_message: '[Interface]: network overloaded'
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h296
    h: c86593bb9e0c
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h297
    h: 059ce03933b4
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h213
    h: c86593bb9e0c
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h214
    h: 059ce03933b4
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h298
    h: c86593bb9e0c
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h299
    h: 059ce03933b4
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h297
    h: 059ce03933b4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h214
    h: 059ce03933b4
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h299
    h: 059ce03933b4
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h459
    h: 6781523265db
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h471
    h: 6781523265db
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:network-load-reduction
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h298
    h: d7d9ebc45ca9
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h215
    h: d7d9ebc45ca9
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h300
    h: d7d9ebc45ca9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h460
    h: d7d9ebc45ca9
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h472
    h: d7d9ebc45ca9
  review: drafted
---
