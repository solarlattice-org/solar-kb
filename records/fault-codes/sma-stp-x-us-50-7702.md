---
id: fc:sma-stp-x-us-50-7702
type: FaultCode
name: SMA STP-X-US 7702
aliases:
- '7702'
- SMA 7702
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '7702'
code_key: '7702'
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.42
    h: 456d29ca76f8
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h573
    h: a01728932883
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h280
    h: 35114d3e86e1
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h689
    h: 75f49e9e17fb
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h690
    h: cca77e1e7cd3
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  note: Applies where the event is raised by the internal relay test.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h573
    h: a01728932883
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h574
    h: 15cb3c42de66
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h574
    h: 15cb3c42de66
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h575
    h: 8585c187c793
  review: drafted
  review_note: 'support check: partial - Passage uses grid voltage measurement as a diagnostic corrective
    step, but does not state the event is detected by it.'
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h575
    h: 8585c187c793
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h281
    h: c87e8fc90a2c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h691
    h: 417f2f122215
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only when the event persists after the AC checks.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h575
    h: 8585c187c793
  review: drafted
- claim_id: c9
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h280
    h: 35114d3e86e1
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h281
    h: c87e8fc90a2c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h574
    h: 15cb3c42de66
  review: drafted
- claim_id: c10
  rel: has_production_effect
  target: ec:trip
  note: Inverter cannot connect to the grid while the relay fault is present.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h574
    h: 15cb3c42de66
  review: drafted
- claim_id: c11
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h280
    h: 35114d3e86e1
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h281
    h: c87e8fc90a2c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h690
    h: cca77e1e7cd3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h691
    h: 417f2f122215
  review: drafted
- claim_id: c12
  rel: applies_to
  target: prod:sma-stp-x-us-50
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.42
    h: 456d29ca76f8
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h573
    h: a01728932883
  review: drafted
---
