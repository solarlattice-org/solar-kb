---
id: fc:sma-sunny-central-cp-xt-6448
type: FaultCode
name: SMA SC-CP-XT 6448
aliases:
- '6448'
- SMA 6448
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6448'
code_key: '6448'
page: 38
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r4
    h: 58b52105d499
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:insulation-monitor-threshold-error
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r4
    h: 58b52105d499
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:insulation-monitor
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r4
    h: 58b52105d499
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:insulation-monitor-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r4
    h: 58b52105d499
  review: drafted
---
