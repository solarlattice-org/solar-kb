---
id: fc:sma-sunny-central-cp-xt-505
type: FaultCode
name: SMA SC-CP-XT 0505
aliases:
- '0505'
- '505'
- SMA 0505
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '0505'
code_key: '505'
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r5
    h: a74a20a44ee5
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r5
    h: a74a20a44ee5
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r5
    h: a74a20a44ee5
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r5
    h: a74a20a44ee5
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
  review_note: 'support check: partial - Auto reconnect implied, but manual acknowledgment possible depending
    on parameterization.'
---
