---
id: fc:sma-sunny-central-cp-xt-6471
type: FaultCode
name: SMA SC-CP-XT 6471
aliases:
- '6471'
- SMA 6471
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6471'
code_key: '6471'
page: 38
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r13
    h: ca8b4ab7fe15
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  note: Online capacitor self-test.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r13
    h: ca8b4ab7fe15
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r13
    h: ca8b4ab7fe15
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r13
    h: ca8b4ab7fe15
  review: drafted
---
