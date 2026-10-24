---
id: fc:sma-sbse-us-50-7703
type: FaultCode
name: SMA SBSE-US-50 7703
aliases:
- '7703'
- SMA 7703
- Self-diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '7703'
code_key: '7703'
display_message: Self-diagnosis > Interference device
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.56
    h: 63cd9701aa48
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h694
    h: 75f49e9e17fb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.56
    h: 63cd9701aa48
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h694
    h: 75f49e9e17fb
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  note: Relay test failed; may also appear briefly during grid fluctuations.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h578
    h: e00fbe5b09cd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h579
    h: 15cb3c42de66
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h578
    h: e00fbe5b09cd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h579
    h: 15cb3c42de66
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.56
    h: 63cd9701aa48
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h695
    h: cca77e1e7cd3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h578
    h: e00fbe5b09cd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h579
    h: 15cb3c42de66
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h578
    h: e00fbe5b09cd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h579
    h: 15cb3c42de66
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h578
    h: e00fbe5b09cd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h580
    h: 8585c187c793
  review: drafted
  review_note: 'support check: partial - Grid voltage measurement is a corrective check, but the passages
    don''t say the event is detected by it.'
- claim_id: c8
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h578
    h: e00fbe5b09cd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h580
    h: 8585c187c793
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:ground-conductor-check
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h578
    h: e00fbe5b09cd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h580
    h: 8585c187c793
  review: drafted
  review_note: 'support check: partial - Grounding is mentioned only through N-PE voltage and grounding
    measures; no explicit grounding conductor check.'
- claim_id: c10
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if the event persists after AC and grounding checks.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h578
    h: e00fbe5b09cd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h580
    h: 8585c187c793
  review: drafted
- claim_id: c11
  rel: has_recovery
  target: ec:service-required
  note: 'Other manual: check AC wiring and grounding first, replace assembly if persisting.'
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.56
    h: 63cd9701aa48
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h695
    h: cca77e1e7cd3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h696
    h: 417f2f122215
  review: drafted
- claim_id: c12
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.56
    h: 63cd9701aa48
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h694
    h: 75f49e9e17fb
  review: drafted
---
