---
id: fc:sma-sunny-central-cp-xt-203
type: FaultCode
name: SMA SC-CP-XT 0203
aliases:
- '0203'
- '203'
- SMA 0203
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '0203'
code_key: '203'
page: 34
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r3
    h: 952732836d16
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r3
    h: 952732836d16
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h209
    h: 5a2fda46a26b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h449
    h: 5a2fda46a26b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h209
    h: 5a2fda46a26b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h449
    h: 5a2fda46a26b
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r3
    h: 952732836d16
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h209
    h: 5a2fda46a26b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h449
    h: 5a2fda46a26b
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h210
    h: 5027c6815068
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h450
    h: 5027c6815068
  review: drafted
  review_note: 'support check: partial - Grid voltage checks are described, but a measurement method as
    the detection is only implied.'
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r3
    h: 952732836d16
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h210
    h: 5027c6815068
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h450
    h: 5027c6815068
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h210
    h: 5027c6815068
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h450
    h: 5027c6815068
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:utility-consultation
  note: When grid voltage is outside permissible range due to local grid conditions.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h210
    h: 5027c6815068
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h450
    h: 5027c6815068
  review: drafted
- claim_id: c9
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h209
    h: 5a2fda46a26b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h449
    h: 5a2fda46a26b
  review: drafted
  review_note: 'support check: partial - The inverter disconnects, but the passages do not explicitly
    classify it as a fault.'
- claim_id: c10
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h209
    h: 5a2fda46a26b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h449
    h: 5a2fda46a26b
  review: drafted
- claim_id: c11
  rel: has_recovery
  target: ec:auto-reset
  note: Reconnects after grid monitoring time; Service only if message persists with grid in range.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r3
    h: 952732836d16
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
---
