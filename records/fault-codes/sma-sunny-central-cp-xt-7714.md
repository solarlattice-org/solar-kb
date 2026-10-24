---
id: fc:sma-sunny-central-cp-xt-7714
type: FaultCode
name: SMA SC-CP-XT 7714
aliases:
- '7714'
- SMA 7714
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7714'
code_key: '7714'
page: 40
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r1
    h: bdaed900d26c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:switch-cycle-limit
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r1
    h: bdaed900d26c
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ground-fault-detector
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r1
    h: bdaed900d26c
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:gfdi-replacement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r1
    h: bdaed900d26c
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r1
    h: bdaed900d26c
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r1
    h: bdaed900d26c
  review: drafted
---
