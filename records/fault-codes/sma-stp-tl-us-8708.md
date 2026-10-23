---
id: fc:sma-stp-tl-us-8708
type: FaultCode
name: SMA STP-TL-US 8708
aliases:
- '8708'
- SMA 8708
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '8708'
code_key: '8708'
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=20.r2
    h: 1f5046ab2665
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=20.r2
    h: 1f5046ab2665
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h413
    h: 4026503bfd7c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h719
    h: 4026503bfd7c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h593
    h: 4026503bfd7c
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h426
    h: 4026503bfd7c
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:network-cable
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h247
    h: af454c6d76e5
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h414
    h: 800a134e3dfa
  review: drafted
  review_note: 'support check: partial - Cables and plugs of the connection to the system manager are
    checked, but a network cable is not specifically named.'
- claim_id: c4
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h247
    h: af454c6d76e5
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h414
    h: 800a134e3dfa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h720
    h: 800a134e3dfa
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h594
    h: 800a134e3dfa
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h427
    h: 800a134e3dfa
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:derate
  note: Only when fallback is set to a percentage limit; otherwise last values retained. Limit is a configured
    setting, no number given.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=20.r2
    h: 1f5046ab2665
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h413
    h: 4026503bfd7c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h593
    h: 4026503bfd7c
  review: drafted
---
