---
id: fc:sma-sunny-central-cp-xt-7507
type: FaultCode
name: SMA SC-CP-XT 7507
aliases:
- '7507'
- SMA 7507
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7507'
code_key: '7507'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r9
    h: 35a8d77bd2b1
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:fan-fault-alarm
  note: Fan motor protective breaker has tripped.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r9
    h: 35a8d77bd2b1
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r9
    h: 35a8d77bd2b1
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r9
    h: 35a8d77bd2b1
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r9
    h: 35a8d77bd2b1
  review: drafted
---
