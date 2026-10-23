---
id: fc:sma-sunny-central-cp-xt-6456
type: FaultCode
name: SMA SC-CP-XT 6456
aliases:
- '6456'
- SMA 6456
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6456'
code_key: '6456'
page: 38
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r10
    h: adcbdb84beb6
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-kb-error-message-6456-precharging-circuit-defective
  cite:
  - src: src:sma-kb-error-message-6456-precharging-circuit-defective
    loc: sec=h1
    h: ec77417e5497
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:precharge-circuit-failure
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r10
    h: adcbdb84beb6
  - src: src:sma-kb-error-message-6456-precharging-circuit-defective
    loc: sec=h1
    h: ec77417e5497
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:precharge-circuit
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r10
    h: adcbdb84beb6
  - src: src:sma-kb-error-message-6456-precharging-circuit-defective
    loc: sec=h1
    h: ec77417e5497
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r10
    h: adcbdb84beb6
  - src: src:sma-kb-error-message-6456-precharging-circuit-defective
    loc: sec=h1
    h: ec77417e5497
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r10
    h: adcbdb84beb6
  - src: src:sma-kb-error-message-6456-precharging-circuit-defective
    loc: sec=h1
    h: ec77417e5497
  review: drafted
---
