---
id: fc:sma-sbse-us-50-6633
type: FaultCode
name: SMA SBSE-US-50 6633
aliases:
- '6633'
- SMA 6633
- Self-diagnosis > Device fault
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '6633'
code_key: '6633'
display_message: Self-diagnosis > Device fault
page: 112
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.48
    h: 47663ea3f4b2
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h654
    h: 731fc1a6c0ad
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.48
    h: 47663ea3f4b2
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h654
    h: 731fc1a6c0ad
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.48
    h: 47663ea3f4b2
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h654
    h: 731fc1a6c0ad
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h655
    h: cca77e1e7cd3
  review: drafted
  review_note: 'support check: partial - Device fault needing Service determination suggests fault, but
    classification isn''t explicit.'
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.48
    h: 47663ea3f4b2
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h655
    h: cca77e1e7cd3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h656
    h: c87e8fc90a2c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.48
    h: 47663ea3f4b2
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h656
    h: c87e8fc90a2c
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.48
    h: 47663ea3f4b2
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h654
    h: 731fc1a6c0ad
  review: drafted
---
