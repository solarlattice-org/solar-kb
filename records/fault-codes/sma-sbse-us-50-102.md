---
id: fc:sma-sbse-us-50-102
type: FaultCode
name: SMA SBSE-US-50 102
aliases:
- '102'
- SMA 102
- Grid incident
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '102'
code_key: '102'
display_message: Grid incident
page: 97
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.2
    h: 4692fc49af09
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h428
    h: 354164b2f12c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h193
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h429
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h378
    h: 9d464275e542
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Grid voltage or impedance too high; overvoltage is covered only
    as an alternative cause.'
- claim_id: c3
  rel: reports
  target: symptom:grid-impedance-high
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h193
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h429
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h378
    h: 9d464275e542
  review: drafted
  review_note: 'support check: partial - Grid impedance too high is stated only as an alternative with
    voltage.'
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h193
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h429
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h378
    h: 9d464275e542
  review: drafted
  review_note: 'support check: partial - Inverter disconnects from the grid, but no explicit fault classification;
    a disconnect is a trip, fault is implied.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h193
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h429
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h378
    h: 9d464275e542
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h194
    h: 60749c2f0bc9
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h430
    h: 7d19dd5568fa
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h379
    h: 7d19dd5568fa
  review: drafted
  review_note: 'support check: partial - Corrective measures involve checking grid voltage, but the passages
    do not say detection is by grid voltage measurement.'
- claim_id: c7
  rel: mitigated_by
  target: mit:utility-consultation
  note: When voltage is out of range due to local grid; service if voltage is normal and message persists.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h194
    h: 60749c2f0bc9
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h430
    h: 7d19dd5568fa
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h379
    h: 7d19dd5568fa
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if grid voltage stays in range and the message persists.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h194
    h: 60749c2f0bc9
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h430
    h: 7d19dd5568fa
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h379
    h: 7d19dd5568fa
  review: drafted
---
