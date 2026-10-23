---
id: fc:sma-sb-us-41-3902
type: FaultCode
name: SMA SB-US-41 3902
aliases:
- '3902'
- SMA 3902
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '3902'
code_key: '3902'
page: 60
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.30
    h: e03f92120763
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:insufficient-dc-power
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.30
    h: e03f92120763
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h305
    h: e2d0be7e71d1
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h306
    h: 27c1c9381a5e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.33
    h: 42baee9bfdc9
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h581
    h: e2d0be7e71d1
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h582
    h: 27c1c9381a5e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.22
    h: 48dceda5e74b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h475
    h: e2d0be7e71d1
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h476
    h: 27c1c9381a5e
  review: drafted
  review_note: 'support check: partial - Waiting for DC start conditions implies insufficient DC power
    but it is not explicitly stated.'
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h307
    h: 95bb0df6a1e0
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h583
    h: 64c1ff830bc2
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h477
    h: 95bb0df6a1e0
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Feed-in has not started because start conditions are not yet met.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h306
    h: 27c1c9381a5e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h582
    h: 27c1c9381a5e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h476
    h: 27c1c9381a5e
  review: drafted
  review_note: 'support check: partial - Feed-in conditions not yet fulfilled is stated, but nothing says
    it is a trip or stops production; it is more…'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Normal case clears with higher irradiation; frequent recurrence calls for parameter or array checks.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h307
    h: 95bb0df6a1e0
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h583
    h: 64c1ff830bc2
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h477
    h: 95bb0df6a1e0
  review: drafted
  review_note: 'support check: partial - Passages say wait for higher irradiation but never state the
    event clears automatically (auto-reset).'
- claim_id: c6
  rel: mitigated_by
  target: mit:avoid-partial-shading
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h307
    h: 95bb0df6a1e0
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h583
    h: 64c1ff830bc2
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h477
    h: 95bb0df6a1e0
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: When the message appears frequently in the morning.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h307
    h: 95bb0df6a1e0
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h583
    h: 64c1ff830bc2
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h477
    h: 95bb0df6a1e0
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When the message appears frequently at medium irradiation.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h307
    h: 95bb0df6a1e0
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h583
    h: 64c1ff830bc2
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h477
    h: 95bb0df6a1e0
  review: drafted
  review_note: 'support check: partial - Passages say to ensure the PV module is correctly rated when
    frequent at medium irradiation, which is only loosely a…'
- claim_id: c9
  rel: mitigated_by
  target: mit:firmware-update
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.33
    h: 42baee9bfdc9
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h583
    h: 64c1ff830bc2
  review: drafted
---
