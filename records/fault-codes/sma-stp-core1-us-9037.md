---
id: fc:sma-stp-core1-us-9037
type: FaultCode
name: SMA CORE1-US 9037
aliases:
- '9037'
- SMA 9037
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '9037'
code_key: '9037'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r4
    h: ef67ddc41dfe
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r4
    h: ef67ddc41dfe
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:pv-array-not-connected
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r4
    h: ef67ddc41dfe
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r4
    h: ef67ddc41dfe
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c4
  rel: affects
  target: comp:pv-disconnect-switch
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r4
    h: ef67ddc41dfe
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r4
    h: ef67ddc41dfe
  review: drafted
---
