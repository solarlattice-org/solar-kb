---
id: fc:sma-sbse-us-50-3302
type: FaultCode
name: SMA SBSE-US-50 3302
aliases:
- '3302'
- SMA 3302
- Unstable operation
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '3302'
code_key: '3302'
display_message: Unstable operation
page: 103
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.21
    h: cc893b83adf1
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h523
    h: 86ef2a663376
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:insufficient-dc-power
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h184
    h: ece357161bcb
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h524
    h: bf9b5386b1d8
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:insufficient-irradiance
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h184
    h: ece357161bcb
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h184
    h: ece357161bcb
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h185
    h: 4ab884337c82
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h525
    h: 2f4e68d48aa0
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h184
    h: ece357161bcb
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Feed-in is interrupted, but fault versus warning is not stated.'
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h184
    h: ece357161bcb
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h524
    h: bf9b5386b1d8
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes when irradiation rises; if frequent, check array sizing and wiring
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h185
    h: 4ab884337c82
  review: drafted
  review_note: 'support check: partial - Waiting for irradiation to increase implies auto-resume but is
    not explicit.'
- claim_id: c8
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Only when the message recurs frequently
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h185
    h: 4ab884337c82
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h525
    h: 2f4e68d48aa0
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.21
    h: cc893b83adf1
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h523
    h: 86ef2a663376
  review: drafted
---
