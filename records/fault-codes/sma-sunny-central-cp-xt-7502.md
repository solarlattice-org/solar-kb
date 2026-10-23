---
id: fc:sma-sunny-central-cp-xt-7502
type: FaultCode
name: SMA SC-CP-XT 7502
aliases:
- '7502'
- SMA 7502
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7502'
code_key: '7502'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r7
    h: 1bc32dcab511
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r7
    h: 1bc32dcab511
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r7
    h: 1bc32dcab511
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r7
    h: 1bc32dcab511
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r7
    h: 1bc32dcab511
  review: drafted
  review_note: 'support check: partial - Cleaning the fans is stated, but ventilation blockage clearing
    is only loosely implied.'
---
