---
id: fc:sma-sb-us-41-3901
type: FaultCode
name: SMA SB-US-41 3901
aliases:
- '3901'
- SMA 3901
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '3901'
code_key: '3901'
page: 60
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.29
    h: 21f654ac028d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:insufficient-dc-power
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.29
    h: 21f654ac028d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h301
    h: e2d0be7e71d1
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h302
    h: 27c1c9381a5e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.32
    h: d493efa5c96e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h576
    h: e2d0be7e71d1
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h577
    h: 27c1c9381a5e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.21
    h: 110d8e4104f6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h470
    h: e2d0be7e71d1
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h471
    h: 27c1c9381a5e
  review: drafted
  review_note: 'support check: partial - Waiting for DC start conditions and feed-in conditions unmet,
    with irradiation remedies, imply insufficient DC power but it is not…'
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h303
    h: 86dadeb7c059
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h578
    h: 64c1ff830bc2
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h472
    h: 86dadeb7c059
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Feed-in has not started because start conditions are not yet met.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h302
    h: 27c1c9381a5e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h577
    h: 27c1c9381a5e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h471
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
    loc: sec=h303
    h: 86dadeb7c059
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h578
    h: 64c1ff830bc2
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h472
    h: 86dadeb7c059
  review: drafted
  review_note: 'support check: partial - Waiting for higher irradiation implies it clears on its own,
    but auto-reset is not explicitly stated.'
- claim_id: c6
  rel: mitigated_by
  target: mit:avoid-partial-shading
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h303
    h: 86dadeb7c059
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h578
    h: 64c1ff830bc2
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h472
    h: 86dadeb7c059
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: When the message appears frequently in the morning.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h303
    h: 86dadeb7c059
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h578
    h: 64c1ff830bc2
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h472
    h: 86dadeb7c059
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When the message appears frequently at medium irradiation.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h303
    h: 86dadeb7c059
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h578
    h: 64c1ff830bc2
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h472
    h: 86dadeb7c059
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:firmware-update
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.32
    h: d493efa5c96e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h578
    h: 64c1ff830bc2
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:sma-sb-us-41
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.29
    h: 21f654ac028d
  review: drafted
---
