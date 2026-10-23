---
id: fc:sma-stp-core1-us-8003
type: FaultCode
name: SMA CORE1-US 8003
aliases:
- '8003'
- SMA 8003
- Active power limit Temperature
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '8003'
code_key: '8003'
display_message: Active power limit Temperature
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h285
    h: e387fca06bb3
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h286
    h: 5d84ec3d5090
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
  cite:
  - src: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
    loc: sec=h1
    h: 0bf710148ab2
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h286
    h: 5d84ec3d5090
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h237
    h: 0d482b96f8cd
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h401
    h: 717859829bc4
  - src: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
    loc: sec=h1
    h: 0bf710148ab2
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
    loc: sec=h1
    h: 0bf710148ab2
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
    loc: sec=h1
    h: 0bf710148ab2
  review: drafted
  review_note: 'support check: partial - The article says to run a fan test and verify fan operation as
    troubleshooting, but doesn''t say the event is…'
- claim_id: c6
  rel: detected_by
  target: method:ambient-temperature-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h287
    h: 304a3b0ee66d
  - src: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
    loc: sec=h1
    h: 0bf710148ab2
  review: drafted
  review_note: 'support check: partial - Passages say to verify ambient temperature isn''t exceeded as
    a corrective check, but not that the event is detected by…'
- claim_id: c7
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h287
    h: 304a3b0ee66d
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h238
    h: 3b4466d6cda8
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h402
    h: 49339a7942f0
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h287
    h: 304a3b0ee66d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h402
    h: 49339a7942f0
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h287
    h: 304a3b0ee66d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h402
    h: 49339a7942f0
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:installation-clearance
  cite:
  - src: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
    loc: sec=h1
    h: 0bf710148ab2
  review: drafted
- claim_id: c11
  rel: has_event_class
  target: ec:warning
  note: Occasional occurrence is not a concern; frequent occurrence warrants installer evaluation.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h286
    h: 5d84ec3d5090
  - src: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
    loc: sec=h1
    h: 0bf710148ab2
  review: drafted
- claim_id: c12
  rel: has_production_effect
  target: ec:derate
  note: No derate value stated.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h286
    h: 5d84ec3d5090
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h401
    h: 717859829bc4
  - src: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
    loc: sec=h1
    h: 0bf710148ab2
  review: drafted
---
