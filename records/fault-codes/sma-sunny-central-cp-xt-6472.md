---
id: fc:sma-sunny-central-cp-xt-6472
type: FaultCode
name: SMA SC-CP-XT 6472
aliases:
- '6472'
- SMA 6472
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6472'
code_key: '6472'
page: 38
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r14
    h: fa0811fd5e22
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  note: Capacitor test loops endlessly between online and offline modes.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r14
    h: fa0811fd5e22
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r14
    h: fa0811fd5e22
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r14
    h: fa0811fd5e22
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r14
    h: fa0811fd5e22
  review: drafted
---
