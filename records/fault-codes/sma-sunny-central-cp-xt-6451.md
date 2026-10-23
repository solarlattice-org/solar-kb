---
id: fc:sma-sunny-central-cp-xt-6451
type: FaultCode
name: SMA SC-CP-XT 6451
aliases:
- '6451'
- SMA 6451
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6451'
code_key: '6451'
page: 38
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r5
    h: a3dbd339652a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-voltage-mismatch
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r5
    h: a3dbd339652a
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r5
    h: a3dbd339652a
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r5
    h: a3dbd339652a
  review: drafted
---
