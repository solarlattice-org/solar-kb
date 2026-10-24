---
id: fc:sma-sunny-central-cp-xt-502
type: FaultCode
name: SMA SC-CP-XT 0502
aliases:
- '0502'
- '502'
- SMA 0502
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '0502'
code_key: '502'
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r2
    h: e11a6a6a6933
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r2
    h: e11a6a6a6933
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r2
    h: e11a6a6a6933
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h286
    h: d1e3cc0693a5
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:utility-consultation
  note: When frequency fluctuations occur frequently.
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h286
    h: d1e3cc0693a5
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only with grid operator approval, coordinated with Service.
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h286
    h: d1e3cc0693a5
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h285
    h: 272c39d1e1c3
  review: drafted
  review_note: 'support check: partial - Passage says inverter disconnected due to grid frequency out
    of range, but doesn''t state a fault classification explicitly; disconnection implies…'
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h285
    h: 272c39d1e1c3
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r2
    h: e11a6a6a6933
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
  review_note: 'support check: partial - Grid monitoring then reconnect implies auto-resume, but the general
    section notes manual acknowledgment may be required depending on parameterization; 0502…'
- claim_id: c9
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r2
    h: e11a6a6a6933
  review: drafted
---
