---
id: fc:sma-sunny-central-cp-xt-7503
type: FaultCode
name: SMA SC-CP-XT 7503
aliases:
- '7503'
- SMA 7503
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7503'
code_key: '7503'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r8
    h: 2ae39df09eda
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r8
    h: 2ae39df09eda
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:cooling-fan
  note: Fan cooling the inverter bridge.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r8
    h: 2ae39df09eda
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r8
    h: 2ae39df09eda
  review: drafted
---
