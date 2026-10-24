---
id: fc:sma-sb-us-40-8206
type: FaultCode
name: SMA SB-US-40 8206
aliases:
- '8206'
- SMA 8206
- Electr. arc detected > Please confirm by tapping
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-40
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP/1TP-US-40)
code: '8206'
code_key: '8206'
display_message: Electr. arc detected > Please confirm by tapping
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-40-ba-en-13
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h239
    h: 01e258de93a4
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h240
    h: dcdd366c906f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:operation-inhibited
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h405
    h: 01564ae6eb14
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h240
    h: dcdd366c906f
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=20.r1
    h: 83339559873d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h405
    h: 01564ae6eb14
  - src: src:sma-kb-stp-us-41-events-8206-8210
    loc: sec=h1
    h: 4223b7d41d2f
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h240
    h: dcdd366c906f
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h406
    h: d7fc9b3e4578
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h240
    h: dcdd366c906f
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h406
    h: d7fc9b3e4578
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h406
    h: d7fc9b3e4578
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h406
    h: d7fc9b3e4578
  review: drafted
  review_note: 'support check: partial - Inspecting DC conductors and connectors for damage is similar
    to a wiring check, but only partly matches.'
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h405
    h: 01564ae6eb14
  review: drafted
  review_note: 'support check: partial - Stops feed-in into operation inhibition suggests a fault, but
    the classification isn''t explicitly stated; it is implied by stopping the device.'
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h405
    h: 01564ae6eb14
  review: drafted
- claim_id: c10
  rel: has_recovery
  target: ec:manual-reset
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h241
    h: c49fd744b7f1
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h406
    h: d7fc9b3e4578
  - src: src:sma-kb-stp-us-41-events-8206-8210
    loc: sec=h1
    h: 4223b7d41d2f
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c11
  rel: applies_to
  target: prod:sma-sb-us-40
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h239
    h: 01e258de93a4
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h240
    h: dcdd366c906f
  review: drafted
---
