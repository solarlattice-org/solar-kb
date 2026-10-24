---
id: fc:sma-sunny-central-cp-xt-6119
type: FaultCode
name: SMA SC-CP-XT 6119
aliases:
- '6119'
- SMA 6119
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6119'
code_key: '6119'
page: 37
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r6
    h: b22ebcba7d77
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r6
    h: b22ebcba7d77
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:digital-signal-processor
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r6
    h: b22ebcba7d77
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r6
    h: b22ebcba7d77
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r6
    h: b22ebcba7d77
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r6
    h: b22ebcba7d77
  review: drafted
---
