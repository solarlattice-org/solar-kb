---
id: fc:sma-sunny-central-cp-xt-6454
type: FaultCode
name: SMA SC-CP-XT 6454
aliases:
- '6454'
- SMA 6454
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6454'
code_key: '6454'
page: 38
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r8
    h: bb5d708c080b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:measurement-signal-error
  note: AC current value reported faulty.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r8
    h: bb5d708c080b
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r8
    h: bb5d708c080b
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r8
    h: bb5d708c080b
  review: drafted
---
