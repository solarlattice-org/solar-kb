---
id: fc:sma-sb-us-41-105
type: FaultCode
name: SMA SB-US-41 105
aliases:
- '105'
- SMA 105
- Grid incident
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '105'
code_key: '105'
display_message: Grid incident
page: 51
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.4
    h: 5b2ca17ad13d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h200
    h: 354164b2f12c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h201
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h439
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h388
    h: 9d464275e542
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-impedance-high
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h201
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h439
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h388
    h: 9d464275e542
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h201
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h439
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h388
    h: 9d464275e542
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h201
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h439
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h388
    h: 9d464275e542
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h202
    h: 60749c2f0bc9
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h440
    h: 60749c2f0bc9
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h389
    h: 60749c2f0bc9
  review: drafted
  review_note: 'support check: partial - Passages tell to check grid voltage but do not say the code is
    detected by grid voltage measurement; only implied.'
- claim_id: c7
  rel: mitigated_by
  target: mit:utility-consultation
  note: When voltage is out of range due to local grid; service if voltage is normal and message persists.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h202
    h: 60749c2f0bc9
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h440
    h: 60749c2f0bc9
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h389
    h: 60749c2f0bc9
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if grid voltage stays in range and the message persists.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h202
    h: 60749c2f0bc9
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h440
    h: 60749c2f0bc9
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h389
    h: 60749c2f0bc9
  review: drafted
---
