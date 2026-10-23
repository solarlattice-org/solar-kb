---
id: fc:sma-sunny-central-cp-xt-802
type: FaultCode
name: SMA SC-CP-XT 0802
aliases:
- '0802'
- '802'
- SMA 0802
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '0802'
code_key: '802'
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r7
    h: b36691fd426f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:phase-loss
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r7
    h: b36691fd426f
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r7
    h: b36691fd426f
  review: drafted
  review_note: 'support check: partial - Corrective measure is to check grid voltage, but detection method
    is not explicitly stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:external-fuse-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r7
    h: b36691fd426f
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r7
    h: b36691fd426f
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r7
    h: b36691fd426f
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r7
    h: b36691fd426f
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
  review_note: 'support check: partial - Auto reconnect implied, but manual acknowledgment may be needed
    depending on parameterization.'
---
