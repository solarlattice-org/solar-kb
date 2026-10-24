---
id: fc:sma-sb-us-41-6701
type: FaultCode
name: SMA SB-US-41 6701
aliases:
- '6701'
- SMA 6701
- Communication impaired
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '6701'
code_key: '6701'
display_message: Communication impaired
page: 61
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.33
    h: d4300b29cacf
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h316
    h: 425aae51d4ca
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h316
    h: 425aae51d4ca
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h317
    h: c766760ec4c5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h352
    h: 425aae51d4ca
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h353
    h: c766760ec4c5
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:communication-processor
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h317
    h: c766760ec4c5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h353
    h: c766760ec4c5
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when the message appears frequently.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h318
    h: 9ae650369fe8
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h354
    h: 9ae650369fe8
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h317
    h: c766760ec4c5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h353
    h: c766760ec4c5
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h317
    h: c766760ec4c5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h353
    h: c766760ec4c5
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sma-sb-us-41
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.33
    h: d4300b29cacf
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h316
    h: 425aae51d4ca
  review: drafted
---
