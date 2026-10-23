---
id: fc:sma-sb-us-41-3303
type: FaultCode
name: SMA SB-US-41 3303
aliases:
- '3303'
- SMA 3303
- Unstable operation
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '3303'
code_key: '3303'
display_message: Unstable operation
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.19
    h: e3d28fa695a1
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h260
    h: 86ef2a663376
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:insufficient-dc-power
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h187
    h: ce98c4366db9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h261
    h: bf9b5386b1d8
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h529
    h: bf9b5386b1d8
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:insufficient-irradiance
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h187
    h: ce98c4366db9
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h187
    h: ce98c4366db9
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h188
    h: 1f65f4b4019b
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h262
    h: 85a79abe467c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h530
    h: 2f4e68d48aa0
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h187
    h: ce98c4366db9
  review: drafted
  review_note: 'support check: partial - Feed-in is interrupted, but fault versus warning is not stated.'
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h187
    h: ce98c4366db9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h261
    h: bf9b5386b1d8
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h529
    h: bf9b5386b1d8
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes when irradiation rises; if frequent, check array sizing and wiring
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h188
    h: 1f65f4b4019b
  review: drafted
  review_note: 'support check: partial - Waiting for higher irradiation implies auto-resume but is not
    explicit.'
- claim_id: c8
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Only when the message recurs frequently
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h188
    h: 1f65f4b4019b
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h262
    h: 85a79abe467c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h530
    h: 2f4e68d48aa0
  review: drafted
  review_note: 'support check: partial - Passages say to ensure the PV array is correctly rated and wired
    if the message is frequent, but do not…'
---
