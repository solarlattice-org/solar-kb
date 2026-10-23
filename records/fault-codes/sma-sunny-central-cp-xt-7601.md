---
id: fc:sma-sunny-central-cp-xt-7601
type: FaultCode
name: SMA SC-CP-XT 7601
aliases:
- '7601'
- SMA 7601
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7601'
code_key: '7601'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r12
    h: 4bbbeb8f9919
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r12
    h: 4bbbeb8f9919
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r12
    h: 4bbbeb8f9919
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r12
    h: 4bbbeb8f9919
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r12
    h: 4bbbeb8f9919
  review: drafted
---
