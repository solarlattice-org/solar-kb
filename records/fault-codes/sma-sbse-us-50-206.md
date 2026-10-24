---
id: fc:sma-sbse-us-50-206
type: FaultCode
name: SMA SBSE-US-50 206
aliases:
- '206'
- SMA 206
- Grid incident
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '206'
code_key: '206'
display_message: Grid incident
page: 99
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.7
    h: bf2775ef7914
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h453
    h: 354164b2f12c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h217
    h: 5a2fda46a26b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h454
    h: 5a2fda46a26b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h217
    h: 5a2fda46a26b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h454
    h: 5a2fda46a26b
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:cable-defect
  note: Only when the AC cable is found damaged.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h217
    h: 5a2fda46a26b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h454
    h: 5a2fda46a26b
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h217
    h: 5a2fda46a26b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h454
    h: 5a2fda46a26b
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h217
    h: 5a2fda46a26b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h454
    h: 5a2fda46a26b
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h217
    h: 5a2fda46a26b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h454
    h: 5a2fda46a26b
  review: drafted
- claim_id: c8
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h218
    h: 5027c6815068
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h455
    h: 5027c6815068
  review: drafted
  review_note: 'support check: partial - Corrective measures include checking grid voltage, but detection
    method is not stated.'
- claim_id: c9
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h218
    h: 5027c6815068
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h455
    h: 5027c6815068
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h218
    h: 5027c6815068
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h455
    h: 5027c6815068
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:utility-consultation
  note: When voltage is out of range due to local grid; service if voltage is normal and message persists.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h218
    h: 5027c6815068
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h455
    h: 5027c6815068
  review: drafted
- claim_id: c12
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.7
    h: bf2775ef7914
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h453
    h: 354164b2f12c
  review: drafted
---
