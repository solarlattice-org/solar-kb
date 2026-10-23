---
id: fc:sma-sunny-central-cp-xt-7901
type: FaultCode
name: SMA SC-CP-XT 7901
aliases:
- '7901'
- SMA 7901
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7901'
code_key: '7901'
page: 40
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r3
    h: 5b40178bb0f2
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:string-reverse-current
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r3
    h: 5b40178bb0f2
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r3
    h: 5b40178bb0f2
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r3
    h: 5b40178bb0f2
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r3
    h: 5b40178bb0f2
  review: drafted
---
