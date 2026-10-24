---
id: fc:sma-sb-us-41-3301
type: FaultCode
name: SMA SB-US-41 3301
aliases:
- '3301'
- SMA 3301
- Unstable operation
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '3301'
code_key: '3301'
display_message: Unstable operation
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.18
    h: 89bfe66c637d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h256
    h: 86ef2a663376
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:insufficient-dc-power
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h182
    h: 4b30e46f6050
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h257
    h: bf9b5386b1d8
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:insufficient-irradiance
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h182
    h: 4b30e46f6050
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h182
    h: 4b30e46f6050
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h183
    h: 2b403acd4c07
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h258
    h: 85a79abe467c
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h182
    h: 4b30e46f6050
  review: drafted
  review_note: 'support check: partial - Feed-in is interrupted, but the passage does not say whether
    it is a fault or a warning.'
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h182
    h: 4b30e46f6050
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h257
    h: bf9b5386b1d8
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes when irradiation rises; if frequent, check array sizing and wiring
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h183
    h: 2b403acd4c07
  review: drafted
  review_note: 'support check: partial - Wait for higher irradiation implies resumption, but auto-reset
    is not explicitly stated.'
- claim_id: c8
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Only when the message recurs frequently
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h183
    h: 2b403acd4c07
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h258
    h: 85a79abe467c
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:sma-sb-us-41
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.18
    h: 89bfe66c637d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h256
    h: 86ef2a663376
  review: drafted
---
