---
id: fc:sma-sbse-us-50-8003
type: FaultCode
name: SMA SBSE-US-50 8003
aliases:
- '8003'
- SMA 8003
- Temperature derating
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '8003'
code_key: '8003'
display_message: Temperature derating
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.57
    h: eaa9d6ed2a96
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h699
    h: 14cc71565301
  review: drafted
- claim_id: c2
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
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
    loc: sec=h1
    h: 0bf710148ab2
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
    loc: sec=h1
    h: 0bf710148ab2
  review: drafted
  review_note: 'support check: partial - The article says to run a fan test and verify fan operation as
    troubleshooting, but doesn''t say the event is…'
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
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
- claim_id: c8
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
- claim_id: c9
  rel: mitigated_by
  target: mit:installation-clearance
  cite:
  - src: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
    loc: sec=h1
    h: 0bf710148ab2
  review: drafted
- claim_id: c10
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
- claim_id: c11
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
