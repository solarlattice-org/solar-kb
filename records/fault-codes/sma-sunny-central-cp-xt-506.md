---
id: fc:sma-sunny-central-cp-xt-506
type: FaultCode
name: SMA SC-CP-XT 0506
aliases:
- '0506'
- '506'
- SMA 0506
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '0506'
code_key: '506'
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r6
    h: 85049fd3cf1c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:islanding-detected
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r6
    h: 85049fd3cf1c
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r6
    h: 85049fd3cf1c
  review: drafted
  review_note: 'support check: partial - Corrective measure says check power frequency, but detection
    method isn''t explicitly stated.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r6
    h: 85049fd3cf1c
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r6
    h: 85049fd3cf1c
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
  review_note: 'support check: partial - Auto reconnect implied, but manual acknowledgment may be required
    depending on parameterization.'
- claim_id: c6
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r6
    h: 85049fd3cf1c
  review: drafted
---
