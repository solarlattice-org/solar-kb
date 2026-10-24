---
id: fc:sma-sunny-central-cp-xt-1500
type: FaultCode
name: SMA SC-CP-XT 1500
aliases:
- '1500'
- SMA 1500
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '1500'
code_key: '1500'
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r9
    h: f829044168eb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-voltage-out-of-range
  note: Reconnection conditions not yet met after a grid error.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r9
    h: f829044168eb
  review: drafted
  review_note: 'support check: partial - Reconnection conditions not met after grid error is stated, but
    the row doesn''t state grid voltage out of range specifically;…'
- claim_id: c3
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r9
    h: f829044168eb
  review: drafted
  review_note: 'support check: partial - Corrective measure says check power frequency, but detection
    method is not explicitly stated.'
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r9
    h: f829044168eb
  review: drafted
  review_note: 'support check: partial - Corrective measure says check grid voltage, but detection method
    is not explicitly stated.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r9
    h: f829044168eb
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
  review_note: 'support check: partial - Row only states reconnection conditions not yet met (W behavior);
    shutdown is implied by the general section for grid errors,…'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r9
    h: f829044168eb
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
  review_note: 'support check: partial - Waiting for reconnection conditions implies auto resumption,
    but manual acknowledgment may be required depending on parameterization.'
- claim_id: c7
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r9
    h: f829044168eb
  review: drafted
---
