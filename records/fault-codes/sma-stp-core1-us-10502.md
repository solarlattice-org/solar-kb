---
id: fc:sma-stp-core1-us-10502
type: FaultCode
name: SMA CORE1-US 10502
aliases:
- '10502'
- SMA 10502
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10502'
code_key: '10502'
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26.r3
    h: 945dd6ee9a7b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-power-derating
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26.r3
    h: 945dd6ee9a7b
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  note: Active power limited depending on AC frequency; no value stated.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26.r3
    h: 945dd6ee9a7b
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26.r3
    h: 945dd6ee9a7b
  review: drafted
---
