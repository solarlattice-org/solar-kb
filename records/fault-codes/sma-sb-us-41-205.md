---
id: fc:sma-sb-us-41-205
type: FaultCode
name: SMA SB-US-41 0205
aliases:
- '0205'
- '205'
- SMA 0205
- Grid incident
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '0205'
code_key: '205'
display_message: Grid incident
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.7
    h: f09c6412bcf1
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h212
    h: 354164b2f12c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-sync-failure
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r5
    h: 34694c80e731
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-frequency-out-of-range
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r5
    h: 34694c80e731
  review: drafted
  review_note: 'support check: partial - The passage mentions a not-permitted grid frequency change, which
    is not exactly frequency out of range.'
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h213
    h: 5a2fda46a26b
  review: drafted
  review_note: 'support check: partial - The passage with the AC cable explanation is cited for 0205,
    but it is a different message''s explanation with no…'
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h214
    h: 5027c6815068
  review: drafted
  review_note: 'support check: partial - Grid voltage checks are described, but they are not tied to 0205
    detection by voltage measurement.'
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h214
    h: 5027c6815068
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h214
    h: 5027c6815068
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h214
    h: 5027c6815068
  review: drafted
- claim_id: c9
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h213
    h: 5a2fda46a26b
  review: drafted
  review_note: 'support check: partial - The inverter disconnects, but the passage does not classify it
    as a fault.'
- claim_id: c10
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h213
    h: 5a2fda46a26b
  review: drafted
- claim_id: c11
  rel: has_recovery
  target: ec:auto-reset
  note: Service only if message persists with grid in permissible range.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r5
    h: 34694c80e731
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
---
