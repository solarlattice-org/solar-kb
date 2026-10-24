---
id: fc:sma-stp-core1-us-101
type: FaultCode
name: SMA CORE1-US 101
aliases:
- '101'
- SMA 101
- Grid incident
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '101'
code_key: '101'
display_message: Grid incident
page: 47
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h236
    h: b078e0b636d4
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h237
    h: 797da27ddf22
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h236
    h: b078e0b636d4
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h237
    h: 797da27ddf22
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h189
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h424
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h373
    h: 9d464275e542
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-impedance-high
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h236
    h: b078e0b636d4
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h237
    h: 797da27ddf22
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h189
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h424
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h373
    h: 9d464275e542
  review: drafted
  review_note: 'support check: partial - The text says grid voltage or grid impedance is too high, so
    impedance is stated only as an alternative cause.'
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h236
    h: b078e0b636d4
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h238
    h: 60749c2f0bc9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h190
    h: 60749c2f0bc9
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h425
    h: 7d19dd5568fa
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h374
    h: 7d19dd5568fa
  review: drafted
  review_note: 'support check: partial - The passages say to check the grid voltage but do not say the
    event is detected by grid voltage measurement.'
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: When grid voltage is outside permissible range due to local grid conditions
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h236
    h: b078e0b636d4
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h238
    h: 60749c2f0bc9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h190
    h: 60749c2f0bc9
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h425
    h: 7d19dd5568fa
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h374
    h: 7d19dd5568fa
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation when grid voltage is within range and message persists
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h236
    h: b078e0b636d4
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h238
    h: 60749c2f0bc9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h190
    h: 60749c2f0bc9
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h425
    h: 7d19dd5568fa
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h374
    h: 7d19dd5568fa
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h236
    h: b078e0b636d4
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h237
    h: 797da27ddf22
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h189
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h424
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h373
    h: 9d464275e542
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h236
    h: b078e0b636d4
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h237
    h: 797da27ddf22
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h189
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h424
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h373
    h: 9d464275e542
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h236
    h: b078e0b636d4
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h237
    h: 797da27ddf22
  review: drafted
---
