---
id: fc:sma-sunny-central-cp-xt-9013
type: FaultCode
name: SMA SC-CP-XT 9013
aliases:
- '9013'
- SMA 9013
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '9013'
code_key: '9013'
page: 40
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r10
    h: 53f18afcee4a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:remote-shutdown
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r10
    h: 53f18afcee4a
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r10
    h: 53f18afcee4a
  review: drafted
  review_note: 'support check: partial - Shutdown is stated, implying trip, but the row mostly describes
    a grid management shutdown without explicit production detail.'
---
