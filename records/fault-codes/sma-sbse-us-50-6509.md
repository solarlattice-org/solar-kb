---
id: fc:sma-sbse-us-50-6509
type: FaultCode
name: SMA SBSE-US-50 6509
aliases:
- '6509'
- SMA 6509
- Self-diagnosis > Overtemperature
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '6509'
code_key: '6509'
display_message: Self-diagnosis > Overtemperature
page: 111
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.43
    h: 5ebdfdeaca2a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h631
    h: 359fae7aa468
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.43
    h: 5ebdfdeaca2a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h631
    h: 359fae7aa468
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h632
    h: abc29332332d
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.43
    h: 5ebdfdeaca2a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h632
    h: abc29332332d
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.43
    h: 5ebdfdeaca2a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h632
    h: abc29332332d
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:ambient-temperature-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.43
    h: 5ebdfdeaca2a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h633
    h: 7ab490300d63
  review: drafted
  review_note: 'support check: partial - Measure says ensure max ambient temperature not exceeded, but
    it''s a corrective action, not a detection check.'
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.43
    h: 5ebdfdeaca2a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h633
    h: 7ab490300d63
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.43
    h: 5ebdfdeaca2a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h633
    h: 7ab490300d63
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.43
    h: 5ebdfdeaca2a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h631
    h: 359fae7aa468
  review: drafted
---
