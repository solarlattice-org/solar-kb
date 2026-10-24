---
id: fc:sma-stp-core1-us-10513
type: FaultCode
name: SMA CORE1-US 10513
aliases:
- '10513'
- SMA 10513
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10513'
code_key: '10513'
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26.r4
    h: 18a9321cfc89
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:remote-shutdown
  note: Triggered by the grid and PV system protection device via monitoring relay.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26.r4
    h: 18a9321cfc89
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26.r4
    h: 18a9321cfc89
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26.r4
    h: 18a9321cfc89
  review: drafted
---
