---
id: fc:sma-sunny-central-cp-xt-7501
type: FaultCode
name: SMA SC-CP-XT 7501
aliases:
- '7501'
- SMA 7501
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7501'
code_key: '7501'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r6
    h: 254fd1c68896
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r6
    h: 254fd1c68896
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r6
    h: 254fd1c68896
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r6
    h: 254fd1c68896
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r6
    h: 254fd1c68896
  review: drafted
  review_note: 'support check: partial - Cleaning the fans is stated, but ventilation blockage clearing
    is only loosely implied.'
---
