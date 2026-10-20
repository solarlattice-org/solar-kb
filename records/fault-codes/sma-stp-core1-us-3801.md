---
id: fc:sma-stp-core1-us-3801
type: FaultCode
name: SMA CORE1-US 3801
aliases:
- '3801'
- SMA 3801
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '3801'
code_key: '3801'
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r2
    h: 8a977edfc09d
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r2
    h: 8a977edfc09d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r2
    h: 8a977edfc09d
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r2
    h: 8a977edfc09d
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r2
    h: 8a977edfc09d
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r2
    h: 8a977edfc09d
  review: drafted
---
