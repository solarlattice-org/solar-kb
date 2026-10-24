---
id: fc:sma-sbse-us-50-9345
type: FaultCode
name: SMA SBSE-US-50 9345
aliases:
- '9345'
- SMA 9345
- Battery charge too low for start procedure
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9345'
code_key: '9345'
display_message: Battery charge too low for start procedure
page: 120
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.77
    h: d235d1819f1d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h796
    h: bfa3341c4bfc
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:low-battery-charge
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h796
    h: bfa3341c4bfc
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h797
    h: bc54a5af1269
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: Start procedure cannot proceed due to low battery charge.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h796
    h: bfa3341c4bfc
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h797
    h: bc54a5af1269
  review: drafted
  review_note: 'support check: partial - Start procedure blocked by low charge, but the passages don''t
    explicitly state a shutdown/trip classification; implied by not starting.'
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  note: Battery must be charged manually by service or battery manufacturer.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h797
    h: bc54a5af1269
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h798
    h: a0f429bc105e
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h798
    h: a0f429bc105e
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.77
    h: d235d1819f1d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h796
    h: bfa3341c4bfc
  review: drafted
---
