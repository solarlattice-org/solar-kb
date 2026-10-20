---
id: fc:sma-stp-core1-us-10110
type: FaultCode
name: SMA CORE1-US 10110
aliases:
- '10110'
- SMA 10110
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10110'
code_key: '10110'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r8
    h: f12fd6a968ec
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r8
    h: f12fd6a968ec
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:time-sync-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r8
    h: f12fd6a968ec
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r8
    h: f12fd6a968ec
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:ntp-configuration-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r8
    h: f12fd6a968ec
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r8
    h: f12fd6a968ec
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
  rel: mitigated_by
  target: mit:network-connection-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r8
    h: f12fd6a968ec
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r8
    h: f12fd6a968ec
  review: drafted
---
